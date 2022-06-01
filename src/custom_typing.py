
from typing import Concatenate, Protocol, TypeVar, TypedDict, Callable, ParamSpec, NewType
import functools


T = TypeVar('T')
P = ParamSpec('P')
K = TypeVar('K')
V = TypeVar('V')

Version = NewType('Version', str)

class NodeId(int):
    pass

class Series(Protocol[K, V]):
    pass

class DataFrame(Protocol[K, V]):
    pass

def version(version_number: str = '1.0') -> Callable[[Callable[Concatenate[Version, P], T]], Callable[P, T]]:
    '''Add version number to a function. The function is required to have a Version typed parameter as its first parameter.'''

    __version__ = f'v{version_number}'

    def version_decorator(fn: Callable[Concatenate[Version, P], T]) -> Callable[P, T]:
        @functools.wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            retval = fn(__version__, *args, **kwargs)
            return retval
        return wrapper
    return version_decorator

class IlpSolverData(TypedDict):
    type: str
    status: str
    version: Version

class Singleton:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance