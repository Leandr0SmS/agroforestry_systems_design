from sqlalchemy import Column, String, Integer#, ForeignKey

from  model import Base

import numpy as np
import plotly.graph_objects as go
import json 


class Canteiro(Base):
    __tablename__ = 'canteiros'

    id_canteiro = Column(Integer, primary_key=True)
    nome_canteiro = Column(String(140), unique=True, nullable=False)
    x_canteiro = Column(Integer, nullable=False)
    y_canteiro = Column(Integer, nullable=False)
    plantas_canteiro = Column(String(100000), nullable=False)
    dados_grafico_cantiero = Column(String(100000))

    def __init__(self, nome_canteiro:str, x_canteiro:int, y_canteiro:int):
        """
        Cria um Canteiro

        Parametros:
            nome_canteiro: O nome da canteiro
            x_canteiro: Valor do eixo X do canteiro
            y_canteiro: Valor do exico Y do canteiro
        """
        self.nome_canteiro = nome_canteiro
        self.x_canteiro = x_canteiro
        self.y_canteiro = y_canteiro
        
    def distribuir_plantas(self, plantas):
        # Definindo o canteiro
        canteiro = {
            "emergente": [],
            "alto": [],
            "medio": [],
            "baixo": []
        }
    
        canteiro_x = int(self.x_canteiro)
        canteiro_y = int(self.y_canteiro)
    
        # Ordenando as plantas por tempo de colheita (priorizando colheita mais rápida)
        plantas_ordenadas = sorted(plantas, key=lambda x: int(x['tempo_colheita']))
    
        # Distribuindo as plantas nos estratos
        for planta in plantas_ordenadas:
            sombra = int(planta['sombra'])
            espacamento = int(planta['espacamento'])
            estrato = planta['estrato']
            
            print('planta: ', planta)
    
            # Calculando a área disponível
            area_disponivel = canteiro_x * canteiro_y
            print('area disponivel: ', area_disponivel)

            # Calculando a área que a planta pode ocupar no estrato
            estrato_disponivel = area_disponivel * (sombra / 100)
            print('estrato_disponivel: ', estrato_disponivel)

            # Calculando a área que a planta pode ocupar
            area_planta = (espacamento ** 2)
            print('area_planta: ', area_planta)
    
            # Verifica se a planta cabe no espaço disponível
            if area_planta > estrato_disponivel:
                continue
    
            num_plantas_possiveis = int(estrato_disponivel // area_planta)
            if num_plantas_possiveis == 0:
                continue
                
            print('numero plantas possiveis:', num_plantas_possiveis)

            num_plantas_y = 1
            num_plantas_x = num_plantas_possiveis
            espacamento_x = canteiro_x // (num_plantas_x + 1)
            espacamento_y = canteiro_y // (num_plantas_y + 1)
                
            while espacamento_x < espacamento:
                num_plantas_x = num_plantas_possiveis
                if espacamento_y < espacamento:
                    continue
                num_plantas_y += 1
                num_plantas_x /= num_plantas_y
                espacamento_x = int(canteiro_x // (num_plantas_x + 1))
                espacamento_y = int(canteiro_y // (num_plantas_y + 1))

            print(f"espacamentoX: {espacamento_x}, espacamentoY: {espacamento_y}")

            num_plantas_x = int(num_plantas_x)
            num_plantas_y = int(num_plantas_y)
            
            print(f'num_plantas_x: {num_plantas_x}, num_plantas_y: {num_plantas_y}')
            
            y = espacamento_y
    
            num_planta = 0 
            for i in range(num_plantas_y):
                x = espacamento_x
                
                for j in range(num_plantas_x):
                    
                    canteiro[estrato].append({
                        "nome_planta": planta['nome_planta'],
                        "estrato": estrato,
                        "posicao": [x, y],
                        "diametro": espacamento,
                        "tempo_colheita": planta['tempo_colheita']
                    })
                    
                    num_planta +=1
                    print(f"planta: {num_planta}: {[x,y]}")
                    
                    x += espacamento_x
                    
                    #if len(canteiro[estrato]) >= num_plantas_possiveis:
                    #    continue  # Retorna quando atingir o limite de plantas
                
                y += espacamento_y
    
        self.plantas_canteiro = canteiro
        
    def criar_grafico(self):
        #try: 
        fig = go.Figure()

        range_x=[0, self.x_canteiro]
        range_y=[0, self.y_canteiro]
        
        # Calculate sizeref dynamically based on the plot dimensions
        plot_width = range_x[1] - range_x[0]
        plot_height = range_y[1] - range_y[0]
        
        # Ensure both axes have the same scaling
        fig.update_layout(
            autosize=False,  
            xaxis=dict(
                scaleanchor="y",  # Locks X-axis to Y-axis scale
                range=range_x,     # Restrict X-axis to defined range
                constrain='domain' # Prevents expansion beyond range
            ),
            yaxis=dict(
                scaleanchor="x",  # Locks Y-axis to X-axis scale
                range=range_y,    # Restrict Y-axis to defined range
                constrain='domain' # Prevents expansion beyond range
            )
        )
        
        max_diameter = max([planta['diametro'] for plantas in self.plantas_canteiro.values() for planta in plantas])
        
        # Adjust divisor to control relative size of markers
        scaling_factor = 5  # Increase this value to make plants smaller
        sizeref = (max(range_x[1], range_y[1]) / max_diameter) / scaling_factor

        np.random.seed(100)
        N = len(self.plantas_canteiro)
        colors = np.random.rand(N)
        

        for estrato, plantas in self.plantas_canteiro.items():
            
            x=[]
            y=[]
            sz = []
            titles = []
            
            for planta in plantas:
                title = []
                title.extend([
                    planta['nome_planta'],
                    planta['estrato'],
                    planta['posicao'],
                    planta['diametro']
                ])
                x.append(int(planta['posicao'][0]))
                y.append(int(planta['posicao'][1]))
                sz.append(int(planta['diametro']))
                titles.append(title)
        
            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                name=estrato,
                mode="markers",
                customdata=titles,
                hovertemplate="<b>Nome</b>: %{customdata[0]}<br><b>estrato</b>: %{customdata[1]}<br><b>Posicao</b>: %{customdata[2]}<br><b>diametro</b>: %{customdata[3]}<extra></extra>",
                marker=go.scatter.Marker(
                    size=sz,
                    sizemode="diameter",
                    sizeref=sizeref,
                    color=colors[0],
                    opacity=0.6,
                    colorscale="Earth"
                )
            ))

        # Configuração Eixos
        fig.update_xaxes(
            type="linear",
            range=range_x
        )
        fig.update_yaxes(
            type="linear",
            range=range_y
        )
        
        fig.show()
        
        # Extract only the data and layout
        fig_data = {
            "data": fig.to_dict()["data"],    # Raw trace data
            "layout": fig.to_dict()["layout"] # Layout config
        }
        
        fig_data_json = json.dumps(fig_data)
        print(len(fig_data_json))

        # Converts to a JSON string
        fig_data_json_str = fig.to_json()

        print("json_str: ", len(fig_data_json_str))

        self.dados_grafico_cantiero = fig_data_json_str
        
        return fig_data_json_str

        #except Exception as e:
        #    # caso um erro fora do previsto
        #    error_msg = "Não foi possível gerar o Canteiro"
        #    logger.warning(f"Erro ao gerar o canteiro, {error_msg}")
        #    return jsonify({
        #        "error": error_msg,
        #        "status": "failed"
        #    }), 500
        
    def __repr__(self):
        return f'Canteiro("{self.nome_canteiro}","{self.plantas_canteiro}")'
