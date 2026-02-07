import requests, os
from dotenv import load_dotenv
from pathlib import Path

basedir = Path().absolute()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


url = os.getenv("WEB_URL")
token = os.getenv("ADMIN_TOKEN")

headers = {
    "X-ADMIN-TOKEN": token
}

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
        print("5) Ver mensajes")
        print("6) Salir")
        response = input("\n#:")
        
        if response == "1":
            confirm_send = False
            while not confirm_send:
                fields = ["bio", "email", "github", "linkedin", "year", "lenguajes", "frameworks", "skills", "other"]
                confirmField = False
                json = None
                while not confirmField:
                    os.system("cls")
                    print("Seleccione un campo a editar y confirme la edicion")
                    for i, field in enumerate(fields):
                        print(f"{i+1}){field}")
                    f = int(input("#:")) - 1
                    if f < 0 or f > len(fields):
                        print("Respuesta incorrecta")
                        continue
                    
                    if f <= 6:
                        print(f"Añada todos los {fields[f]} separando con enter, para terminar escriba: listo")
                        new_field = []
                        while True:
                            r = input("#:")
                            if r == "listo":
                                if len(new_field) == 0:
                                    input("No se actualiza la data:")
                                    break
                                
                                confirm_Field = True

                            new_field.append(r)
                        json = {fields[f]:new_field}

                    else:
                        print(f"Editando {fields[f]}, presione enter al terminar")
                        new_field = input("#:")
                        ok = input("¿confirmar? si/no:")
                        if ok == "si":
                            confirmField = True
                            json = {fields[f]:new_field}
                        elif ok == "no":
                            pass
                        else:
                            print("Respuesta invalida")

                response = requests.patch(f"{url}/bio", headers=headers, json=json)
                if response.status_code == 200:
                    input(f"datos enviados: {response.json().get("message")}")
                else:
                    input(f"error al enviar: {response.status_code}:{response.text}")
                    
        elif response == "2":
            confirm_send = False
            while not confirm_send:
                fields = ["slug:","titulo:","resumen:","contenido:"]
                responses = []
                for field in fields:
                    confirmField = False
                    while not confirmField:
                        os.system("cls")
                        print("Crar post")
                        print("Llene los campos que se van a pedir confirme o rehaga el campo y envie")
                        response = input(field)
                        ok = input("¿confirmar? si/no:")
                        if ok == "si":
                            confirmField = True
                            responses.append(response)
                        elif ok == "no":
                            pass
                        else:
                            print("Respuesta invalida")
                
                data = {
                    "slug":responses[0],
                    "titulo":responses[1],
                    "resumen":responses[2],
                    "contenido":responses[3]
                }

                os.system("cls")            
                for i, r in enumerate(responses):
                    print(f"{fields[i]}: {r}")

                ok = input("\n Enviar al blog? si/no:")
                if ok == "si":
                    confirm_send = True
                    response = requests.post(f"{url}/blog/posts", headers=headers, json=data)
                    if response.status_code == 200:
                        if response.json().get("status") == "ok":

                            print("Post creado correctamente")
                            
                    else:
                        print("Error al enviar")
                    
                elif ok == "no":
                    pass
                else:
                    print("Respuesta invalida")

        elif response == "3":
            pass
        elif response == "4":
            print("Eliminar post")

            response = None
            while True:
                delete_type = input("\n Dijite si quiere rliminar por id/slug:")
                if delete_type == "id":
                    r = input("dijite el numero de ID:")
                    response = requests.delete(f"{url}/blog/posts?id={r}", headers=headers)
                    break
                elif delete_type == "slug":
                    r = input("dijite el slug:")
                    response = requests.delete(f"{url}/blog/posts?slug={r}", headers=headers)
                    break
                else:
                    print("respuesta invalida")
                
            if response.status_code == 200:
                print("Se elimino correctamente")
        
        elif response == "5":
            response = requests.get(f"{url}/bio/messages", headers=headers).json()

            for msg in response:
                print(msg)


        elif response == "6":
            key = False
    
        else:
            print("Opcion invalida")
            input("Presione enter para continuar")
            os.system("cls")
    
menu()