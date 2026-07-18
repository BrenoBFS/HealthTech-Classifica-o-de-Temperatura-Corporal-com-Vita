# Recebe o sintoma informado pelo paciente
sintoma = input().strip()  # Remove espaços extras
if sintoma == "dor no peito":
    print("atendimento imediato")

elif sintoma == "febre":
    print("agendar consulta")

elif sintoma == "dor de cabeca":
    print("repouso em casa")

elif sintoma == "falta de ar":
    print("atendimento imediato")