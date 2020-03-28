import time

condicao = True
numero = 10
def executeSomething():
    print('Somando', numero )
    time.sleep(2)

while condicao:
    executeSomething()
    numero+=1

    if(numero == 15):
        condicao=False
        print('Acabou - >', numero )