'''
Simulación de un día en el refugio

'''

from animal import Animal

#Instanciar animales
luna = Animal('Luna', 'gato', 3)
rocky = Animal('Rocky', 'perro', 5)
kiwi = Animal('Kiwi', 'loro', 2)

#Presentaciones 
luna.presentarse()
rocky.presentarse()
kiwi.presentarse()

#Actividad Luna
luna.jugar()
luna.comer(150)
luna.dormir()

#Actividad Rocky
rocky.jugar()
rocky.jugar()
rocky.jugar()
rocky.comer(300)

#Actividad kiwi 
kiwi.comer(100)
kiwi.dormir()








