import pandas as pd
import numpy as np
from datetime import datetime
import sys
import json

df = pd.read_excel('Prueba Modulo de facturación.xlsx')


########## Defining data #######
data = df.iloc[0:50, 0:6]

print(data.columns)

# data['fecha_modif'] = pd.to_datetime(data['fecha']).dt.strftime("%Y-%m-%d")
data['fecha_month'] = pd.to_datetime(data['fecha']).dt.month
data['fecha_day'] = pd.to_datetime(data['fecha']).dt.day
data['fecha_year'] = pd.to_datetime(data['fecha']).dt.year
# data['fecha_seconds'] = data['fecha'].apply(lambda x: pd.Timestamp(x))
# data['fecha_seconds'] = pd.DatetimeIndex(data['fecha'])

for i in range(len(data)):
    # print("seconds since epoch: ", datetime(data.loc[i,'fecha_year'], data.loc[i, 'fecha_month'], data.loc[i, 'fecha_day']).timestamp())
    data.loc[i, 'ts'] = datetime(data.loc[i,'fecha_year'], data.loc[i, 'fecha_month'], data.loc[i, 'fecha_day'], data.loc[i, 'Hora'], data.loc[i, 'Minutos']).timestamp()

print(data.head())

obj = {}
obj['p1'] = 1
obj['p2'] = 'un str'
obj['p3'] = [1,2,23]

arr = [obj]
print(obj)
print(json.dumps(arr))

sys.exit()

for i in range(0,6):
    print('[','\n', '{')

    print('kWh_T:',data.loc[i, 'kWh_T'], ',')
    print('kVArh_T:',data.loc[i, 'kVArh_T'], ',')
    print('ts:',data.loc[i, 'ts'], ',')
    
    print('}', '\n', '],', '\n')






def printConstantAttributes(f, data:pd.DataFrame, j: int):
    f.writelines(['{', '\n'])
    f.writelines(["\"type\":", str(np.random.randint(0, 4)), ',', '\n']) 
    f.writelines(["\"V_P\":", str(220*(1+0.01*np.random.randn())), ',', '\n']) 
    f.writelines(["\"A\":", str(2*(1+0.01*np.random.randn())), ',', '\n']) 
    f.writelines(["\"V_P_THD\":", str(300*(1+0.01*np.random.randn())), ',', '\n']) 
    f.writelines(["\"Hz\":", str(60*(1+0.01*np.random.randn())), ',', '\n']) 
    f.writelines(["\"FP\":", str(0.95*(1+0.01*np.random.randn())), ',', '\n']) 
    f.writelines(["\"KW\":", str(0.5*(1+0.01*np.random.randn())), ',', '\n']) 
    f.writelines(["\"KVar\":", str(0.01*np.random.randn()), ',', '\n']) 
    f.writelines(["\"KVA\":", str(0.5*(1+0.01*np.random.randn())), ',', '\n']) 
    f.writelines(["\"KWh_I\":", str(150*(1+0.01*np.random.randn())), ',', '\n']) 
    f.writelines(["\"KWh_E\":", str(300*(1+0.01*np.random.randn())), ',', '\n']) 
    f.writelines(["\"KVarh\":", str(300*(1+0.01*np.random.randn())), ',', '\n'])

    for i in range(len(data.columns)):
        if (i==4 or i==5): 
            f.writelines(['\"',data.columns[i], '\"',":", str(data.iloc[j, i]), ',' , '\n']) 
        if (i==9):
            f.writelines(['\"',data.columns[i], '\"',":", str(data.iloc[j, i]), '\n'])     

def printAttributes(data: pd.DataFrame, f):
    f.writelines(['[', '\n'])

    for j in range(0,6):
        printConstantAttributes(f,data, j) 
        if(j!=5):
            f.writelines(['},', '\n'])
        else:
            f.writelines(['}', '\n'])

    f.writelines([']', '\n'])


# with open('test.json', 'w', encoding='utf-8') as f:
#     # for i in range(len(data.index)):
#     printAttributes(data, f)



