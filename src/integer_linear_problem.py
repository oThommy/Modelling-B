from custom_typing import NodeId, Series, DataFrame
from typing import Optional, TypeAlias, TypeVar
from typing_extensions import Self
import pandas as pd
import numpy as np
import json
import os


class Ilp:
    __slots__ = '__N', '__collection', '__transfer', '__distribution', '__w', '__c', '__f', '__filepath'

    def __init__(
        self,
        N: set[NodeId],
        collection: int,
        transfer: int,
        distribution: int,
        w: DataFrame[NodeId, Series[NodeId, int]] | dict[NodeId, dict[NodeId, int]],
        c: DataFrame[NodeId, Series[NodeId, int]] | dict[NodeId, dict[NodeId, int]],
        f: Series[NodeId, int] | dict[NodeId, int],
        filepath: Optional[str] = None
    ) -> None:

        self.__N = N
        self.__collection = collection
        self.__transfer = transfer
        self.__distribution = distribution

        if isinstance(w, dict):
            w = pd.DataFrame.from_dict(w)
        self.__w = w

        if isinstance(c, dict):
            c = pd.DataFrame.from_dict(c)
        self.__c = c

        if isinstance(f, dict):
            f = pd.Series(f)
        self.__f = f

        self.__filepath = os.path.abspath(filepath) if filepath is not None else None

    @classmethod
    def from_excel(cls, filepath: str) -> Self:
        '''Load Ilp dataset from excel'''

        filepath = os.path.abspath(filepath)

        gen_info_ser = pd.read_excel(filepath, sheet_name='General information', header=None, index_col=0).squeeze('columns')
        # due to a mistake in the excel dataset, the collection may contain an extra space
        try:
            collection = gen_info_ser['collection ']
        except:
            collection = gen_info_ser['collection']
        transfer = gen_info_ser['transfer']
        distribution = gen_info_ser['distribution']

        # take transpose since vertical column is the origin and horizontal row the destination
        w_df = pd.read_excel(filepath, sheet_name='w', index_col=0).T
        w_df = Ilp.df_drop_unnamed_cols(w_df)

        c_df = pd.read_excel(filepath, sheet_name='c', index_col=0).T
        c_df = Ilp.df_drop_unnamed_cols(c_df)

        f_ser = pd.read_excel(filepath, sheet_name='f', index_col=0, header=None).squeeze('columns')
        N = set(f_ser.index)

        return cls(N, collection, transfer, distribution, w_df, c_df, f_ser, filepath)

    @staticmethod
    def df_drop_unnamed_cols(df: pd.DataFrame):
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
    def w(self) -> DataFrame[NodeId, Series[NodeId, int]]:
        return self.__w
    
    @property
    def c(self) -> DataFrame[NodeId, Series[NodeId, int]]:
        return self.__c
    
    @property
    def f(self) -> Series[NodeId, int]:
        return self.__f
    
    @property
    def filepath(self) -> Optional[str]:
        return self.__filepath
    
    def get_z(
        self, 
        hubs: set[NodeId], 
        non_hubs: set[NodeId], 
        E: Optional[DataFrame[NodeId, Series[NodeId, bool]]] = None
    ) -> int:

        '''returns the value of the function that should be minimized'''

        if len(hubs) == 1:
            return self._get_z_single_hub(next(iter(hubs)), non_hubs)
        else:
            return self._get_z_multiple_hubs(hubs, non_hubs, E)

    # @overload
    # def get_z(self, H: Series[NodeId, bool], E: DataFrame[NodeId, Series[NodeId, bool]]) -> int:
    #     FIXME: ADD COMMENT

    #     z = 0

    #     for i in self.N:
    #         # add fixed costs for establishing hubs
    #         z += H[i] * self.f[i]

    #         for j in self.N:
    #             # add costs of type hub to hub
    #             z += H[i] * H[j] * self.w[i][j] * self.transfer * self.c[i][j]
                
    #             for k in self.N:
    #                 # add costs of type non-hub to hub
    #                 z += (1 - H[i]) * H[j] * E[i][k] * self.w[i][j] * (self.collection * self.c[i][k] + self.transfer * self.c[k][j])
                    
    #                 # add costs of type hub to non-hub
    #                 z += H[i] * (1 - H[j]) * E[k][j] * self.w[i][j] * (self.transfer * self.c[i][k] + self.distribution * self.c[k][j])
                    
    #                 for l in self.N:
    #                     # add costs of type non-hub to non-hub
    #                     z += (1 - H[i]) * (1 - H[j]) * E[i][k] * E[l][j] * self.w[i][j] * (self.distribution * self.c[l][j] + self.transfer * self.c[k][l] + self.collection * self.c[i][k])

    #     return z

    def _get_z_single_hub(self, hub: NodeId, non_hubs: set[NodeId]) -> int:
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

    def _get_z_multiple_hubs() -> int:
        pass

    def __repr__(self) -> str:
        rep = f"""
Ilp(
    filepath: {self.filepath}
    N: {self.N}
    collection: {self.collection}
    transfer: {self.transfer}
    distribution: {self.distribution}
    w: {json.dumps(self.w, indent=4)}
    c: {json.dumps(self.c, indent=4)}
    f: {json.dumps(self.f, indent=4)}
)
        """
        return rep

    def __str__(self) -> str:
        return repr(self)