#Classificação do consumo de água e indentificando o perfil adequado para o imóvel.

imovel = input("Digite o imóvel (comercial, casa ou apartamento): ")

consumo = float(input("Digite o consumo de água em metros m3: "))

match imovel:
    case "comercial":
        print("Tarifa comercial aplicada - consulte o plano corporativo.")

    case "apartamento" if consumo < 10:
        print("Consumo econômico - excelente controle de água.")

    case "apartamento" | "casa" if consumo <= 25:
        print("Consumo moderado - dentro do padrão residencial.")

    case _:
        print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")