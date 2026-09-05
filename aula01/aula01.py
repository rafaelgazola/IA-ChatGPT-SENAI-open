import time
print("Bem vindo ao help das notas de aluno!!!")  # primeiro  print para dizer bem vindo

while True:
    try:
        n1 = float(input("Insira a primeira nota:"))  #primeira variavel para contar valor
        n2 = float(input("Insira a segunda nota:"))
        n3 = float(input("Insira a terceira nota:"))
        n4 = float(input("Insira a quarta nota:"))
    except ValueError as erro:
        print(f"Apenas numero para realizar o calculo {erro}!!!")
        continue

    soma = n1 + n2 + n3 + n4

    resultado = soma/4

    print("===CALCULANDO===")
    time.sleep(3)
    
    print(f"Este é o resultado da media do aluno: {resultado}")

    if resultado == 10:
        print(f"Aluno passou com: {resultado}")

    elif resultado >= 7:
        print(f"O aluno passou dentro da media: {resultado}")

    else:
        print(f"O aluno nao passou a media é: {resultado}")
    break
