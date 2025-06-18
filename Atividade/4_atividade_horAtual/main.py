'''
# TODO - ATIVIDADE : Criar um programa que mostre a hora atual sempre quando atualizada a casa segundo
# NOTE - para  interroper o programa, use a tecla de atalho Ctrl + C
'''
import datetime
from datetime import date
import time

agora = datetime.datetime.now()
hora_formatada = agora.strftime("%H:%M:%S")

while True:
    try:
        print("Hora atual: {hora_formatada}")
        time.sleep(1)
        break

    except Exception as e:
        print(f"Não foi possivel realizar a operaçao. {e}.")

