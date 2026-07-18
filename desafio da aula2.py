# Recebe a temperatura corporal do paciente como entrada
entrada = input()
if float(entrada) <= 36.8:
    print("Aguardar")
elif float(entrada) <= 37.5:
    print("Atendimento imediato")
elif float(entrada) <= 39.2:
    print("Atendimento imediato")
elif float(entrada) <= 36.0:
    print("Aguardar")
# Converte a entrada para float para permitir comparação decimal
temperatura = float(entrada)