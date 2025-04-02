from flask import redirect, jsonify, request
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from logger import logger

from model import Session, Canteiro
from schemas import *


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
    
@app.post('/canteiro', tags=[canteiro_tag],
         responses={"200": CanteiroSchema, "404": ErrorSchema})
def get_canteiro():
    """
    Retorna uma representação do Canteiro.
    """
    logger.debug(f"Criando Canteiro")
    
    #try: 
    
    """Debugging endpoint"""
    logger.debug(f"Raw received data: {request.get_json()}")
    
    raw_data = request.get_json()
    query = CanteiroSchema.parse_obj(raw_data)
    print("✅ Raw JSON:", raw_data)
    print("🔄 Parsed Schema:", query.dict())
    canteiro = Canteiro(
        nome_canteiro=query.nome_canteiro,
        x_canteiro=query.x_canteiro,
        y_canteiro=query.y_canteiro,
        plantas_canteiro=query.plantas_canteiro
    )
    
    canteiro.distribuir_plantas()
    canteiro.criar_grafico()
    logger.debug(f"Criado canteiro de nome: '{canteiro.nome_canteiro}'")
    #print(apresenta_canteiro(canteiro))
    return jsonify(canteiro.plantas_canteiro), 200
    
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