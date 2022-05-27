![python-version](https://img.shields.io/badge/python-v3.10-blue)
![license](https://img.shields.io/badge/license-MIT-green)

### Overleaf
https://www.overleaf.com/7557863444ptzfkkrvdqjk
### Google Calendar
https://calendar.google.com/calendar
### Planning
https://docs.google.com/document/d/1-InGPKSWdSScHAVy1Oyk3DItv9hBOH1Lgwy5Pj5Ojp8/edit?usp=sharing
### Google drive modelling-B directory with meetings, plannings and peer reviews
https://drive.google.com/drive/folders/1vBNFrfofDKTUi9H0g7Ep10lGsGGAuJqL?usp=sharing
### Trello
https://trello.com/b/cLFZ9x3D/modelleren-b

# Python environement setup
Please ensure you have Python version 3.10 installed. Note that an internet connection is required in order to use pyvis.

## Using a normal Python installation
### Using cmd
- Open `cmd.exe` in the root of `Modelling-B` as administrator and run `python -m venv venv && "venv/Scripts/activate.bat" && pip install -r requirements.txt`.
- To activate virtual environment use `"venv/Scripts/activate.bat"`.
- To deactivate virtual environment use `deactivate`.

### Using Git Bash
- Open Git Bash in the root of `Modelling-B` as administrator and run `python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt`.
- To activate virtual environment use `source venv/Scripts/activate`.
- To deactivate virtual environment use `deactivate`.

### Selecting Python interpreter in Visual Studio Code
- To select a the virtual environment, use the **Python: Select Interpreter** command from the **Command Palette** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) and enter `.\venv\Scripts\python.exe`.

## Using an Anaconda installation
Replace `C:/ProgramData/Anaconda3/` with `your/path/to/Anaconda3` in the code below in case they do not match.
- Open `cmd.exe` in the root of `Modelling-B` as administrator and run `"C:/ProgramData/Anaconda3/condabin/activate.bat" && conda env create -f environment.yml && conda activate modelling-b-venv`.
- To activate virtual environment use `conda activate modelling-b-venv`.
- To deactivate virtual environment use `conda deactivate`.

### Selecting Python interpreter in Anaconda
The interpreter is located at `C:\ProgramData\Anaconda3\envs\modelling-b-venv\python.exe`.
- To use Spyder, either activate the virtual environment and run `conda install spyder` and run `spyder` or activate the virtual environment from the Spyder console.
- To use Jupyter Notebook, activate the virutal environment and run `jupyter notebook`. Once you have selected a file you can select the virtual environment from **Kernel** > **Change kernel** > **Python 3 (ipykernel)**.

# TODO
- 

# Resources (bronnen)
- https://pyvis.readthedocs.io/en/latest/documentation.html
- https://medium.com/opex-analytics/optimization-modeling-in-python-pulp-gurobi-and-cplex-83a62129807a
- https://github.com/IBMPredictiveAnalytics/Simple_Linear_Programming_with_CPLEX/blob/master/source/main.py
- https://www.pythonpool.com/cplex-python/
- https://colab.research.google.com/github/Gurobi/modeling-examples/blob/master/intro_to_modeling/introduction_to_modeling_gcl.ipynb#scrollTo=mR1uBPyzgT9S
- https://www.gurobi.com/documentation/9.5/examples/diet_py.html
