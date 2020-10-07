print("Calculadora de fuerza de atraccion")
print('Inserta el valor sin el 10 de la primera masa')
MassOne = float(input())
print('Inserta el valor sin el 10 de la segunda masa')
MassTwo = float(input())
print('Inserta el exponente de la primera masa')
MassOne_Exponent = int(input())
print('Inserta el exponente de la segunda masa')
MassTwo_Exponent = int(input())
print('Inserta la distancia')
Distance = float(input())
print("Inserta el exponente de la distancia")
Distance_Exponent = int(input())

print("Calculando..")

AttractionForce = MassOne * MassTwo / (Distance * Distance) * 6.7
Distance_Exponent1 = Distance_Exponent * 2
AttractionForce_Exponent = MassOne_Exponent + MassTwo_Exponent - Distance_Exponent1 -11
print('Calculation job done')
print('Tu cantidad es:')
print(AttractionForce)
print("x10 a la")
print(AttractionForce_Exponent)