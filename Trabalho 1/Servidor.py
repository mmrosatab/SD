from xmlrpc.server import SimpleXMLRPCServer

#Lado Servidor

def add(self,a,b):
	return a+b

def main():
    print("Sou a servidor! Olá")
    server = SimpleXMLRPCServer(("localhost", 8080))
    server.register_function(add)
    server.serve_forever()
    print("Aperte Ctrl+C para encerrar o programa")

if __name__ == "__main__":
    main()
    

