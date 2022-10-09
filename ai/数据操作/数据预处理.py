import os
import pandas as pd
import torch

# os.mkdir(os.path.join('..', 'data'))
datafile = os.path.join('..', 'data', 'house_tiny.csv')
# with open(datafile, 'w') as f:
#     f.write('NumRooms,Alley,Price\n')
#     f.write('NA,Pave,127500\n')
#     f.write('2,NA,10600\n')
#     f.write('4,NA,12000\n')
#     f.write('NA,NA,14300\n')

data = pd.read_csv(datafile)
# print(data)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
# print(inputs)

inputs = pd.get_dummies(inputs, dummy_na=True)
# print(inputs)

x, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
print(x)
print(y)
