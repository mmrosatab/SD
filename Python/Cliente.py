
import xmlrpc.client

def main():
    
    print("Conectando ao servidor...")
   
    cliente = xmlrpc.client.ServerProxy("http://localhost:8080/")

    consultando = True
    while consultando:
        print("Digite o numero da operacao que deseja realizar:")
        print("1. Cadastrar Nota")
        print("2. Consulta nota de um aluno em uma disciplina especifica")
        print("3. Consultar todas as notas de um aluno")
        print("4. Calcular CR de um aluno")
        print("5. Sair")
        opcao = input()       
   
        if opcao == "1":            
            matricula  = input("Matricula do aluno:")
            disciplina = input("Digite o codigo da disciplina:")
            
            while len(disciplina) > 4:
                print("\nCodigo de disciplina incorreto. Digite novamente.\n")
                disciplina = input("Digite o codigo da disciplina:")
                
            nota       = input("Digite a nota a ser cadastrada:")                       
            
            print(cliente.cadastrarNota(int(matricula),disciplina,float(nota)))
            
            decisao = input("Caso  deseje fazer outra operacao digite: Y.\n")            
            if decisao != "Y":
                consultando = False
                
        elif opcao == "2":
            matricula  = input("Matricula do aluno:")
            disciplina = input("Código da disciplina")
            
            while len(disciplina) > 4:
                print("\nCodigo de disciplina incorreto. Digite novamente.\n")
                disciplina = input("Digite o codigo da disciplina:")
            
            retorno = cliente.consultarNota(int(matricula),disciplina)
            if retorno == False:
                print("ERRO: A nota requisitada nao existe no sistema.")               
            else:
                print(retorno)
            
            decisao = input("Caso  deseje fazer outra operacao digite: Y.\n")                
            if decisao != "Y":
                consultando = False    
            
        
        elif opcao == "3":
            matricula = input("Matricula do aluno:")
            
            retorno = cliente.listarNotas(int(matricula))
            
            if retorno == False:
                print("ERRO: A matricula indicada nao existe ou nao possui notas cadastradas!")            
            else:
                print(retorno)
            
            decisao = input("Caso  deseje fazer outra operacao digite: Y.\n")                
            if decisao != "Y":
                consultando = False
            
        elif opcao == "4":
            matricula = input("Matrica do aluno:")
            
            retorno = cliente.consultarCR(int(matricula))
            
            if retorno == False:
                print("ERRO: A matricula indicada nao existe ou nao possui notas cadastradas!")
            else:
                print(retorno)
            
            decisao = input("Caso  deseje fazer outra operacao digite: Y.\n")                
            if decisao != "Y":
                consultando = False
                
        elif opcao == "5":
            consultando = False
        else:
            print("Opcao invalida. Tente novamente.")
        
            
    
    cliente.terminar()
                                    
    
    
    
if __name__ == "__main__":
    main()

