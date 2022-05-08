from dataclasses import dataclass
import os


@dataclass(frozen=True, slots=True)
class Config:
    GRAPHS_DIR_PATH: str = os.path.relpath(r'./graphs')