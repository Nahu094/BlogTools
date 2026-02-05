import requests, os

def menu():
    key = True
    response = None
    while key:
        print("!-------- Blog Tools --------¡")
        print("\n")
        print("1) Editar Biografia")
        print("2) Crear post")
        print("3) Editar post")
        print("4) Eliminar post")
        print("5) Salir")
        response = input("\n#:")
        
        if response == "1":
            pass
        elif response == "2":
            pass
        elif response == "3":
            pass
        elif response == "4":
            pass
        elif response == "5":
            key = False
    
        else:
            print("Opcion invalida")
            input("Presione enter para continuar")
            os.system("cls")
    
menu()