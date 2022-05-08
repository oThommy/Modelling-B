
from typing import Protocol, TypeVar


K = TypeVar('K')
V = TypeVar('V')

class NodeId:
    pass

class Series(Protocol[K, V]):
    pass

class DataFrame(Protocol[K, V]):
    pass