def inverter_string(texto):
    invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

texto_original = input("Digite uma string para inverter: ")

resultado = inverter_string(texto_original)

print(f"String invertida: {resultado}")
