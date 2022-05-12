
from typing import Protocol, TypeVar


K = TypeVar('K')
V = TypeVar('V')

class NodeId(int):
    pass

class Series(Protocol[K, V]):
    pass

class DataFrame(Protocol[K, V]):
    pass

class Singleton:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance