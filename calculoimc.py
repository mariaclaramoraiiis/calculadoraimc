
# Extração de dados do usuário (peso e altura)
altura= float (input("Qual a sua altura?"))
peso= int (input("Qual o seu peso?"))

# Cálculo do IMC
imc= round (peso/altura**2,1)

# Retorno do resultado para o usuário + a classificação do IMC
if imc <=18.5:
    print (f"Seu imc é {imc} e você se encontra com baixo peso")
elif imc <=24.9:
    print (f"Seu imc é {imc} e você se encontra com peso normal")
elif imc <=29.9:
    print (f"Seu imc é {imc} e você se encontra com sobrepeso")
elif imc <=34.9:
    print (f"Seu imc é {imc} e você se encontra com obesidade grau 1")
elif imc <=39.9:
    print (f"Seu imc é {imc} e você se encontra com obesidade grau 2")
elif imc >40:
    print (f"Seu imc é {imc} e você se encontra com obesidade grau 3")
