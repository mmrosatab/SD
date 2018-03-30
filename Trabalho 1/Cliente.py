
# coding: utf-8

# In[2]:


import xmlrpc.client


# In[3]:



def main():
    print("Eu sou o Cliente")
    cliente = xmlrpc.client.ServerProxy("http://localhost:8080/")
              
    
    print(cliente.add(10,10)
    #print(cliente.cadastrarNota)
    
if __name__ == "__main__":
    main()
