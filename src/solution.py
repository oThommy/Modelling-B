from dataclasses import dataclass, field
import os
from custom_typing import NodeId
from integer_linear_problem import Ilp
import sys


@dataclass(frozen=True, slots=True)
class Solution:
    hubs: set[NodeId]
    non_hubs: set[NodeId]
    E: dict[NodeId, dict[NodeId, bool]]
    ilp: Ilp
    __basename: str = field(
        init=False,  #https://stackoverflow.com/questions/4152963/get-name-of-current-script-in-python#:~:text=You%20can%20use%20__file,path.
        default=os.path.basename(sys.argv[0]) # returns script name that was invoked from the command line (instead of this module)
    )
    # date
    # ID
    def visualise(self):
        ...

    def print(self):
        ...

    def save(self):
        ...

    def test(self):
        print(