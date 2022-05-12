from dataclasses import dataclass, field
import os
from custom_typing import NodeId
from integer_linear_problem import Ilp
import sys
import __main__
from config import Config
import utils
from graph_visualiser import visualise_graph


@dataclass(slots=True)
class Solution:
    input_filepath: str
    hubs: set[NodeId]
    non_hubs: set[NodeId]
    E: dict[NodeId, dict[NodeId, bool]]
    ilp: Ilp
    __id: int = field(init=False)
    __basename: str = field(init=False)
    __input_basename: str = field(init=False)
    __algo_dir_path: str = field(init=False)
    __save_dir_path: str = field(init=False)

    def __post_init__(self) -> None:
        base = __main__.__file__ # returns script name that was invoked from the command line (instead of this module)
        self.__basename = utils.remove_extension(base)

        self.__algo_dir_path = os.path.realpath(os.path.join(Config().OUT_DIR_PATH, self.__basename))

        self.__id = utils.count_dirs(self.__algo_dir_path) + 1

        self.input_filepath = os.path.realpath(self.input_filepath)
        input_base = os.path.basename(self.input_filepath)
        self.__input_basename = utils.remove_extension(input_base)

        save_dir_name = fr'{self.__id}-{self.__input_basename}-{utils.get_date("-")}'
        self.__save_dir_path = os.path.realpath(os.path.join(self.__algo_dir_path, save_dir_name))

    def visualise(self):
        '''visualise graph in an interactable graphical interface'''
        
        graph_base = fr'graph_{self.__id}_{}.html'
        visualise_graph

    def save(self):
        ...

    def print(self):
        ...

