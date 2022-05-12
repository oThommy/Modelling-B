from dataclasses import dataclass, field
from custom_typing import Singleton
import os


@dataclass(frozen=True, slots=True)
class Config(Singleton):
    # PATHS
    ROOT_DIR_PATH: str = os.path.realpath(os.path.dirname(__file__))
    OUT_DIR_PATH: str = os.path.realpath(os.path.join(ROOT_DIR_PATH, r'out'))
    IN_DIR_PATH: str = os.path.realpath(os.path.join(ROOT_DIR_PATH, r'in'))
    OTHER_GRAPHS_DIR_PATH: str = os.path.realpath(os.path.join(OUT_DIR_PATH, r'other-graphs')) # directory for random graphs

    DATA_VERY_SMALL_PATH: str = os.path.realpath(os.path.join(IN_DIR_PATH, r'Data assignment parcel transport 2 very small Small.xlsx'))
    DATA_SMALL_PATH: str = os.path.realpath(os.path.join(IN_DIR_PATH, r'Data assignment parcel transport 2 very small Small.xlsx'))
    DATA_LARGE_PATH: str = os.path.realpath(os.path.join(IN_DIR_PATH, r'Data assignment parcel transport 2 very small Small.xlsx'))

    # OTHER
    TQDM_NCOLS: int = 100

    # GRAPH VISUALISER
    MIN_NODE_SIZE: int = 20
    MAX_NODE_SIZE: int = 55
    MIN_EDGE_WIDTH: int = 7
    MAX_EDGE_WIDTH: int = 25
    GRAPH_OPTIONS: dict = field(default_factory={
        'nodes': {
            'borderWidthSelected': 3,
            'color': {
                'border': 'rgba(43,124,233,1)',
                'background': 'rgba(151,194,252,1)',
                'highlight': {
                    'border': 'rgba(43,124,233,1)',
                    'background': 'rgba(210,229,255,1)'
                },
                'hover': {
                    'border': 'rgba(43,124,233,1)',
                    'background': 'rgba(210,229,255,1)'
                }
            },
            'scaling': {
                'min': MIN_NODE_SIZE,
                'max': MAX_NODE_SIZE,
            },
            "font": {
                "size": 20
            }
        },
        'edges': {
            'color': {
                'inherit': False,
                'color': 'rgba(43,124,233,1)',
                'highlight': 'rgba(114,166,229,1)',
                'hover': 'rgba(114,166,229,1)'
            },
            'hoverWidth': 1.5,
            'smooth': False,
            'scaling': {
                'min': MIN_EDGE_WIDTH,
                'max': MAX_EDGE_WIDTH
            },
            'smooth': {
                'type': 'discrete',
                'roundness': 0.6
            },
        },
        'physics': {
            'hierarchicalRepulsion': {
                'centralGravity': 0,
                'springLength': 150,
                'springConstant': 0.01,
                'damping': 0.09,
                'nodeDistance': 300
            },
            'minVelocity': 0.75,
            'solver': 'hierarchicalRepulsion'
        },
        # 'physics': {
        #     'barnesHut': {
        #         'centralGravity': 0,
        #         'springLength': 300,
        #         'springConstant': 0.01,
        #         'damping': 0.09,
        #     },
        #     'minVelocity': 0.75,
        #     'solver': 'barnesHut'
        # }
    })