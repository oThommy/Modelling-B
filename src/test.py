import pandas as pd

df = pd.read_excel(r'./../other/Data assignment parcel transport 2 Small.xlsx', usecols='A:B', header=None) #, sheet_name='General information', header=None
# df = pd.DataFrame(data)
print(df)