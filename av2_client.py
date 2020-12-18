import requests
import urllib.parse
import json

#1ª parte: api servidor e enderecos

consumidor_id=[]
consumidor_qtd=[]

api="http://127.0.0.1:8080/lista_clientes/"
url=api+"Brazil"
#print(url)

clientes=requests.get(url).json()
#print (json.dumps(clientes, indent=4))

for c in clientes:
    api2="http://127.0.0.1:8080/lista_pedidos/"
    url=api2+str(c["CustomerId"])
    #print(url)
    idspedidos=requests.get(url).json()
    #print (json.dumps(idspedidos, indent=4))
    
    for i in idspedidos:
        api3="http://127.0.0.1:8080/get_valor/"
        url=api3+str(i["InvoiceId"])
        #print(url)
        valorpedido=requests.get(url).json()
        #print (json.dumps(valorpedido, indent=4))
        
        if int(c["CustomerId"]) in consumidor_id:
            ind=consumidor_id.index(int(c["CustomerId"]))
            consumidor_qtd[ind]+=valorpedido[0]["Valor"]
        else:
            consumidor_id.append(int(c["CustomerId"]))
            consumidor_qtd.append(valorpedido[0]["Valor"])
        
maior=max(consumidor_qtd)
ind = consumidor_qtd.index(maior)

for c in clientes:
    if c["CustomerId"] == consumidor_id[ind]:
        endereco=c["Address"]
        cidade=c["City"]
        estado=c["State"]
        
endereco_brazil=endereco+", "+cidade+" - "+estado
#print(endereco_brazil)



consumidor_id=[]
consumidor_qtd=[]

api="http://127.0.0.1:8080/lista_clientes/"
url=api+"USA"
#print(url)

clientes=requests.get(url).json()
#print (json.dumps(clientes, indent=4))

for c in clientes:
    api2="http://127.0.0.1:8080/lista_pedidos/"
    url=api2+str(c["CustomerId"])
    #print(url)
    idspedidos=requests.get(url).json()
    #print (json.dumps(idspedidos, indent=4))
    
    for i in idspedidos:
        api3="http://127.0.0.1:8080/get_valor/"
        url=api3+str(i["InvoiceId"])
        #print(url)
        valorpedido=requests.get(url).json()
        #print (json.dumps(valorpedido, indent=4))
        
        if int(c["CustomerId"]) in consumidor_id:
            ind=consumidor_id.index(int(c["CustomerId"]))
            consumidor_qtd[ind]+=valorpedido[0]["Valor"]
        else:
            consumidor_id.append(int(c["CustomerId"]))
            consumidor_qtd.append(valorpedido[0]["Valor"])
        
maior=max(consumidor_qtd)
ind = consumidor_qtd.index(maior)

for c in clientes:
    if c["CustomerId"] == consumidor_id[ind]:
        endereco=c["Address"]
        cidade=c["City"]
        estado=c["State"]
        
endereco_usa=endereco+", "+cidade+" - "+estado
#print(endereco_usa)



consumidor_id=[]
consumidor_qtd=[]

api="http://127.0.0.1:8080/lista_clientes/"
url2=api+"Canada"
#print(url)

clientes=requests.get(url2).json()
#print (json.dumps(clientes, indent=4))

for c in clientes:
    api2="http://127.0.0.1:8080/lista_pedidos/"
    url=api2+str(c["CustomerId"])
    #print(url)
    idspedidos=requests.get(url).json()
    #print (json.dumps(idspedidos, indent=4))
    
    for i in idspedidos:
        api3="http://127.0.0.1:8080/get_valor/"
        url=api3+str(i["InvoiceId"])
        #print(url)
        valorpedido=requests.get(url).json()
        #print (json.dumps(valorpedido, indent=4))
        
        if int(c["CustomerId"]) in consumidor_id:
            ind=consumidor_id.index(int(c["CustomerId"]))
            consumidor_qtd[ind]+=valorpedido[0]["Valor"]
        else:
            consumidor_id.append(int(c["CustomerId"]))
            consumidor_qtd.append(valorpedido[0]["Valor"])
        
maior=max(consumidor_qtd)
ind = consumidor_qtd.index(maior)

for c in clientes:
    if c["CustomerId"] == consumidor_id[ind]:
        endereco=c["Address"]
        cidade=c["City"]
        estado=c["State"]
endereco_canada=endereco+", "+cidade+" - "+estado
#print(endereco_canada)



consumidor_id=[]
consumidor_qtd=[]

api="http://127.0.0.1:8080/lista_clientes/"
url=api+"France"
#print(url)

clientes=requests.get(url).json()
#print (json.dumps(clientes, indent=4))

for c in clientes:
    api2="http://127.0.0.1:8080/lista_pedidos/"
    url=api2+str(c["CustomerId"])
    #print(url)
    idspedidos=requests.get(url).json()
    #print (json.dumps(idspedidos, indent=4))
    
    for i in idspedidos:
        api3="http://127.0.0.1:8080/get_valor/"
        url=api3+str(i["InvoiceId"])
        #print(url)
        valorpedido=requests.get(url).json()
        #print (json.dumps(valorpedido, indent=4))
        
        if int(c["CustomerId"]) in consumidor_id:
            ind=consumidor_id.index(int(c["CustomerId"]))
            consumidor_qtd[ind]+=valorpedido[0]["Valor"]
        else:
            consumidor_id.append(int(c["CustomerId"]))
            consumidor_qtd.append(valorpedido[0]["Valor"])
        
