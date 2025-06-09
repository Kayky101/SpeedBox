class SimuladorEntrega:
    def __init__(self, meio_transporte, entregador):
        self.meio_transporte = meio_transporte
        self.entregador = entregador

    def calcular_tempo(self, distancia):
        if self.meio_transporte.velocidade == 0: return float('inf')
        return distancia / self.meio_transporte.velocidade

    def calcular_custo(self):
        return self.meio_transporte.custo

class MeioTransporte:
    def __init__(self, tipo, velocidade, custo):
        self.tipo = tipo
        self.velocidade = float(velocidade)
        self.custo = float(custo)

    def __str__(self):
        return f"{self.tipo} (Velocidade: {self.velocidade} km/h, Custo: R$ {self.custo:.2f})"

    def calculo_tempo_estimado(self, distancia):
        sim = SimuladorEntrega(self, None)
        tempo = sim.calcular_tempo(distancia)
        print(f"Tempo estimado de entrega: {tempo:.2f} horas")
        return tempo

    def calculo_custo_transporte(self):
        sim = SimuladorEntrega(self, None)
        custo = sim.calcular_custo()
        print(f"Custo estimado de transporte: R$ {custo:.2f}")
        return custo

class Carro(MeioTransporte):
    def __init__(self, modelo, marca, capacidade_max, velocidade_max):
        super().__init__("Carro", float(velocidade_max), 30.0)
        self.modelo = modelo
        self.marca = marca
        self.capacidade_max = capacidade_max
        self.velocidade_max = velocidade_max

class Moto(MeioTransporte):
    def __init__(self, modelo, marca, capacidade_max, velocidade_max):
        super().__init__("Moto", float(velocidade_max), 15.0)
        self.modelo = modelo
        self.marca = marca
        self.capacidade_max = capacidade_max
        self.velocidade_max = velocidade_max

class Caminhao(MeioTransporte):
    def __init__(self, modelo, marca, capacidade_max, velocidade_max):
        super().__init__("Caminhão", float(velocidade_max), 60.0)
        self.modelo = modelo
        self.marca = marca
        self.capacidade_max = capacidade_max
        self.velocidade_max = velocidade_max

class Transportadora:
    def __init__(self, cnpj, endereco):
        self.cnpj = cnpj
        self.endereco = endereco
        self.meios_transporte = []

    def adicionar_meio_transporte(self, meio):
        if isinstance(meio, MeioTransporte):
            self.meios_transporte.append(meio)
        else:
            print("Transporte inválido.")
