# CONSTANTES = Variáveis que não vão mudar
# Utiliza-se letras maiúsculas

velocidade = 61
local_carro = 101

VELOCIDADE_RADAR = 60
LOCAL_RADAR = 100
RADAR_RANGE = 1

#if velocidade > VELOCIDADE_RADAR:
  #  print(f'Você está a {velocidade-VELOCIDADE_RADAR}km/h acima do limite de velocidade')

if local_carro >= (LOCAL_RADAR - RADAR_RANGE) and \
local_carro <= (LOCAL_RADAR + RADAR_RANGE):
    print('O carro foi multado')
else:
    print('O carro não foi multado')
    

