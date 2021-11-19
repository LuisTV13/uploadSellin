import requests
import json
from dataframe import getDataframe



url ='https://graph.sop.strategio.cloud/v1beta1/relay'

headers = {"x-hasura-admin-secret"  : "x5cHTWnDb7N2vh3eJZYzamgsUXBVkw",
           "content-type":"application/json"}

def run_query(query,variables):
    request = requests.post(url, json={'query': query ,"variables":variables}, headers=headers,)
    if request.status_code == 200:
        print("Ingresado Correctamente")
        return request.json()
        
    else :
        raise print(Exception('Error Mutacion'))
    
query = """
  mutation Sellin($objects: [Sell_in_insert_input!]!) {
  insert_Sell_in(objects: $objects, on_conflict: {constraint:Sell_in_pkey , update_columns:nart }) {
    returning {
      nart
    }
  }
}

"""


getDataframe()

d = open('data/variables.json')
variables = json.load(d)

#print(variables)

run_query(query,variables)