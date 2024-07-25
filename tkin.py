import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para cargar datos desde un archivo CSV
def cargar_datos():
    try:
        # Cargar datos desde el archivo CSV (o Excel si es necesario)
        # Cambia el nombre del archivo y el tipo según el formato real de tu archivo
        df = pd.read_excel(".\\ResetasPrueba.xlsx")
        
        # Actualizar la tabla en la interfaz con los datos cargados
        actualizar_tabla(df)
        
        messagebox.showinfo("Éxito", "Datos cargados correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar los datos: {str(e)}")

# Función para actualizar la tabla en la interfaz
def actualizar_tabla(df):
    # Limpiar tabla existente si hay datos previos
    limpiar_tabla()
    
    # Mostrar datos en la tabla
    for index, row in df.iterrows():
        treeview.insert('', 'end', values=list(row))

# Función para limpiar la tabla
def limpiar_tabla():
    for item in treeview.get_children():
        treeview.delete(item)

# Función para realizar análisis por producto y por mes
def analizar_datos():
    try:
        df = pd.read_excel(".\\ResetasPrueba.xlsx")  # Cargar datos
        
        # Ejemplo de análisis: agrupar por producto y sumar las cantidades vendidas
        analisis_por_producto = df.groupby('Producto')['Cantidad'].sum().sort_values(ascending=False)
        
        # Mostrar resultados en una ventana emergente
        messagebox.showinfo("Análisis por Producto", f"Producto más vendido:\n{analisis_por_producto.head(1)}")
        
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo analizar los datos: {str(e)}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Análisis de Ventas")

# Botones y controles
btn_cargar = ttk.Button(root, text="Cargar Datos", command=cargar_datos)
btn_cargar.pack(pady=10)

btn_analizar = ttk.Button(root, text="Análisis por Producto", command=analizar_datos)
btn_analizar.pack(pady=10)

# Tabla para mostrar los datos
treeview = ttk.Treeview(root, columns=['Fecha', 'Producto', 'Cantidad', 'Precio', 'Modo de Pago', 'Negocio o Consumidor'])
treeview.heading('#0', text='Índice')
treeview.heading('#1', text='Fecha')
treeview.heading('#2', text='Producto')
treeview.heading('#3', text='Cantidad')
treeview.heading('#4', text='Precio')
treeview.heading('#5', text='Modo de Pago')
treeview.heading('#6', text='Negocio o Consumidor')
treeview.pack()

# Ejecutar la aplicación
root.mainloop()
