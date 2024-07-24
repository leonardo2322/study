
# redColor= "\033[1;31m"
# endColour = "\033[0m"
# fondoblanco = "\033[1;32;47m"
# def code_morse(word:str):
#     codigo_morse = {
#         'A': '.-', 
#         'B': '-...', 
#         'C': '-.-.', 
#         'D': '-..', 
#         'E': '.', 
#         'F': '..-.', 
#         'G': '--.', 
#         'H': '....', 
#         'I': '..', 
#         'J': '.---', 
#         'K': '-.-', 
#         'L': '.-..', 
#         'M': '--', 
#         'N': '-.', 
#         'O': '---', 
#         'P': '.--.', 
#         'Q': '--.-', 
#         'R': '.-.', 
#         'S': '...', 
#         'T': '-', 
#         'U': '..-', 
#         'V': '...-', 
#         'W': '.--', 
#         'X': '-..-', 
#         'Y': '-.--', 
#         'Z': '--..',
#         '0': '-----',
#         '1': '.----',
#         '2': '..---',
#         '3': '...--',
#         '4': '....-',
#         '5': '.....',
#         '6': '-....',
#         '7': '--...',
#         '8': '---..',
#         '9': '----.',
#         '.': '.-.-.-',
#         ',': '--..--',
#         '?': '..--..',
#         "'": '.----.',
#         '!': '-.-.--',
#         '/': '-..-.',
#         '(': '-.--.',
#         ')': '-.--.-',
#         '&': '.-...',
#         ':': '---...',
#         ';': '-.-.-.',
#         '=': '-...-',
#         '+': '.-.-.',
#         '-': '-....-',
#         '_': '..--.-',
#         '"': '.-..-.',
#         '$': '...-..-',
#         '@': '.--.-.',
#         ' ': '.......'
# }

#     words_upper = word.upper()
#     text_morse = ""
#     for l in words_upper:
#         if l in codigo_morse:
#             text_morse += codigo_morse[l]
#     return text_morse

# word = code_morse("elina te amo")
# print(f"codigo_morse{redColor} {word} {endColour} ")
# def binario(n:str)->int:
#     decimal = 0
#     longitud = len(n)
#     for i in n[-1::-1]:
#         if i != '0':
#             decimal = decimal + (2 **(len(n) - longitud))
#         longitud = longitud - 1
#     return decimal
# bins =binario("10101010")
# print(bins)

# def binario(n:str):
#     decimal = 0
#     longitud = len(n)
#     for i in reversed(n):
#         if i == '1':
#             decimal = decimal + (2** (len(n) - longitud))
#         longitud = longitud - 1
#     return decimal

# bins = binario("10101010")
# def binario_a_decimal(n:str):
#     decimal = 0
#     longitud = len(n)
#     for i in range(longitud):
#         bit = int(n[longitud -1 -i])
#         decimal += bit * (2**i)

#     return decimal 
# decimal = binario_a_decimal("101010")
# print(decimal)

# def decimal_a_binario(n:int):
#     if n == 0:
#         return '0'
    
#     binario = ''
#     while n > 0:
#         residuo = n % 2 
#         binario = str(residuo) + binario
        
#         n = n // 2
#     return binario
# n = 37
# binario = decimal_a_binario(n)
# print(f" el numero {n} en binario es:{binario}")
# -----------------invirtiendo los textos en una funcion esta con la explicacion de chatgpt

# def inverted_text(text:str)-> str:

#     return text[-1::-1].capitalize()

#----------- invirtiendo los textos en una funcion 1er intento con los conocimientos base
# print(inverted_text("leonardo fabio"))
# def inverted_text(text:str)-> str:
#     newText = ""
#     for i, l in enumerate(text):
#         if i == 0:
#             continue 
#         newText += text[-i]
#     newText += text[0].capitalize()
#     return newText


#--------------- practica aspect ratio de una imagen 
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

#-------------- poligonos calculo para saber el area 1er intento 
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

# --------------------n primos 
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