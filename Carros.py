lista = []
consumoCombustivel = []
gasto = []
qtd = int(input(" Número de modelos de carros: "))

for i in range(qtd):
  carros = input(" Escolha um modelo de carro para calcular: ")
  litros = float(input("Quantos litros de gasolina o carro faz por Km?: "))
  litrosporKm = 500/litros
  gastoCombustivel = (litrosporKm * 4.90)
  lista.append(carros)
  consumoCombustivel.append(round (litrosporKm,2))
  gasto.append(round (gastoCombustivel,2))


print(lista, consumoCombustivel, gasto )

 