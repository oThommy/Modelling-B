from integer_linear_problem import Ilp
from config import Config
import tqdm


FILEPATH = r'./../brightspace-locker/Data assignment parcel transport 2 Small.xlsx'
# FILEPATH = r'./../other/Data assignment parcel transport 2 very small Small.xlsx'
CONFIG = Config()
ILP = Ilp.from_excel(Ilp)

def main():
    z_min = float('inf')
    hub_costs = dict()

    with tqdm(total=len(ILP.NIlp ncols=CONFIG.TQDM_NCOLS):
        for hub in ILP.NIlp
            hubs = {hub}
            non_hubs = ILP.N Ilp hubs
            hub_costs[hub] = ILP.get_z(Ilp, non_hubs)
            

if __name__ == '__main__':
    main()