from dataclasses import dataclass
from custom_typing import Singleton
from pathlib import Path
import utils


@dataclass(frozen=True, slots=True)
class Config(Singleton):
    # PATHS
    @property
    def ROOT_DIR_PATH(self) -> Path:
        return Path(__file__).parent

    @property
    def OUT_DIR_PATH(self) -> Path:
        return self.ROOT_DIR_PATH / r'out'

    @property
    def IN_DIR_PATH(self) -> Path:
        return self.ROOT_DIR_PATH / r'in'

    @property
    def OTHER_GRAPHS_DIR_PATH(self) -> Path:
        '''directory for random graphs'''

        return self.ROOT_DIR_PATH / r'other-graphs'

    @property
    def DATA_VERY_SMALL_PATH(self) -> Path:
        return self.IN_DIR_PATH / r'Data assignment parcel transport 2 very small Small.xlsx'

    @property
    def DATA_SMALL_PATH(self) -> Path:
        return self.IN_DIR_PATH / r'Data assignment parcel transport 2 very small Small.xlsx'

    @property
    def DATA_LARGE_PATH(self) -> Path:
        return self.IN_DIR_PATH / r'Data assignment parcel transport 2 very small Small.xlsx'

    @property
    def DATA_HUGE_PATH(self) -> Path:
        return self.IN_DIR_PATH / r'Data assignment parcel transport 2 huge.xlsx'

    # OTHER
    TQDM_NCOLS: int = 100
    PICKLE_PROTOCOL: int = 5

    # GRAPH VISUALISER
    MIN_NODE_SIZE: int = 20
    MAX_NODE_SIZE: int = 55
    MIN_EDGE_WIDTH: int = 7
    MAX_EDGE_WIDTH: int = 25
    GRAPH_OPTIONS: dict = utils.default_fact_field({
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