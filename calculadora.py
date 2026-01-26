import math


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def porcentagem(valor, percentual):
    return (valor * percentual) / 100


def potencia(base, expoente):
    return base ** expoente


def raiz(valor):
    return math.sqrt(valor)


def mostrar_historico(historico):
    if not historico:
        print("Nenhuma operação realizada ainda.")
    else:
        print("\n--- HISTÓRICO ---")
        for i, item in enumerate(historico, start=1):
            print(f"{i}) {item}")


def salvar_historico(historico):
    with open("historico.txt", "w", encoding="utf-8") as arquivo:
        for item in historico:
            arquivo.write(item + "\n")


def main():
    historico = []

    while True:
        print("\n--- CALCULADORA ---")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Porcentagem")
        print("6 - Potência")
        print("7 - Raiz quadrada")
        print("8 - Ver histórico")
        print("9 - Limpar histórico")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            salvar_historico(historico)
            print("Encerrando a calculadora...")
            break

        if opcao == "8":
            mostrar_historico(historico)
            continue

        if opcao == "9":
            historico.clear()
            print("Histórico limpo com sucesso.")
            continue

        try:
            if opcao in ["7"]:
                num1 = float(input("Digite o número: "))
            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: digite apenas números.")
            continue

        if opcao == "1":
            resultado = soma(num1, num2)
            historico.append(f"{num1} + {num2} = {resultado}")
        elif opcao == "2":
            resultado = subtracao(num1, num2)
            historico.append(f"{num1} - {num2} = {resultado}")
        elif opcao == "3":
            resultado = multiplicacao(num1, num2)
            historico.append(f"{num1} * {num2} = {resultado}")
        elif opcao == "4":
            if num2 == 0:
                print("Erro: divisão por zero.")
                continue
            resultado = divisao(num1, num2)
            historico.append(f"{num1} / {num2} = {resultado}")
        elif opcao == "5":
            resultado = porcentagem(num1, num2)
            historico.append(f"{num2}% de {num1} = {resultado}")
        elif opcao == "6":
            resultado = potencia(num1, num2)
            historico.append(f"{num1} ^ {num2} = {resultado}")
        elif opcao == "7":
            if num1 < 0:
                print("Erro: não existe raiz de número negativo.")
                continue
            resultado = raiz(num1)
            historico.append(f"√{num1} = {resultado}")
        else:
            print("Opção inválida.")
            continue

        print(f"Resultado: {resultado:.2f}")


if __name__ == "__main__":
    main()