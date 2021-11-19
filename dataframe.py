from typing import NewType
import pandas as pd
import json

path= 'input/Sell_In.xlsx'








def getDataframe():
    df=pd.read_excel(path, sheet_name='Standard_WB',skiprows=6, header=None)
    P1_NART=df[1]
    PRODUCT_NAME=df[2]
    CALENDAR_DAY=df[3]
    N_S=df[4].fillna(0)
    NET_SALES=[]
    QTY=df[5].fillna(0)
    QUANTITY=[]
    DATES=[]
    for date in CALENDAR_DAY:
        t=str(date)
        año=t[6:]
        mes=t[3:5]
        dia=t[0:2]
        new_date= año+'-'+mes+'-'+dia
        # print(new_date)
        DATES.append(new_date)
        
    for ns in N_S:
        NET_SALES.append(str(ns))
    for q in QTY:
        QUANTITY.append(str(q))

    my_dict={
        "nart": P1_NART,
        "nartdesc": PRODUCT_NAME,
        "clasificacion":'REALES',
        "calendar_day": DATES,
        "units": QUANTITY,
        "netsales":NET_SALES
    }
    data= pd.DataFrame(data=my_dict)
    json_data=data.to_json(orient='records')
    x=json.loads(json_data)
    info={}
    info['objects']=[]
    for y in x:
        info['objects'].append(y)
    with open('data/variables.json', 'w') as outfile:
        json.dump(info, outfile)
    print(json_data)
getDataframe()
    
