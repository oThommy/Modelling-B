from dataclasses import dataclass
from custom_typing import Singleton
from pathlib import Path
import utils


@dataclass(frozen=True, slots=True)
class Config(Singleton):
    '''Contains all the configurations
    
    To get a config value, use Config().ATTRIBUTE_NAME.
    '''

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

        return self.OUT_DIR_PATH / r'other-graphs'

    @property
    def DATA_VERY_SMALL_PATH(self) -> Path:
        return self.IN_DIR_PATH / r'Data assignment parcel transport 2 very small Small.xlsx'

    @property
    def DATA_SMALL_PATH(self) -> Path:
        return self.IN_DIR_PATH / r'Data assignment parcel transport 2 Small.xlsx'

    @property
    def DATA_LARGE_PATH(self) -> Path:
        return self.IN_DIR_PATH / r'Data assignment parcel transport 2 Large.xlsx'

    @property
    def DATA_MEDIUM_HUGE_PATH(self) -> Path:
        return self.IN_DIR_PATH / r'Data assignment parcel transport 2 medium huge.xlsx'
    
    @property
    def DATA_HUGE_PATH(self) -> Path:
        return self.IN_DIR_PATH / r'Data assignment parcel transport 2 huge.xlsx'

    # OTHER
    TQDM_NCOLS: int = 100

    # GRAPH VISUALISER
    NETWORK_WIDTH: str = '100%'
    NETWORK_HEIGHT: str = '100%'
    NETWORK_BGCOLOR: str = '#222222'
    NETWORK_FONT_COLOR: str = 'white'
    MIN_NODE_SIZE: int = 20
    MAX_NODE_SIZE: int = 55
    MIN_EDGE_WIDTH: int = 7
    MAX_EDGE_WIDTH: int = 25
    DEFAULT_EDGE_WIDTH: int = 15
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

    def to_dict(self) -> dict:
        return {
            'ROOT_DIR_PATH': self.ROOT_DIR_PATH,
            'OUT_DIR_PATH': self.OUT_DIR_PATH,
            'IN_DIR_PATH': self.IN_DIR_PATH,
            'OTHER_GRAPHS_DIR_PATH': self.OTHER_GRAPHS_DIR_PATH,
            'DATA_VERY_SMALL_PATH': self.DATA_VERY_SMALL_PATH,
            'DATA_SMALL_PATH': self.DATA_SMALL_PATH,
            'DATA_LARGE_PATH': self.DATA_LARGE_PATH,
            'DATA_MEDIUM_HUGE_PATH': self.DATA_MEDIUM_HUGE_PATH,
            'DATA_HUGE_PATH': self.DATA_HUGE_PATH,
            'TQDM_NCOLS': self.TQDM_NCOLS,
            'MIN_NODE_SIZE': self.MIN_NODE_SIZE,
            'MAX_NODE_SIZE': self.MAX_NODE_SIZE,
            'MIN_EDGE_WIDTH': self.MIN_EDGE_WIDTH,
            'MAX_EDGE_WIDTH': self.MAX_EDGE_WIDTH,
            'GRAPH_OPTIONS': self.GRAPH_OPTIONS,
        }

    def __repr__(self) -> str:
        rep = f'''
Config(
    {str(self.to_dict())}
)
        '''
        return rep

    def __str__(self) -> str:
        return repr(self)