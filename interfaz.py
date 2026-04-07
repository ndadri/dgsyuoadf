import tkinter as tk
from calculadora import sumar, restar, multiplicar, dividir

# FUNCIONES
expresion = ""
resultado_mostrado = False

# Funciones para manejar eventos de botones
def click(valor):
    global expresion, resultado_mostrado

    if resultado_mostrado:
        # Si acabamos de mostrar un resultado y presionan un número
        expresion = ""           # limpiar pantalla
        resultado_mostrado = False

    expresion += str(valor)
    pantalla_var.set(expresion)

# Función para limpiar la pantalla y la expresión
def limpiar():
    global expresion
    expresion = ""
    pantalla_var.set("0")

# Función para borrar el último dígito ingresado
def borrar_un_digito():
    global expresion
    if expresion:  # si no está vacía
        expresion = expresion[:-1]  # elimina el último carácter
        pantalla_var.set(expresion if expresion else "0")  # si queda vacío, muestra 0

# Función para calcular el resultado de la expresión
def calcular():
    global expresion, resultado_mostrado
    try:
        # Separar números y operador (simple)
        for op in ["+", "-", "*", "/"]:
            if op in expresion:
                # Divide en 2 partes lo que se almacena en la variable expresion
                a, b = expresion.split(op)
                a, b = float(a), float(b)

                if op == "+":
                    resultado = sumar(a, b)
                elif op == "-":
                    resultado = restar(a, b)
                elif op == "*":
                    resultado = multiplicar(a, b)
                elif op == "/":
                    resultado = dividir(a, b)
                # Muestra el resultado en pantalla y actualiza la expresión para permitir cálculos encadenados
                pantalla_var.set(resultado)
                expresion = str(resultado)
                resultado_mostrado = True 
                return
    # Si la expresión no es válida o hay un error, muestra "Error"
    except:
        pantalla_var.set("Error")
        expresion = ""

# Intwerfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x450")
ventana.resizable(False, False)

pantalla_var = tk.StringVar(value="0")

pantalla = tk.Entry(
    ventana,
    textvariable=pantalla_var,
    font=("Segoe UI", 24),
    bd=10,
    relief="flat",
    justify="right",
    state="readonly"

)
pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=10)

# Configurar grid
for i in range(6):
    ventana.rowconfigure(i, weight=1)
for j in range(4):
    ventana.columnconfigure(j, weight=1)

# Botones estilo calculadora
botones = [
    ("C", 1, 0), ("⌫", 1, 1), ("/", 1, 2), ("*", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),
    ("0", 5, 0), (".", 5, 1),
]

def crear_boton(texto, fila, col):
    if texto == "=":
        cmd = calcular
        color = "#0078D7"
        fg = "white"
    elif texto == "C":
        cmd = limpiar
        color = "#d9d9d9"
        fg = "black"
    elif texto == "⌫":
        cmd = borrar_un_digito
        color = "#f0f0f0"
        fg = "black"
    else:
        cmd = lambda t=texto: click(t)
        color = "#f0f0f0"
        fg = "black"

    tk.Button(
        ventana,
        text=texto,
        command=cmd,
        font=("Segoe UI", 14),
        bd=1,
        bg=color,
        fg=fg
    ).grid(row=fila, column=col, sticky="nsew", padx=2, pady=2)
    
for (t, f, c) in botones:
    crear_boton(t, f, c)

ventana.mainloop()