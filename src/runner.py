import ilp_solver
from intuitive_algo_1 import intuitive_algo_1
from intuitive_algo_2 import intuitive_algo_2
from integer_linear_problem import Ilp
from solution import Flags
from config import Config


def main() -> None:
    ilp = Ilp.from_excel(Config().DATA_SMALL_PATH)

    intuitive_algo_2(ilp, annotation='testing Solution custom path saving', algo_dir_path=Config().OUT_DIR_PATH / r'test/yeet')


if __name__ == '__main__':
    main()