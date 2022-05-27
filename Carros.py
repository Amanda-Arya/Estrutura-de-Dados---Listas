lista = []
consumoCombustivel = []
gasto = []
qtd = int(input(" Número de modelos de carros: "))

for i in range(qtd):
  carros = input(" Escolha um modelo de carro para calcular: ")
  litros = float(input("Quantos litros de gasolina o carro faz por Km?: "))
  distancia = float(input("Qual a distância que você vai percorrer?: "))
  preco = float(input("Qual o preço do combustível?: "))
  litrosporKm = distancia/litros
  gastoCombustivel = (litrosporKm * preco)
  lista.append(carros)
  consumoCombustivel.append(round (litrosporKm,2))
  gasto.append(round (gastoCombustivel,2))

for i in range(qtd):
  print(f"Carro: {lista[i]} - Consumo em litros: {consumoCombustivel[i]} - Preço total: {gasto[i]}")
 