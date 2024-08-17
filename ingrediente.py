
class Ingredientes:
    def __init__(self,nombre:str,cant:int,precio:float,kg_gr:str):
        self.nombre_i = nombre
        self.cantid = cant
        self.precio = precio
        self.kg_gr = kg_gr
    @property
    def valor_x_gramo(self):
        peso = self.kg_gr.lower()
        if peso == "kg":
            costo = (self.precio / self.cantid) / 1000
            return costo 
        elif peso == "gr":
            costo = self.precio / self.cantid
            return costo
        return f"{self.kg_gr} opcion no definida"

    def to_dict(self):
        return {
            "nombre":self.nombre_i,
            "cantidad":self.cantid,
            "precio":self.valor_x_gramo,
            "kg_gr":self.kg_gr
        }

    def __str__(self):
        return f"{self.nombre_i}->{self.cantid}->{self.precio}->{self.kg_gr}"


