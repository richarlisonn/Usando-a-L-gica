nome = input("Olá, digite seu nome: ")
print ("Prazer" , (nome) , "!")

horario = int(input("digite horario em que você esta respondendo essa menssagem "))

if horario <= 11:
    print ("Bom dia")
if horario >= 12 and horario <=17:
    print("Boa tarde ")
if horario >= 18:
    print("Boa noite")
