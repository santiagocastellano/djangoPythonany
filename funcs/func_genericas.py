from suds.client import Client

#def serializarObj(obj,dict):
   # print(obj[0].Delimitacion)
    #for ele in obj:
       # print(getattr(ele, 'Delimitacion'))
        #print('sksksks')
        #for i in ele.values():
         #   print('sksksksksks')
        #for i in dict.values():
         #   print(getattr(ele,'Delimitacion'))
def getSOAPClient(cliente):
    client = Client(cliente)
    return client
