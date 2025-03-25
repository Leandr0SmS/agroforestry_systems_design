from sqlalchemy import Column, String, Integer#, ForeignKey
import math

from  model import Base


class Canteiro(Base):
    __tablename__ = 'canteiros'

    id_canteiro = Column(Integer, primary_key=True)
    nome_canteiro = Column(String(140), unique=True, nullable=False)
    x_canteiro = Column(Integer, nullable=False)
    y_canteiro = Column(Integer, nullable=False)
    data_canteiro = Column(String(1000), nullable=False)

    def __init__(self, nome_canteiro:str, data_canteiro:str):
        """
        Cria um Canteiro

        Arguments:
            nome_canteiro: O nome da canteiro;
            data_canteiro: Svg Json do canteiro;
        """
        self.nome_canteiro = nome_canteiro
        self.data_canteiro = data_canteiro
        
    def distribuir_plantas_no_canteiro(self, plantas):
        # Definindo o canteiro
        canteiro = {
            "emergente": [],
            "alto": [],
            "medio": [],
            "baixo": []
        }

        canteiro_x = int(self.x_canteiro)
        canteiro_y = int(self.y_canteiro)

        # Ordenando as plantas por tempo de colheita (para priorizar plantas de colheita mais rápida)
        plantas_ordenadas = sorted(plantas, key=lambda x: int(x['tempo_colheita']))

        # Distribuindo as plantas nos estratos
        for planta in plantas_ordenadas:

            print('planta: ', planta)

            sombra = int(planta['sombra'])
            espacamento = int(planta['espacamento'])
            estrato = planta['estrato']
            
            #  # Calculando a área que a planta pode ocupar no estrato
            #  estrato_disponivel = area_disponivel * (sombra / 100)

            # numero de plantas possiveis X e Y
            num_plantas_x = math.floor(canteiro_x / espacamento)
            num_plantas_y = math.floor(canteiro_y / espacamento)

            if num_plantas_x > 0 and num_plantas_y > 0:
                # Sobra espaco X e Y nas bordas do canteiro
                diff_esp_x = canteiro_x % (num_plantas_x * espacamento)
                diff_esp_y = canteiro_x % (num_plantas_y * espacamento)
                print( 'diff: ', diff_esp_x, diff_esp_y)

                # Valor iniciais
                x_init = (espacamento / 2) + (diff_esp_x / 2)
                y = (espacamento / 2) + (diff_esp_y / 2)

                num_planta = 0
                for _ in range(num_plantas_y):
                    # Iniciando x
                    x = x_init

                    for _ in range(num_plantas_x):

                        num_planta +=1
                        print(f"planta: {num_planta}: {[x,y]}")

                        # Adicionando a planta ao estrato
                        canteiro[estrato].append({
                            "nome_planta": planta['nome_planta'],
                            "estrato": estrato,
                            "posicao": [x, y],
                            "diametro": espacamento,
                            "tempo_colheita": planta['tempo_colheita']
                        })
                        # atualizando Y
                        x += espacamento

                    # atualizando X
                    y += espacamento
            else:
                 continue
             
        return canteiro
        
    def __repr__(self):
        return f'Canteiro("{self.nome_canteiro}","{self.data_canteiro}")'
