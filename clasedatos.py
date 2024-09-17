class Informacion:

    def mi_lista(self):
        lista_Nomperros=["boby","Dollar","fany"]
        for x in lista_Nomperros:
            print(x)

    def mi_tupla(self):
        tupla_Nomgatos=("Pelusa","elmen","solovino")
        for x in tupla_Nomgatos:
            print(x)

    def mi_conjunto(self):
        conj_Razaperros={"Pitbull","Doberman","Chihuahua"}
        for x in conj_Razaperros:
            print(x)

    def mi_diccionario(self):
        dicc_Tamañosperros={"Perro 1":"Mediano","Perro 2":"Grande","Perro 3":"Chico"}
        for x,key in dicc_Tamañosperros.items():
            print(x,"-",key)

# creando el objeto

datos=Informacion()
print("-----Listado de nombres de perros-----")
datos.mi_lista()
print("-----Tupla de nombres de gatos-----")
datos.mi_tupla()
print("-----Conjunto de razas de perros-----")
datos.mi_conjunto()
print("-----Diccionario de tamaños de perros-----")
datos.mi_diccionario()