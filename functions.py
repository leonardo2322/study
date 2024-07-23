
# def inverted_text(text:str)-> str:

#     return text[-1::-1].capitalize()

# print(inverted_text("leonardo fabio"))
# def inverted_text(text:str)-> str:
#     newText = ""
#     for i, l in enumerate(text):
#         if i == 0:
#             continue 
#         newText += text[-i]
#     newText += text[0].capitalize()
#     return newText

# import urllib.request
# import json
# from PIL import Image

# url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/76.png"

# def aspect_ratio(urls,image):
        
#     try:
#         with urllib.request.urlopen(urls) as response:
#             data = response.read()
#             with open("nuevo.png","wb") as f:
#                   f.write(data) 
        
#         imagen = Image.open(image)
#         # print("Metadatos de la imagen:")
#         # print(f"Formato: {imagen.format}")
#         # print(f"Modo: {imagen.mode}")
#         # print(f"Tamaño: {imagen.size}")
#         # print(f"Info: {imagen.info}")
#         w, h = imagen.size
#         print(f"width{w}, heigth{h}")
#         asp_ratio = w/h
#         ratio = str(asp_ratio).replace(".", ":")
#         print(f"el aspect_ratio de la imagen es: {ratio}")
#     except urllib.error.URLError as e:
#             print(f"Error de URL: {e}")
#             return None
#     except json.JSONDecodeError as e:
#             print(f"Error al decodificar JSON: {e}")
#             return None
    
# aspect_ratio(url,"nuevo.png")
# def poligonos(p:dict):
    
#     if p['tipo'] == "triangulo":
#         formula =  (p["triangulo"]['base'] * p["triangulo"]['altura']) / 2
#         return print(f"las dimensiones del poligo {p['tipo']} son: {formula}")
    
#     elif p['tipo'] == "cuadrado":
#         formula = p["cuadrado"]["lado"] * p["triangulo"]["lado"]
#         return print(f"las dimensiones del poligo {p['tipo']}  son: {formula}")
    
#     elif p['tipo'] == "rectángulo":
#         formula = p["rectángulo"]["base"] * p["rectángulo"]["altura"]
#         return f"las dimensiones del poligo {p['tipo']}  son: {formula}"

#     else:
#         print(f"No se reconoce el tipo de polígono: {p["tipo"]}")
#         return None


# p = {"tipo":"triangulo","triangulo":{
#     "base":5,
#     "altura":3,
# }}
# poligonos(p)
# def primos(n1:int):
#     uno = 1
#     result = n1 <= uno
#     if result:
#         return False
#     if n1 == 2:
#         return True
#     if n1 % 2 == 0 and n1 != 2:
#         return False
#     for i in range(3,n1,2):
#         if n1 % i == 0:
#             return False
#     return True
        
# def printable():
#     for i in range(1,101):
#         result = primos(i)
#         if result:
#             print(result)
#         else:
#             print(i)
#    return None
        

# printable()