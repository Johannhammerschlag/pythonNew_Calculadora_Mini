a = float(input("Primeiro núm:"))
b = float(input("Segundo núm:"))
operação = input("Digite qual operação (+,-,* ou /):")
if operação == "+":
    total = a + b
elif operação == "-":
    total = a - b
elif operação == "*":
    total = a * b
elif operação == "/":
    total = a / b
else:
    print("Operação inválida!")
    total = 0
print("total: ", total)
