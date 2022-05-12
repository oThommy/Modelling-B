from dataclasses import dataclass
import os
import __main__
from config import Config
from integer_linear_problem import Ilp
import utils
from datetime import datetime

# print(Config().ROOT_DIR_PATH)
# print(Config().OUT_DIR_PATH)
# print(os.path.relpath(Config().OUT_DIR_PATH))
# os.makedirs('YEET', exist_ok=False)

# from datetime import datetime

# print(fr'5--{datetime.now():%Y-%m-%d-%H-%M-%S}')


# dir_path = os.path.realpath(os.path.join(Config().ROOT_DIR_PATH, 'yeet', 'hi'))
# print(dir_path)
# os.makedirs(dir_path)

# print(utils.get_date('-'))
print(Config().GRAPH_OPTIONS)
# print(datetime.now().strftime('-'.join('%Y', '%m', '%d', '%H', '%M', '%S')))