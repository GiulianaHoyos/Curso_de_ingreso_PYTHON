import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Giuliana
apellido:Hoyos
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        bandera = True
        
        acumulador_negativo = 0
        acumulador_positivo = 0
        contador_positivo = 0
        contador_negativo = 0
        contador_cero = 0
        
        while True:
            numero = prompt("UTN FRA", "Ingrese su numero")
            
            if numero == None:
                break
            
            numero = int(numero)
            
            if numero < 0:
                acumulador_negativo = acumulador_negativo + numero
                resultado = acumulador_negativo
                contador_positivo = contador_positivo + 1
            elif numero > 0:
                acumulador_positivo = acumulador_positivo + numero
                resultado = acumulador_positivo
                contador_negativo = contador_negativo + 1
            else:
                contador_cero = contador_cero + 1
                
        diferencia_numeros = contador_positivo - contador_negativo
        
        alert("UTN FRA","Suma de negativos {}. Suma de positivos {}".format(resultado))
    
    
    #C. Cantidad de números positivos ingresados
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
