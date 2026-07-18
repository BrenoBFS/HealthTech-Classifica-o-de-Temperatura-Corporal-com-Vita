# Lê a temperatura corporal informada pelo paciente
entrada = input()
if float(entrada) <= 35.8:
    print("Hypothermia")

elif float(entrada) < 36.0:
    print("Normal")

elif float(entrada) <= 37.5:
    print("Normal")
elif float(entrada) <= 38.2:
    print("Fever")
temperatura = float(entrada)  # Converte a entrada para decimal

# TODO: Implemente a estrutura condicional para classificar a temperatura
# Dica: Use if, elif e else para verificar as faixas e imprimir "Hypothermia", "Normal" ou "Fever"