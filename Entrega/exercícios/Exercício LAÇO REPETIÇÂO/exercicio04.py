num = int(input("Digite um número inteiro: "))

if num > 0:
    for i in range(1, num + 1):
        if i == num:
            print(f"1/{i}", end="")
        else:
            print(f"1/{i} + ", end="")
else:
    print("O número digitado não é um inteiro positivo.")
