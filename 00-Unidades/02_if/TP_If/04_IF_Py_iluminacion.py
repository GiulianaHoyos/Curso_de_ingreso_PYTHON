import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Giuliana
apellido:Hoyos
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.
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
        valor_unidad = float (800)
        marca_elegida = self.combobox_marca.get()
        cantidad_elegida = int (self.combobox_cantidad.get())
        
        Precio_total = valor_unidad * cantidad_elegida
        
        if cantidad_elegida >= 6:
            Descuento = 50
        elif marca_elegida == "ArgentinaLuz" and cantidad_elegida == 5:
                Descuento = 40
        elif not marca_elegida == "ArgentinaLuz" and cantidad_elegida == 5:
                Descuento = 30
        elif (marca_elegida == "ArgentinaLuz" or marca_elegida == "FelipeLamparas") and cantidad_elegida == 4:
                Descuento = 25
        elif (not marca_elegida == "ArgentinaLuz" or not marca_elegida == "FelipeLamparas") and cantidad_elegida == 4:
                Descuento = 20
        elif marca_elegida == "ArgentinaLuz" and cantidad_elegida == 3:
                Descuento = 15
        elif marca_elegida == "FelipeLamparas" and cantidad_elegida == 3:
                Descuento = 10
        elif (not marca_elegida == "ArgentinaLuz" and not marca_elegida == "FelipeLamparas") and cantidad_elegida == 3:
            Descuento = 5
        else:
            alert(title="UTN FRA", message= "Su total es {}".format(Precio_total))
        
        
        Valor_con_Descuento = (Precio_total * Descuento) / 100
        Valor_Final = Precio_total - Valor_con_Descuento
        alert ("UTN FRA", "¡Comprando {} lamparitas obtuvo un {}% de descuento! Su total es ${}".format(cantidad_elegida,Descuento,Valor_Final))
        
        if Valor_Final > 4000:
            Descuento = (Valor_Final * 5) / 100
            Valor_con_descuento_adicional = Valor_Final - Descuento
        alert(title="UTN FRA", message="¡Obtuvo un %5 mas de descuento por haber gastado más de $4000 pesos! Su total es {}".format(Valor_con_descuento_adicional))


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()