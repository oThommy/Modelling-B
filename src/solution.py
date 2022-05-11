from dataclasses import dataclass
from custom_typing import NodeId

@dataclass(frozen=True, slots=True)
class Solution:
    hubs: set[NodeId]
    non_hubs: set[NodeId]
    E: dict[NodeId, dict[NodeId, bool]]

    def visualise_solution():
        visualise_graph