maior=max(consumidor_qtd)
ind = consumidor_qtd.index(maior)

for c in clientes:
    if c["CustomerId"] == consumidor_id[ind]:
        endereco=c["Address"]
        cidade=c["City"]
        
endereco_france=endereco+", "+cidade
#print(endereco_france)
        
        

#2ª parte: api HERE e calculo de distância

api="https://geocoder.ls.hereapi.com/search/6.2/geocode.json?"
api_key="pQYS29mrAN0W8Rz5xqfK4p-59EtU1B8bu9rIONC4n8M"

endereco_origem="Av. José de Souza Campos, 44, Campinas - SP"

url=api+urllib.parse.urlencode({"apiKey":api_key, "searchtext":endereco_origem})
#print(url)
dados=requests.get(url).json()

#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"], indent=4))
#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"], indent=4))

lat_orig=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
long_orig=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]

url=api+urllib.parse.urlencode({"apiKey":api_key, "searchtext":endereco_brazil})
#print(url)
dados=requests.get(url).json()

#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"], indent=4))
#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"], indent=4))

lat_dest=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
long_dest=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]

api2="https://router.hereapi.com/v8/routes?transportMode=car&origin="+str(lat_orig)+","+str(long_orig)+"&destination="+str(lat_dest)+","+str(long_dest)+"&return=summary&apiKey="+api_key
dados=requests.get(api2).json()

#print(json.dumps(dados["routes"][0]["sections"][0]["summary"]["length"], indent=4))

dist=dados["routes"][0]["sections"][0]["summary"]["length"]
distkm_brazil=dist/1000



endereco_origem="213 Madison St, New York - NY"

url=api+urllib.parse.urlencode({"apiKey":api_key, "searchtext":endereco_origem})
#print(url)
dados=requests.get(url).json()

#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"], indent=4))
#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"], indent=4))

lat_orig=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
long_orig=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]

url=api+urllib.parse.urlencode({"apiKey":api_key, "searchtext":endereco_usa})
#print(url)
dados=requests.get(url).json()

#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"], indent=4))
#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"], indent=4))

lat_dest=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
long_dest=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]

api2="https://router.hereapi.com/v8/routes?transportMode=car&origin="+str(lat_orig)+","+str(long_orig)+"&destination="+str(lat_dest)+","+str(long_dest)+"&return=summary&apiKey="+api_key
dados=requests.get(api2).json()

#print(json.dumps(dados["routes"][0]["sections"][0]["summary"]["length"], indent=4))

dist=dados["routes"][0]["sections"][0]["summary"]["length"]
distkm_usa=dist/1000



endereco_origem="385 Ontario St, St. Catharines, ON"

url=api+urllib.parse.urlencode({"apiKey":api_key, "searchtext":endereco_origem})
#print(url)
dados=requests.get(url).json()

#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"], indent=4))
#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"], indent=4))

lat_orig=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
long_orig=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]

url=api+urllib.parse.urlencode({"apiKey":api_key, "searchtext":endereco_canada})
#print(url)
dados=requests.get(url).json()

#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"], indent=4))
#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"], indent=4))

lat_dest=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
long_dest=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]

api2="https://router.hereapi.com/v8/routes?transportMode=car&origin="+str(lat_orig)+","+str(long_orig)+"&destination="+str(lat_dest)+","+str(long_dest)+"&return=summary&apiKey="+api_key
dados=requests.get(api2).json()

#print(json.dumps(dados["routes"][0]["sections"][0]["summary"]["length"], indent=4))

dist=dados["routes"][0]["sections"][0]["summary"]["length"]
distkm_canada=dist/1000



endereco_origem="282 Avenue Daumesnil, Paris"

url=api+urllib.parse.urlencode({"apiKey":api_key, "searchtext":endereco_origem})
#print(url)
dados=requests.get(url).json()

#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"], indent=4))
#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"], indent=4))

lat_orig=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
long_orig=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]

url=api+urllib.parse.urlencode({"apiKey":api_key, "searchtext":endereco_france})
#print(url)
dados=requests.get(url).json()

#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"], indent=4))
#print(json.dumps(dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"], indent=4))

lat_dest=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
long_dest=dados["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]

api2="https://router.hereapi.com/v8/routes?transportMode=car&origin="+str(lat_orig)+","+str(long_orig)+"&destination="+str(lat_dest)+","+str(long_dest)+"&return=summary&apiKey="+api_key
dados=requests.get(api2).json()

#print(json.dumps(dados["routes"][0]["sections"][0]["summary"]["length"], indent=4))

dist=dados["routes"][0]["sections"][0]["summary"]["length"]
distkm_france=dist/1000



#3ª parte: Cálculo de envio e print

envio_brazil=distkm_brazil*0.01
envio_usa=distkm_usa*0.01
envio_canada=distkm_canada*0.01
envio_france=distkm_france*0.01

print("Os custos de envio para os clientes que mais gastaram são: ")
print("Brasil: U$$"+str("{:.2f}".format(envio_brazil)))
print("Estados Unidos: U$$"+str("{:.2f}".format(envio_usa)))
print("Canadá: U$$"+str("{:.2f}".format(envio_canada)))
print("França: U$$"+str("{:.2f}".format(envio_france)))