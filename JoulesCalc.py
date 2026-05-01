#!/usr/bin/python3
print("Calculadora de Joules")
print(" ")
while True:
 peso= float (input("Peso do Projétil em Grains: "))
 mps=float (input("Velocidade em Metros por Segundos: "))
 joules= (peso*mps*mps/30860)
 joulesfinal = round(joules, 2)
 print ("Energia em Joules: ", joulesfinal)
 print (" ")
 print ("Calculadora zerada ")
 print ("Novo calcúlo ")
 #cont= input("Calcular novamente ? S ou n ? ")
 print (" ")
 #if cont== "s": continue
 #if cont== "n": break
 
