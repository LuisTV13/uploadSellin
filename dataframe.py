from typing import NewType
import pandas as pd
import json

path= 'input/Sell_In.xlsx'
def getDataframe():
    df=pd.read_excel(path, sheet_name='Standard_WB',skiprows=6, header=None)
    P1_NART=df[1]
    PRODUCT_NAME=df[2]
    CALENDAR_DAY=df[3]
    N_S=df[4]
    NET_SALES=[]
    QTY=df[5]
    QUANTITY=[]
    DATES=[]
    for date in CALENDAR_DAY:
        año=date[6:]
        mes=date[3:5]
        dia=date[0:2]
        new_date= año+'-'+mes+'-'+dia
        DATES.append(new_date)
    for ns in N_S:
        NET_SALES.append(str(ns))
    for q in QTY:
        QUANTITY.append(str(q))

    my_dict={
        "nart": P1_NART,
        "nartdesc": PRODUCT_NAME,
        "clasificacion":'baseline',
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
    
