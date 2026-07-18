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