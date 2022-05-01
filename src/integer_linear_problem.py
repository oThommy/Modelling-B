from typing import Dict, List, Set
import pandas as pd
import numpy as np
import json
import os

NodeId = int

# removes all columns that start with 'Unnamed:'
def df_drop_unnamed_cols(df: pd.DataFrame):
    return df[df.columns.drop(list(df.filter(regex=r'^Unnamed:')))]

class ILP:
    filepath: str
    N: Set[NodeId]
    collection: int
    transfer: int
    distribution: int
    w: Dict[NodeId, Dict[NodeId, int]]
    c: Dict[NodeId, Dict[NodeId, int]]
    f: Dict[NodeId, int]

    def __init__(self, filepath: str):
        self.filepath = os.path.abspath(filepath)

        # read excel file into dataframes
        gen_info_df = pd.read_excel(self.filepath, sheet_name='General information', usecols='A:B', index_col=0, header=None)
        # due to a mistake in the excel dataset, the collection may contain an extra space
        try:
            self.collection = gen_info_df.loc['collection '].iloc[0]
        except:
            self.collection = gen_info_df.loc['collection'].iloc[0]
        self.transfer = gen_info_df.loc['transfer'].iloc[0]
        self.distribution = gen_info_df.loc['distribution'].iloc[0]

        w_df = pd.read_excel(filepath, sheet_name='w', index_col=0)
        w_df = df_drop_unnamed_cols(w_df)
        self.w = w_df.to_dict()

        c_df = pd.read_excel(filepath, sheet_name='c', index_col=0)
        c_df = df_drop_unnamed_cols(c_df)
        self.c = c_df.to_dict()

        f_df = pd.read_excel(filepath, sheet_name='f', index_col=0, header=None)
        self.f = f_df.iloc[:, 0].to_dict()
        self.N = set(range(1, len(self.f) + 1))
        
    # returns the value of the function that should be minimized
    def get_z(self, H: Dict[NodeId, bool], y: Dict[NodeId, Dict[NodeId, Dict[NodeId, Dict[NodeId, bool]]]]) -> int:
        pass # TODO: implement z function

    def __repr__(self) -> str:
        rep = f"""
ILP(
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