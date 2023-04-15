import time
import random
import requests
import json

datos = { 'idcan':42, 'idcat':5 }
headers = {'Content-Type': 'application/json'}
cont=1

while True:
    time.sleep(random.uniform(107, 208))  
    peticion = requests.post("https://www.vanguardia.com/empresasgeneradoras/reconocimientos/votar", headers=headers, data=json.dumps(datos))
    print(f"voto, {cont}")
    print(peticion.text)
    if(cont == 200):
        break
