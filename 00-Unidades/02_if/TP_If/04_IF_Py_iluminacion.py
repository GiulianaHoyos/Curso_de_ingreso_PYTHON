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
            #descuento 50%
            Descuento = Precio_total * 0.50
            #muestro total
            Valor_con_Descuento = Precio_total - Descuento
            alert(title= "UTN FRA",message= "¡Comprando {} lamparitas obtuvo un 50% de descuento! Su total es ${}".format(cantidad_elegida,Valor_con_Descuento))
        else:
            if marca_elegida == "ArgentinaLuz" and cantidad_elegida == 5:
                #descuento 40%
                Descuento = Precio_total * 0.40
                #muestro total
                Valor_con_Descuento = Precio_total - Descuento
                alert(title= "UTN FRA", message= "¡Comprando 5 lamparitas ArgentinaLuz obtuvo un 40% de descuento! Su total es ${}".format(Valor_con_Descuento))
            else:
                if not marca_elegida == "ArgentinaLuz" and cantidad_elegida == 5:
                    #descuento 30%
                    Descuento = Precio_total * 0.30
                    #muestro total
                    Valor_con_Descuento = Precio_total - Descuento
                    alert(title="UTN FRA", message= "¡Comprando 5 lamparitas {} obtuvo un 30% de descuento! Su total es ${}".format(marca_elegida,Valor_con_Descuento))
                else:
                    if marca_elegida == "ArgentinaLuz" and cantidad_elegida == 4 or marca_elegida == "FelipeLamparas" and cantidad_elegida == 4:
                        Descuento = Precio_total * 0.25
                        Valor_con_Descuento = Precio_total - Descuento
                        alert(title="UTN FRA", message= "¡Comprando 4 lamparitas {} obtuvo un 25% de descuento! Su total es ${}".format(marca_elegida,Valor_con_Descuento))
                    else:
                        if not marca_elegida == "ArgentinaLuz" or not marca_elegida == "FelipeLamparas" and cantidad_elegida == 4:
                            Descuento = Precio_total * 0.20
                            Valor_con_Descuento = Precio_total - Descuento
                            alert(title="UTN FRA", message= "¡Comprando 4 lamparitas {} obtuvo un 20% de descuento! Su total es ${}".format(marca_elegida,Valor_con_Descuento))
                        else:
                            if marca_elegida == "ArgentinaLuz" and cantidad_elegida == 3:
                                Descuento = Precio_total * 0.15
                                Valor_con_Descuento = Precio_total - Descuento
                                alert(title="UTN FRA", message= "¡Comprando 3 lamparitas {} obtuvo un 15% de descuento! Su total es ${}".format(marca_elegida,Valor_con_Descuento))
                            else:
                                if marca_elegida == "FelipeLamparas" and cantidad_elegida == 3:
                                    Descuento = Precio_total * 0.10
                                    Valor_con_Descuento = Precio_total - Descuento
                                    alert(title="UTN FRA", message= "¡Comprando 3 lamparitas {} obtuvo un 10% de descuento! Su total es ${}".format(marca_elegida,Valor_con_Descuento))
                                else:
                                    if not marca_elegida == "ArgentinaLuz" and not marca_elegida == "FelipeLamparas" and cantidad_elegida == 3:
                                        Descuento = Precio_total * 0.05
                                        Valor_con_Descuento = Precio_total - Descuento
                                        alert(title="UTN FRA", message= "¡Comprando 3 lamparitas {} obtuvo un 5% de descuento! Su total es ${}".format(marca_elegida,Valor_con_Descuento))
                                        
        if Valor_con_Descuento > 4000:
            Descuento = Valor_con_Descuento * 0.05
            Valor_con_descuento_adicional = Valor_con_Descuento - Descuento
            
            alert(title="UTN FRA", message="¡Obtuvo un %5 mas de descuento por haber gastado más de $4000 pesos! Su total es {}".format(Valor_con_descuento_adicional))
                                        
        
        #D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()