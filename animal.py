

class Animal:



    def __init__(self, p_nombre, p_especie, p_edad):
        self.nombre = p_nombre
        self.especie = p_especie 
        self.edad = p_edad
        self.energia = 50 
        

    def presentarse(self):
        text = f'\nHola, soy {self.nombre} ({self.especie} | {self.edad} ã)'
        

    def jugar(self):
        self.energia -= 20
        if self.energia < 0:
            self.energia = 0 
        print(f'\n({self.nombre}) Juagando... energía nueva: {self.energia}')


    def comer(self, gramos: int):
        self.energia += (gramos // 10)
        if self.energia > 100:
            self.energia = 100
        print(f'\n({self.nombre}) Comiendo... energía nueva: {self.energia}')


    def dormir(self):
        self.energia += 30
        if self.energia > 100:
            self.energia = 100 
        print(f'\n({self.nombre}) Durmiendo... energía nueva: {self.energia}')
        
        















