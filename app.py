from flask import redirect, jsonify
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from logger import logger

from model import Session, Canteiro
from schemas import *

import numpy as np
import plotly.graph_objects as go
import json 

info = Info(title="Meu Canteiro Plot", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
canteiro_tag = Tag(name="Plot", description="Visualização do Canteiro")

@app.get('/', tags=[home_tag])
def home():
    """
    Redireciona para /openapi, 
    tela que permite a escolha do estilo de documentação. 
    """
    return redirect('/openapi')
    
@app.get('/canteiro', tags=[canteiro_tag],
         responses={"200": CanteiroSchema, "404": ErrorSchema})
def get_canteiro():
    """
    Retorna uma representação do Canteiro.
    """
    logger.debug(f"Criando Canteiro")
    
    canteiro_data = {
        "plantas": [
            {
              "espacamento": 200,
              "estrato": "emergente",
              "nome_planta": "Embaúba",
              "sombra": 20,
              "tempo_colheita": 1095
            },
            {
              "espacamento": 100,
              "estrato": "alto",
              "nome_planta": "Jucara",
              "sombra": 40,
              "tempo_colheita": 2555
            },
            {
              "espacamento": 50,
              "estrato": "medio",
              "nome_planta": "Pimenta-do-reino",
              "sombra": 60,
              "tempo_colheita": 1460
            },
            {
              "espacamento": 40,
              "estrato": "baixo",
              "nome_planta": "Abacaxi",
              "sombra": 80,
              "tempo_colheita": 730
            }
        ]
    }
    
    #try: 
    fig = go.Figure()
    
    range_x=[0, 500]
    range_y=[0,100]
    # Calculate sizeref dynamically based on the plot dimensions
    plot_width = range_x[1] - range_x[0]
    plot_height = range_y[1] - range_y[0]
    sizeref = 2.0 * max(plot_width, plot_height) / (100 ** 2)  # Adjust the denominator for scaling
    
    np.random.seed(100)
    N = len(canteiro_data["plantas"])
    colors = np.random.rand(N)
        
    x=[]
    y=[]
    sz = []
    
    for planta in canteiro_data["plantas"]:

        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode="markers",
            marker=go.scatter.Marker(
                size=sz,
                sizemode="diameter",
                sizeref=1,
                color=colors,
                opacity=0.6,
                colorscale="Viridis"
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
    # Update marker sizes using update_traces()
    fig.update_traces(
        marker=dict(
            sizeref=1
        )
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
    json_str = fig.to_json()
    
    print("json_str: ", len(json_str))
    
    canteiro = Canteiro(
        nome_canteiro='cantieroTest1',
        svg_canteiro=fig_data
    )
    logger.debug(f"Criado canteiro de nome: '{canteiro.nome_canteiro}'")
    return jsonify(apresenta_canteiro(canteiro)), 200
    
    #except Exception as e:
    #    # caso um erro fora do previsto
    #    error_msg = "Não foi possível gerar o Canteiro"
    #    logger.warning(f"Erro ao gerar o canteiro, {error_msg}")
    #    return jsonify({
    #        "error": error_msg,
    #        "status": "failed"
    #    }), 500
    
if __name__ == '__main__':
    app.run(debug=True)