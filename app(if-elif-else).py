#Classificação do consumo de água e indentificando o perfil adequado para o imóvel.

imovel = input("Digite o imóvel (comercial, casa ou apartamento): ")

consumo = float(input("Digite o consumo de água em metros cúbicos(m3): "))

if imovel == "comercial":
    print("tarifa comercial aplicada - consulte o plano corporativo.")

elif imovel == "apartamento" and consumo < 10:
    print("Consumo econômico - excelente controle de água.")

elif (imovel == "apartamento" or imovel == "casa") and consumo <= 25:
    print("Consumo moderado - dentro do padrão residencial.")

else:
    print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")