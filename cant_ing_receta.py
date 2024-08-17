class Cant_ing_x_receta:
    def __init__(self,ing:list, cant):
        self.ing = ing 
        self.cant = cant
    @property
    def total_ing_costo(self):
        receta_ing = {}
        for ingr in self.ing:
            items = ingr.to_dict()
            for _ in items:
                if items["nombre"] == "panela":
                    if self.cant["panela"] == 5000:
                        self.cant["panela"] = 3375

                receta_ing[items["nombre"]] = round(float(items["precio"])* float(self.cant[items['nombre']]),3)
        total = round(sum(receta_ing.values()),3)

        return total       
                

#  for _ in items:
 #               precio = items['precio']
 #               cant = items['cantidad']
  #              nombre = items['nombre']
   #             cantida[nombre] =                    

              
    def __str__(self):
        return f"ingredientes{self.cant}-> total receta {self.total_ing_costo}"
