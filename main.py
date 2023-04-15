import time
import random
import requests
import json

#captcha
#_grecaptcha:"09AMqPRJxWlovGLU4ds3xKgQQtInnc6ZZVH8raJ3f8nLGycBp-OFuPexjDmzkze272Ih2ygMSoe37df7ahYnrL-AUwPNnPxS42us0"


datos = { 'idcan':42, 'idcat':5 }
headers = {'Content-Type': 'application/json'}
cont=1

while True:
    time.sleep(random.uniform(107, 208))  
    peticion = requests.post("https://www.vanguardia.com/empresasgeneradoras/reconocimientos/votar", headers=headers, data=json.dumps(datos))
    cont=cont+1
    print(f"voto, {cont}")
    print(peticion.text)
    if(cont == 120):
        break
