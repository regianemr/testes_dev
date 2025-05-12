# 1 Questão
# Resposta: 91

# 2 Questão
def seq_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero or numero == 0

numero_informado = int(input("Informe um número: "))

if seq_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} NÃO pertence à sequência de Fibonacci.")


