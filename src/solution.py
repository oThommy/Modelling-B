from dataclasses import dataclass, field
from datetime import datetime
import os
from custom_typing import NodeId
from integer_linear_problem import Ilp
import sys
import __main__
from config import Config
import utils
from graph_visualiser import visualise_graph
import pickle


@dataclass(slots=True)
class Solution:
    z: int
    hubs: set[NodeId]
    non_hubs: set[NodeId]
    E: dict[NodeId, dict[NodeId, bool]]
    ilp: Ilp
    __date: datetime = field(init=False, default=datetime.now())
    __id: int = field(init=False)
    __basename: str = field(init=False)
    __input_basename: str = field(init=False)
    __algo_dir_path: str = field(init=False)
    __save_dir_path: str = field(init=False)

    def __post_init__(self) -> None:
        base = os.path.basename(__main__.__file__) # returns script name that was invoked from the command line (instead of this module)
        self.__basename = utils.remove_extension(base)

        self.__algo_dir_path = os.path.realpath(os.path.join(Config().OUT_DIR_PATH, self.__basename))

        if os.path.exists(self.__algo_dir_path):
            self.__id = utils.count_dirs(self.__algo_dir_path) + 1
        else:
            self.__id = 1

        if self.ilp.filepath is not None:
            input_filepath = os.path.realpath(self.ilp.filepath)
            input_base = os.path.basename(input_filepath)
            self.__input_basename = utils.remove_extension(input_base)

        save_dir_name = fr'{self.__id}-{self.__input_basename}-{utils.get_formatted_date("-", self.__date)}'
        self.__save_dir_path = os.path.realpath(os.path.join(self.__algo_dir_path, save_dir_name))

    def visualise(self) -> None:
        '''visualise graph in an interactable graphical interface'''
        
        utils.ensure_dir_exists(self.__save_dir_path)

        graph_base = fr'graph_{self.__id}_{self.__input_basename}_{utils.get_formatted_date("_", self.__date)}.html'
        graph_path = os.path.realpath(os.path.join(self.__save_dir_path, graph_base))

        visualise_graph(self.hubs, self.non_hubs, self.E, self.ilp, graph_path)

    def save(self) -> None:
        '''save solution for easy later lookup. a serialized version of this class' instance, a json variant, a plain text file variant and optionally a graph.html (if you run Solution.visualise()) will be stored in OUT_DIR_PATH/{solver filename}/{id-} (see config for OUT_DIR_PATH)'''

        utils.ensure_dir_exists(self.__save_dir_path)

        pickle_base = fr'solution_{self.__id}_{self.__input_basename}_{utils.get_formatted_date("_", self.__date)}.pickle'
        pickle_path = os.path.realpath(os.path.join(self.__save_dir_path, pickle_base))
        with open(pickle_path, 'wb') as file:
            pickle.dump(self, file, Config().PICKLE_PROTOCOL)



    def print(self):
        ...

