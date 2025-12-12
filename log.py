Nome = input("Digite o nome do herói: ")
xp = int(input("Digite o valor do xp: "))

if (xp < 1000):
    nivel = "Ferro"
    print(f" O heroi de nome {Nome} está no nível {nivel}")
if (xp > 1000 and xp < 2000):
    nivel = "Bronze"
    print(f" O heroi de nome {Nome} está no nível {nivel}")
if (xp > 2000 and xp < 5000):
    nivel = "Prata"
    print(f" O heroi de nome {Nome} está no nível {nivel}")
if (xp > 6000 and xp < 7000):
    nivel = "Ouro"
    print(f" O heroi de nome {Nome} está no nível {nivel}")
if (xp > 7000 and xp < 8000):
    nivel = "Platina"
    print(f" O heroi de nome {Nome} está no nível {nivel}")
if (xp > 8000 and xp < 9000):
    nivel = "Ascendente"
    print(f" O heroi de nome {Nome} está no nível {nivel}")
if (xp > 9000 and xp < 10000):
    nivel = "Imortal"
    print(f" O heroi de nome {Nome} está no nível {nivel}")
if (xp >=10000):
    nivel = "Radiante"
    print(f" O heroi de nome {Nome} está no nível {nivel}")
