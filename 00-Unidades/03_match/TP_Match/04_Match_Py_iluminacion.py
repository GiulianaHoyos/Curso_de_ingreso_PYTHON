import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Giuliana
apellido:Hoyos
---
TP: Iluminación
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        valor_por_unidad = int (800)
        marca_elegida = self.combobox_marca.get()
        cantidad_elegida = int (self.combobox_cantidad.get())
        
        Precio_Total = int (valor_por_unidad * cantidad_elegida)
        
        match cantidad_elegida:
            case 6 | 7 | 8 | 9 | 10 | 11 | 12:
                Descuento = 50
            case 5:
                match marca_elegida:
                    case "ArgentinaLuz":
                        Descuento = 40
                    case _:
                        Descuento = 30
            case 4:
                match marca_elegida:
                    case "ArgentinaLuz" | "FelipeLamparas":
                        Descuento = 25
                    case _:
                        Descuento = 20
            case 3:
                match marca_elegida:
                    case "ArgentinaLuz":
                        Descuento = 15
                    case "FelipeLamparas":
                        Descuento = 10
                    case _:
                        Descuento = 5
            case 1 | 2:
                alert("UTN FRA", "Su total es ${}".format(Precio_Total))

        Precio_Final = Precio_Total - ((Descuento / 100) * Precio_Total)
        alert("UTN FRA","¡Llevando {} obtuvo un %{} de descuento! Su total es ${}".format(cantidad_elegida,Descuento,Precio_Final))

        if Precio_Final > 4000:
            Descuento_Adicional_Final = Precio_Final - ((5 / 100) * Precio_Final)
            alert("UTN FRA", "¡Obtuvo un %5 mas de descuento por haber gastado más de $4000 pesos! Su total es {}".format(Descuento_Adicional_Final))

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()