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
Please ensure you have Python version 3.10 installed.

## Using a normal Python installation
### Using cmd
- Open `cmd.exe` in the root of `Modelling-B` as administrator and run `python -m venv venv && "venv/Scripts/activate.bat" && pip install -r requirements.txt`.
- To activate virtual environment use `"venv/Scripts/activate.bat"`.
- To deactivate virtual environment use `deactivate`.

### Using Git Bash
- Open Git Bash in the root of `Modelling-B` as administrator and run `python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt`.
- To activate virtual environment use `source venv/Scripts/activate`.
- To deactivate virtual environment use `deactivate`.

## Using an Anaconda installation
Replace `C:/ProgramData/Anaconda3/` with `your/path/to/Anaconda3` in the code below in case they do not match.
- Open `cmd.exe` in the root of `Modelling-B` as administrator and run `"C:/ProgramData/Anaconda3/condabin/activate.bat" && conda env create -f environment.yml && conda activate modelling-b-venv`.
- To activate virtual environment use `conda activate modelling-b-venv`.
- To deactivate virtual environment use `deactivate`.

Note that an internet connection is required in order to use pyvis.

# TODO
- 

# Resources (bronnen)
- https://pyvis.readthedocs.io/en/latest/documentation.html
- https://medium.com/opex-analytics/optimization-modeling-in-python-pulp-gurobi-and-cplex-83a62129807a

# Other
- brightspace-locker is a container for all finalized files that are uploaded to the brightspace-locker
