from typing_extensions import Self
from custom_typing import NodeId
from typing import Optional
from config import Config
from pathlib import Path
import pandas as pd
import utils


class Ilp:
    '''Ilp Dataset Manager
    
    inputfile_path must reside in in Config().IN_DIR_PATH.
    Ilp.w and Ilp.c both interpret the Excel column as the origin and the row as the destination.
    '''

    __slots__ = '__N', '__collection', '__transfer', '__distribution', '__w', '__c', '__f', '__inputfile_basename'

    def __init__(
        self,
        N: set[NodeId],
        collection: int,
        transfer: int,
        distribution: int,
        w: dict[NodeId, dict[NodeId, int]],
        c: dict[NodeId, dict[NodeId, int]],
        f: dict[NodeId, int],
        inputfile_path: Optional[Path | str] = None
    ) -> None:

        self.__N = N
        self.__collection = collection
        self.__transfer = transfer
        self.__distribution = distribution
        self.__w = w
        self.__c = c
        self.__f = f
        self.__inputfile_basename = Path(inputfile_path).name if inputfile_path is not None else None

    @classmethod
    def from_excel(cls, inputfile_path: Path | str) -> Self:
        '''Load Ilp dataset from excel. inputfile_path must be in Config().IN_DIR_PATH'''

        inputfile_basename = Path(inputfile_path).name
        inputfile_path = Config().IN_DIR_PATH / inputfile_basename

        gen_info_ser = pd.read_excel(inputfile_path, sheet_name='General information', header=None, index_col=0).squeeze('columns')
        # due to a mistake in the excel dataset, the collection may contain an extra space
        try:
            collection = gen_info_ser['collection ']
        except:
            collection = gen_info_ser['collection']
        collection = utils.to_int(collection)
        transfer = utils.to_int(gen_info_ser['transfer'])
        distribution = utils.to_int(gen_info_ser['distribution'])

        # take transpose since vertical column is the origin and horizontal row the destination
        w_df = pd.read_excel(inputfile_path, sheet_name='w', index_col=0).T
        w_df = Ilp.df_drop_unnamed_cols(w_df)
        w = w_df.to_dict()
        w = utils.dict_dtypes_to_int(w)

        c_df = pd.read_excel(inputfile_path, sheet_name='c', index_col=0).T
        c_df = Ilp.df_drop_unnamed_cols(c_df)
        c = c_df.to_dict()
        c = utils.dict_dtypes_to_int(c)

        f_ser = pd.read_excel(inputfile_path, sheet_name='f', index_col=0, header=None).squeeze('columns')
        N = set(f_ser.index.astype(int))
        f = f_ser.to_dict()
        f = utils.dict_dtypes_to_int(f)

        return cls(N, collection, transfer, distribution, w, c, f, inputfile_basename)

    @staticmethod
    def df_drop_unnamed_cols(df: pd.DataFrame) -> pd.DataFrame:
        """removes all columns that start with 'Unnamed:'"""

        return df[df.columns.drop(list(df.filter(regex=r'^Unnamed:')))]

    @property
    def N(self) -> set[NodeId]:
        return self.__N

    @property
    def collection(self) -> int:
        return self.__collection
    
    @property
    def transfer(self) -> int:
        return self.__transfer
    
    @property
    def distribution(self) -> int:
        return self.__distribution
    
    @property
    def w(self) -> dict[NodeId, dict[NodeId, int]]:
        return self.__w
    
    @property
    def c(self) -> dict[NodeId, dict[NodeId, int]]:
        return self.__c
    
    @property
    def f(self) -> dict[NodeId, int]:
        return self.__f
    
    @property
    def inputfile_path(self) -> Optional[Path]:
        return Config().IN_DIR_PATH / self.__inputfile_basename if self.__inputfile_basename is not None else None
    
    @property
    def w_df(self) -> pd.DataFrame:
        return pd.DataFrame.from_dict(self.w)

    @property
    def c_df(self) -> pd.DataFrame:
        return pd.DataFrame.from_dict(self.c)

    @property
    def f_ser(self) -> pd.Series:
        return pd.Series(self.f)

    def get_z_single_hub(self, hub: NodeId, non_hubs: set[NodeId]) -> int:
        '''returns the value of the function that should be minimized for a single hub'''

        z = 0

        # add fixed costs for establishing hub
        z += self.f[hub]

        for non_hub_dest in non_hubs:
            # add costs of type hub to non-hub
            z += self.w[hub][non_hub_dest] * self.distribution * self.c[hub][non_hub_dest]

            for non_hub_src in non_hubs:
                # add costs of type non-hub to non-hub
                z += self.w[non_hub_src][non_hub_dest] * (self.collection * self.c[non_hub_src][hub] + self.distribution * self.c[hub][non_hub_dest])
        
        return z

    def get_z_multiple_hubs(self, H: dict[NodeId, bool], E: dict[NodeId, dict[NodeId, bool]]) -> int:
        '''returns the value of the function that should be minimized for multiple hubs'''

        z = 0

        for i in self.__N:
            # add fixed costs for establishing hubs
            z += H[i] * self.__f[i]

            for j in self.__N:
                # add costs of type hub to hub
                z += H[i] * H[j] * self.__w[i][j] * self.__transfer * self.__c[i][j]
                
                for k in self.__N:
                    # add costs of type non-hub to hub
                    z += (1 - H[i]) * H[j] * E[i][k] * self.__w[i][j] * (self.__collection * self.__c[i][k] + self.__transfer * self.__c[k][j])
                    
                    # add costs of type hub to non-hub
                    z += H[i] * (1 - H[j]) * E[k][j] * self.__w[i][j] * (self.__transfer * self.__c[i][k] + self.__distribution * self.__c[k][j])
                    
                    for l in self.__N:
                        # add costs of type non-hub to non-hub
                        z += (1 - H[i]) * (1 - H[j]) * E[i][k] * E[l][j] * self.__w[i][j] * (self.__distribution * self.__c[l][j] + self.__transfer * self.__c[k][l] + self.__collection * self.__c[i][k])
                        
        return z

    def to_dict(self) -> dict:
        return {
            'N': self.N,
            'collection': self.collection,
            'transfer': self.transfer,
            'distribution': self.distribution,
            'w': self.w,
            'c': self.c,
            'f': self.f,
            'inputfile_path': self.inputfile_path,
            '__inputfile_basename': self.__inputfile_basename,
        }

    def __repr__(self) -> str:
        rep = f'''
Ilp(
    {str(self.to_dict())}
)
        '''
        return rep

    def __str__(self) -> str:
        return repr(self)