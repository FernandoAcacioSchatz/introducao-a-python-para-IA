print("Informe a temperatura do servidor: ")
temperatura = float(input())
if temperatura < 0:
    print("Sensor com erro!")
elif temperatura >= 90:
    print("Crítico!")
    print("Desligando o servidor...")
elif temperatura > 70 and temperatura < 90:
    print("Alerta!")
else:
    print("Normal!")
