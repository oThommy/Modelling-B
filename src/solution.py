from custom_typing import NodeId, IlpSolverData
from graph_visualiser import visualise_graph
from dataclasses import dataclass, field
from integer_linear_problem import Ilp
from datetime import datetime
from typing import Optional
from enum import Flag, auto
from config import Config
from pathlib import Path
import pandas as pd
import __main__
import utils
import dill


class Flags(Flag):
    LOG = auto()
    VISUALISE = auto()
    SAVE = auto()
    DEFAULT = LOG | VISUALISE | SAVE
    NONE = auto()

class AlreadySavedError(Exception):
     '''Raised when a Solution instance has already been saved'''
     pass

@dataclass(slots=True)
class Solution:
    '''
    The Solution class acts as a manager for solutions, providing the option to print, visualise or save the solution in a structured manner.

    WARNING: Using an unpickled Solution instance might result in unpredictable behaviour since the Solution class relies on the Config class, which may 
    have changed after the original Solution instance has been pickled.
    '''

    z: int
    hubs: set[NodeId]
    non_hubs: set[NodeId]
    E: dict[NodeId, dict[NodeId, bool]]
    ilp: Ilp
    algo_file: str
    timer: Optional[utils.Timer] = None
    ilp_solver_data: Optional[IlpSolverData] = None
    config_dict: dict = utils.default_fact_field(Config().to_dict(), init=False)
    __algo_basename: str = field(init=False)
    __date: datetime = field(init=False, default=datetime.now())
    __id: int = field(init=False)
    __is_saved: bool = field(init=False, default=False)

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
        self.__algo_basename = Path(self.algo_file).stem

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

    def save(self) -> Path:
        '''save solution for easy later lookup. a serialized version of this class' instance, a plain text file variant and optionally a graph.html (if you run Solution.visualise()) will be stored in OUT_DIR_PATH/{solver filename}/{id-} (see config for OUT_DIR_PATH). The directory path containing the saved files is returned.'''

        if (self.__is_saved):
            raise AlreadySavedError('You cannot save a Solution instance that has already been saved.')
        self.__is_saved = True

        utils.ensure_dir_exists(self.__save_dir_path)

        if self.__inputfile_basename is None:
            pickle_base = fr'solution_{self.__id}_{utils.get_formatted_date("_", self.__date)}.pickle'
        else:
            pickle_base = fr'solution_{self.__id}_{self.__inputfile_basename}_{utils.get_formatted_date("_", self.__date)}.pickle'

        pickle_path = self.__save_dir_path / pickle_base

        with open(pickle_path, 'wb') as file:
            dill.dump(self, file)

        if self.__inputfile_basename is None:
            solution_repr_base = fr'solution_repr_{self.__id}_{utils.get_formatted_date("_", self.__date)}.txt'
        else:
            solution_repr_base = fr'solution_repr_{self.__id}_{self.__inputfile_basename}_{utils.get_formatted_date("_", self.__date)}.txt'

        solution_repr_path = self.__save_dir_path / solution_repr_base

        with open(solution_repr_path, 'w') as file:
            file.write(repr(self))

        print(f'The solution is successfully saved to {self.__save_dir_path}.')

        return self.__save_dir_path

    def print(self) -> None:
        print(f'===== Solution from {self.__algo_basename} =====')

        if self.timer is not None:
            print(f'Total time: {self.timer.total_time}')

        if self.ilp_solver_data is not None:
            print(f'ILP Solver Type: {self.ilp_solver_data["type"]}')
            print(f'ILP Solver Status: {self.ilp_solver_data["status"]}')

        print(f'z = {self.z}')
        print(f'hubs = {self.hubs}')
        print(f'non-hubs = {self.non_hubs}')

        E_df = pd.DataFrame.from_dict(self.E).T # display it as the column being the origin and row the destination
        print(f'E = ')
        print(E_df)

        print(self)

    def run(self, flags: Flags) -> None:
        if ~(flags & Flags.NONE):
            if flags & Flags.LOG:
                self.print()

            if flags & Flags.VISUALISE:
                self.visualise()

            if flags & Flags.SAVE:
                self.save()

    def to_dict(self) -> dict:
        d = {
            'z': self.z,
            'hubs': self.hubs,
            'non_hubs': self.non_hubs,
            'E': self.E,
            '__date': self.__date,
            '__id': self.__id,
            '__algo_basename': self.__algo_basename,
            '__is_saved': self.__is_saved,
            '__algo_dir_path': self.__algo_dir_path,
            '__inputfile_basename': self.__inputfile_basename,
            '__save_dir_path': self.__save_dir_path,
            'ilp': self.ilp,
            'config_dict': self.config_dict,
        }

        if self.timer is not None:
            d['timer'] = self.timer

        if self.ilp_solver_data is not None:
            d['ilp_solver_data'] = self.ilp_solver_data 

        return d

    def __repr__(self) -> str:
        rep = f'''
Solution(
    {str(self.to_dict())}
)
        '''
        return rep

    def __str__(self) -> str:
        return repr(self)