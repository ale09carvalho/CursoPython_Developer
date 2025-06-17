'''
# TODO -  ATIVIDADE:
Crie um programa com o seguinte menu:
- Calcular àrea de um círculo
- Calcular tamanho de uma circunferência
- Sair do programa
'''
# importando biblioteca
import math as m

print(f"{'='*10}MENU{'='*20}\n")
print("Escolha a opção.")
print(" 1 - Calcular a area do cículo.")
print(" 2 - Calcular o tamanho da circunferência.")

opcao = int(input("Informe a opção desejada: ").strip())

# raiz quadrada
try:
    match opcao:
        case 1:
            r = float(input("Informe o raio do circulo: "))
            a = m.pi *(r**2)
            print(f"A area do circulo corresponde a: {a}.")
        case 2: 
            c = float(input("Informe o cumprimento."))
            perimetro = C = 2*m.pi*r

            C = 2πr.
        case _:
             print("Operação inválida.")

except Exception as e:
    print(f"Não foi possivel executar a operação. {e}.")


