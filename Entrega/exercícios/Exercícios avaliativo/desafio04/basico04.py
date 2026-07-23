print("Informe a temperatura do servidor: ")
temperatura = float(input())
if temperatura < 0:
    print("Sensor com erro!")
elif temperatura >= 70:
    print("Alerta!")
else:
    print("Normal!")
