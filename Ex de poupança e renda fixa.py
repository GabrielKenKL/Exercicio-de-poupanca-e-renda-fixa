#Algorítmo
#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.
print("Digite o valor do investimento:")
Valor = float(input())

print("Indique qual tipo de investimento desejado: 1 para poupança e 2 para renda fixa")
N = int(input())
if N == 1:
    VN = Valor * 1.03
elif N == 2:
    VN = Valor * 1.05

print("O valor corrigido é de: R$" , VN)