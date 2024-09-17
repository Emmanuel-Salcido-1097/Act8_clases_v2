print("Clases version 2 el constructor")

class Perro:
    # Funcion constructor
    def __init__(self,color,edad):
        self.color = color
        self.edad = edad
    # Funciones creadas por el usuario
    def muerde(self):
        print("Chale el perro me mordio")
    def chatperro(self,mensaje):
        print(f"Chat perro: {mensaje}")
    def chatperra(self,mensajepe):
        print(f"Chat perra: {mensajepe}")
    def datos(self):
        print(f"Color {self.color} eddad {self.edad}")
# Crear el objeto
chihuas=Perro("Negro",2)
# Llamadas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola boby")
chihuas.chatperro("Quieres ser mi gugguu ?")
chihuas.chatperra("grrru.......")