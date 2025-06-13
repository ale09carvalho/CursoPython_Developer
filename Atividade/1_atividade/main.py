'''
# TODO - Atividade:
#  Crie um programa que RECEBA do usuario O VALOR do etanol e da gasolina em reais, e INFORME ao usuario qual e o melhor combustível para abastecimento.
# NOTE - o usuario poderá informar varias vezes os valores, e irá encerrar o programa quando desejar.
# NOTE Compensa o Etanol caso ele tenha até 70% do valor da gasolina.
'''

# entra de dados
try:   
    while True:
        RS_gasolina = float(input('Informe o valor da gasolina: R$ ').replace(',', '.'))
        RS_etanol = float(input('Informe o valor do etanol: R$ ').replace(',', '.'))

        # calcula se o etanol é 70% do valor da gasolina
        if RS_etanol <= (RS_gasolina * 0.7):
            print('Atençao!! sugiro que você abastecer com Etanol.')
        else:
            print('Atençao!! Sugiro que você abasteça com Gasolina!')

        # pergunta se deseja continuar
        continuar = input('Deseja informar novos valores? (s/n): ').strip().lower()
        if continuar != 's':
            break
except Exception as e:
    print(f'Ocorreu um erro: {e}')
finally:
    print('Programa encerrado. Obrigado !')
# Fim do programa