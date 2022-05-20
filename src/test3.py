from config import Config
import pickle
import dill

with open('TESTCONFIG.pickle', 'wb') as file:
    dill.dump(Config(), file)

print()