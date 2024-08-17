from ingrediente import Ingredientes
from cant_ing_receta import Cant_ing_x_receta


class Receta(Ingredientes,Cant_ing_x_receta):
    def __init__(self,costo_ing, receta, cantidad_receta):
        #self.ingredientes = [ing.to_dict() for ing in ingredientes]
        self.ingredientes_costo = costo_ing
        self.nombre = receta
        self.cantida_hecha = cantidad_receta
#    @property
#    def costo_total(self):
        
#        costo = 0
#        receta_ingredientes = {}
#        for ingre in self.ingredientes:
#            for key in ingre:
#                if key == "precio" and not None:
#                    costo += ingre[key]
#       return f"{round(costo,7)}"      

                
    def __str__(self):
        return f"Reseta: {self.nombre} costos de la receta: {self.ingredientes_costo} Cantidad receta elavorada: {self.cantida_hecha}"

p1 = Ingredientes("ht",45,31.5,"kg")
p2 = Ingredientes("panela",22.8,21,"kg")
p3 = Ingredientes("mantequilla",15,24,"kg")
p4 = Ingredientes("manteca",15,46,"kg")
p5 = Ingredientes("caramelina",650,3,"gr")
p6 = Ingredientes("levadura",500,3.5,"gr")
p7 = Ingredientes("conservante",1,6,"kg")
p8 = Ingredientes("bicarbonato",1,4,"kg")

cantida_ing = Cant_ing_x_receta([p1,p2,p3,p4,p5,p6,p7,p8],{"ht":6320,"panela":5000,"mantequilla":470,"manteca":300,"caramelina":60,"levadura":20,"conservante":25,"bicarbonato":80})
receta_qks = Receta(cantida_ing,"qks",1.5)
print(receta_qks)
