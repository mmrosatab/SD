


from xmlrpc.server import SimpleXMLRPCServer
import psycopg2

class Servidor():
 
    def __init__(self):
        
        self.con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='20071992')
        cur = self.con.cursor()
        
        sql = "select exists (select 1 from information_schema.tables where table_name = 'periodo');"
        cur.execute(sql)
        retorno = cur.fetchone()
        print(retorno)

        if retorno[0] == False:

        	sql = "CREATE TABLE Periodo ( matricula int NOT NULL, disciplina varchar(4) NOT NULL, nota float NOT NULL, primary key(matricula, disciplina));"
        	cur.execute(sql)

        self.con.commit()
        
        self.server = SimpleXMLRPCServer(("localhost", 8080))
        self.server.register_function(self.cadastrarNota)
        self.server.register_function(self.consultarNota)
        self.server.register_function(self.listarNotas)
        self.server.register_function(self.consultarCR)
        self.server.register_function(self.terminar)
        
        self.quit = False
        
        while not self.quit:
        	    self.server.handle_request()
        

    def cadastrarNota(self,mat,codDisc,nota):
        
        if len(codDisc) > 4 or len(codDisc) == 0:
        	return False

        cur   = self.con.cursor()
        
        sql   = 'SELECT nota FROM Periodo WHERE matricula = ' + str(mat) + ' AND disciplina = ' + "'" + codDisc + "'"
        cur.execute(sql)
        
        if cur.rowcount > 0:
            sql = 'UPDATE Periodo SET nota = '+ str(nota) + ' WHERE matricula = ' + str(mat) + ' AND disciplina = ' + "'" + codDisc + "'"
        
        else:
            sql = 'INSERT INTO Periodo VALUES ('+ str(mat) + ",'" + codDisc + "'," + str(nota) + ');'
            
        cur.execute(sql)
        self.con.commit()
        return "Nota cadastrada."
    
    def consultarNota(self,matricula, codDisc):

    	if len(codDisc) > 4 or len(codDisc) == 0:
    		return False

    	cur      = self.con.cursor()
    	sql      = 'SELECT disciplina, nota FROM Periodo WHERE matricula = '+ str(matricula) + ' AND disciplina = ' + "'" + codDisc + "';"
    	cur.execute(sql)
    	linha    = cur.fetchone()

    	if linha is None:   
    		return False
    	else:
    		return linha[0] + ' ' + str(linha[1])
            
        
    
    def listarNotas(self,matricula):
        cur      = self.con.cursor()
        sql      = 'SELECT disciplina, nota FROM Periodo WHERE matricula = '+ str(matricula);
        cur.execute(sql)
        linhas   = cur.fetchall()
        result   = ''
        if len(linhas) == 0:           
            return False
        
        else:
            
            for linha in linhas:
                result = result + linha[0] + ' ' + str(linha[1]) + '\n'
                
            return result
            
    
    def consultarCR(self,matricula):
        cur      = self.con.cursor()
        sql      = 'SELECT nota FROM Periodo WHERE matricula = '+ str(matricula)
        cur.execute(sql)
        notas    = cur.fetchall()
        if len(notas) == 0:            
            return False
        else:
            
            cr = 0
            
            for nota in notas:
                cr = cr + float(nota[0]) 
            
            return round(cr/cur.rowcount,2)

    def terminar(self):        
        self.quit = True
        return True
    
    

def main():
    
    print("Inicializando servidor:")
    Servidor()
    print("Servidor finalizado!")
    
    
    
    
    
    
if __name__ == "__main__":
    main()