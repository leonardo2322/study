import pandas as pd

import time
from decimal import Decimal
from banner import bannerPaper
from funcionalidades import saveInExcel, resetasCosto,crear_grafico,insertar_venta,gestion_datos, inventario
import datetime as dt

greenColour = "\x1b[3;32m"#formato hexadecimal
yellowColour = '\033[1;33m'#formato octal
redColor= "\033[1;31m"
endColour = "\033[0m"#finaliza color
whiteColour = "\033[1;37m"
cianColour = "\033[1;36m"
blackColour = "\033[1;30m"
blueColour = "\033[1;34m"
purpleColour = "\033[1;35m"
fondoblanco = "\033[1;32;47m"
#codigo ascci para billete"4B5"
global hoja


comandos = {
'salir' : False,
'opcion1':False,
'opcion2':False,
'data':None,
'productoTotal':None,
'porcentajes':0,
'information':"",
'dataPrintable':[]
}





" empieza a correr el sistema principal ********************************"

while comandos['salir'] != True:
    print()
    bannerPaper()
    print(f" {yellowColour} OPCIONES DE USO {endColour} \n\n {blackColour} modo de uso debe 1ero costear un producto para que el sistema cargue la informacion \n luego podra ingresar al area de Ventas e inventario si es su primer inicio \n recuerde que la informacion esta siendo almacenada en un excel {endColour} \n\n {greenColour} [1]Costear Producto {endColour} \t {whiteColour} [2]Ventas  {endColour} \t { redColor} [3]Inventario {endColour} \n")
    
    manage = input(f" {blackColour} elije una de las opciones mostradas en pantalla marca 'q' o 'exit' para salir {endColour}")
    comandos['opcion2'] = False
    if manage == 'q' or manage == 'exit':
        print(f'{redColor} saliendo del sistema {endColour}')
        time.sleep(1)
        print(f'{redColor} por favor espere... {endColour}')
        
        time.sleep(2)
        comandos['salir'] = True
    elif manage == '1':
        while comandos['opcion1'] != True: 
            comando = input(f" {whiteColour} deseas continuar con la opcion de costos marque 's' o 'si' o 'n' para salir : {endColour} \n")

            if comando == 'si' or comando == 's':
                opciones = input(f'{whiteColour} [0] registrar los datos en excel \t [1] costo x cantidad y ganancia \t [2] costo producto {endColour} \n {redColor} [3] mostrar datos  {endColour}')
              
                if opciones == '2':
                    hoja = input(f' {whiteColour} introduce el nombre de la hoja que quieres analizar: {endColour}')
                    try:                
                        bd = pd.read_excel(".\\ResetasPrueba.xlsx", sheet_name=hoja, header=None,engine='openpyxl')
                        print()
                        unidadesxreceta = input(f' {blackColour} cuantas unidades arroja la reseta: {endColour}')
                        print()
                        unidades = input(f'{blackColour} cuantas unidades para el paquete: {endColour}')
                        gramaje = input(f'{blackColour} gramaje de la unidad: {endColour}')
                        comandos['data'], comandos['productoTotal'] = resetasCosto(bd,unidadesxreceta,unidades,0.014, 0.035, gramaje)
                        time.sleep(1)
                        print(f"{fondoblanco}el total de unidades variable que arroja la receta es: {round(comandos['productoTotal'],3)} \U0001f911 {endColour}")
                        print(f" {fondoblanco} el Total del producto es: \U0001f4b5 {round(comandos['data'],3)} {endColour}")
                        time.sleep(2)
                    except Exception as e:
                        print(f"\t {redColor}|a ocurrido un error por favor verifica que has introducido el nombre correcto de la hoja de excel '{e}' {endColour} \n ")

                elif opciones == '1':
                    if comandos['data'] == None:
                        print(f"{redColor}aun no has elejido la opcion [2] para proseguir con el analisis{endColour}")
                        continue
                    else:
                        try:
                            cantidad = Decimal(input(f"{whiteColour} introduce la cantidad que deseas sacar y te mostrare el costo: {endColour} "))
                            totalgasto = Decimal(comandos['data']) * cantidad
                            porcentaje = Decimal(input(f"{blackColour}introduce el porcentaje de ganancia para el producto : {endColour}"))
                            treintaycincoporciento = Decimal(comandos['data']) * porcentaje /100
                            comandos['porcentajes'] = porcentaje
                            totalfinal = treintaycincoporciento * cantidad
                            print(f"{fondoblanco} el total de gasto seria de: \U0001f4b5 {round(totalgasto,3)} {endColour} \n")
                            print(f" {fondoblanco} la ganancia x: {round(cantidad,0)} paquetes\U0001f4b5,  seria de: {round(totalfinal,3)}\U0001f4b5 y el total generado serian{round(totalgasto+totalfinal,2)}\U0001f4b5 , valor por producto con el porcentaje% de ganancia:{round(treintaycincoporciento,2)} el total precio seria de: {round(Decimal(comandos['data']) + treintaycincoporciento,2)}\U0001f4b5  {endColour} \n")

                            comandos['information'] = {
                                'fecha': dt.date.today(),
                                'Producto': hoja,
                                'porcentaje_ganancia':treintaycincoporciento,
                                'totalGasto':round(totalgasto,3),
                                'cantidad':cantidad,
                                'ganancia_generada_t':round(totalfinal,3),
                                'costoVentaProductofinal':round(Decimal(comandos['data']) + treintaycincoporciento,2),
                                'cuentaTotal':round(totalgasto+totalfinal,2)
                                
                            }
                        except Exception as e:
                            print(f"{redColor} has introducido un texto o nada{endColour}")   
                elif opciones == '0':
                        if len(comandos['information']) > 0 and comandos['information'] != None:
                            try:
                                nameHoja = input(f"{whiteColour}introduce el nombre de la hoja de excel donde guardar los datos: {endColour}")
                                archivo = ".\\ResetasPrueba.xlsx"
                                comandos['dataPrintable'] = {'archivoPath': archivo, 'sheetName': nameHoja}
                                headin = input(f"{whiteColour}Quieres un encabezado marca 's' en caso contrario presiona 'Enter': {endColour}").strip()

                                saveInExcel(archivo,comandos['information'],nameHoja,headin)
                            except Exception as e:
                                print(f"{redColor}ocurrio un error {e} {endColour}")
                        else:
                            print(f"{redColor}ha ocurrido un error al guardar{endColour}")
                elif opciones == '3':
                    try:
                        df = pd.read_excel(comandos['dataPrintable']['archivoPath'],sheet_name=comandos['dataPrintable']['sheetName'], header=None,engine='openpyxl')  
                        dataprintable = pd.DataFrame(df)
                        dfCleaned = dataprintable.dropna(how='all')
                        print(f"\n{yellowColour} tabla de registros:\n\n {endColour}{whiteColour}{dfCleaned}{endColour}\n")
                    except Exception as e:
                        print(f"{redColor} {e} {endColour}")
            else:
                comandos['opcion1'] = True
                print(f"{yellowColour} opcion no encontrada en el menu {endColour}")
        comandos['opcion1'] = False

    elif manage == '2':
        ################### Ventas ##################### 
        while comandos['opcion2'] != True:
            opcion = input(f"\n\n{purpleColour} [0]crear un grafico {endColour} {yellowColour}[1] Total ventas {endColour} \n\n  {whiteColour}\n[2] crear venta {endColour}\n {blackColour} presione salir 's' o 'q'{endColour}\n\n")
            try:
                if opcion == '0':
                    crear_grafico() 
                elif opcion == '1':
                    gestion_datos()
                elif opcion == '2':
                    insertar_venta()
                
                else:
                    comandos['opcion2'] = True
            except Exception as e:
                print(f"{redColor} {type(e).__name__} {e} {endColour}")
    elif manage == '3':
            try:
                inventario() 
            except Exception as e :
                print(f"{redColor}{e}{endColour}")
            

