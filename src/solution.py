from dataclasses import dataclass, field
from datetime import datetime
from custom_typing import NodeId
from integer_linear_problem import Ilp
import sys
import __main__
from config import Config
import utils
from graph_visualiser import visualise_graph
import pickle
from pathlib import Path


@dataclass(slots=True)
class Solution:
    z: int
    hubs: set[NodeId]
    non_hubs: set[NodeId]
    E: dict[NodeId, dict[NodeId, bool]]
    ilp: Ilp
    __date: datetime = field(init=False, default=datetime.now())
    __id: int = field(init=False)
    __algo_basename: str = field(
        init=False, 
        default=Path(__main__.__file__).stem # returns script name that was invoked from the command line (instead of this module)
    )

    @property
    def __algo_dir_path(self) -> Path:
        return Config().OUT_DIR_PATH / self.__algo_basename

    @property
    def __inputfile_basename(self) -> Path:
        return self.ilp.inputfile_path.stem if self.ilp.inputfile_path is not None else None

    @property
    def __save_dir_path(self) -> Path:
        if self.__inputfile_basename is None:
            save_dir_name = fr'{self.__id}-{utils.get_formatted_date("-", self.__date)}'
        else:
            save_dir_name = fr'{self.__id}-{self.__inputfile_basename}-{utils.get_formatted_date("-", self.__date)}'

        return self.__algo_dir_path / save_dir_name

    def __post_init__(self) -> None:
        if self.__algo_dir_path.exists():
            self.__id = utils.count_dirs(self.__algo_dir_path) + 1
        else:
            self.__id = 1

    def visualise(self) -> None:
        '''visualise graph in an interactable graphical interface'''
        
        utils.ensure_dir_exists(self.__save_dir_path)

        if self.__inputfile_basename is None:
            graph_base = fr'graph_{self.__id}_{utils.get_formatted_date("_", self.__date)}.html'
        else:
            graph_base = fr'graph_{self.__id}_{self.__inputfile_basename}_{utils.get_formatted_date("_", self.__date)}.html'

        graph_path = self.__save_dir_path / graph_base

        visualise_graph(self.hubs, self.non_hubs, self.E, self.ilp, graph_path)

    def save(self) -> None:
        '''save solution for easy later lookup. a serialized version of this class' instance, a json variant, a plain text file variant and optionally a graph.html (if you run Solution.visualise()) will be stored in OUT_DIR_PATH/{solver filename}/{id-} (see config for OUT_DIR_PATH)'''

        utils.ensure_dir_exists(self.__save_dir_path)

        if self.__inputfile_basename is None:
            pickle_base = fr'solution_{self.__id}_{utils.get_formatted_date("_", self.__date)}.pickle'
        else:
            pickle_base = fr'solution_{self.__id}_{self.__inputfile_basename}_{utils.get_formatted_date("_", self.__date)}.pickle'

        pickle_path = self.__save_dir_path / pickle_base
        
        with open(pickle_path, 'wb') as file:
            pickle.dump(self, file, Config().PICKLE_PROTOCOL)

    def print(self):
        print(self.__algo_dir_path)
        print(self.__save_dir_path)
        print(self.__inputfile_basename)