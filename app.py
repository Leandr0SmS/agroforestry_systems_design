from flask import redirect, jsonify, request
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from logger import logger

from sqlalchemy.exc import IntegrityError

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
def get_canteiro(form: CanteiroSchema):
    """
    Retorna uma representação do Canteiro.
    """
    logger.debug(f"Criando Canteiro")
    
    try: 

        raw_data = request.get_json()
        query = CanteiroSchema.model_validate(raw_data)
        logger.debug(f"Criado canteiro de nome: '{query.nome_canteiro}'")
        canteiro = Canteiro(
            nome_canteiro=query.nome_canteiro,
            x_canteiro=query.x_canteiro,
            y_canteiro=query.y_canteiro,
            plantas_canteiro=query.plantas_canteiro
        )
        print({
            'nome_canteiro':query.nome_canteiro,
            'x_canteiro':query.x_canteiro,
            'y_canteiro':query.y_canteiro,
            'plantas_canteiro':query.plantas_canteiro
        })

        logger.debug(f"Adicionando canteiro de nome: '{canteiro.nome_canteiro}'")
        try:
            # criando conexão com a base
            with Session() as session:
                # adicionando canteiro
                session.add(canteiro)
                session.commit()
                logger.debug(f"Adicionado canteiro de nome: '{canteiro.nome_canteiro}'")

        except IntegrityError as e:
            # como a duplicidade do nome é a provável razão do IntegrityError
            error_msg = "Canteiro de mesmo nome já salvo na base :/"
            logger.warning(f"Erro ao adicionar canteiro '{canteiro.nome_canteiro}', {error_msg}")
            return {"mesage": error_msg}, 409
        
        except Exception as e:
            # caso um erro fora do previsto
            error_msg = "Não foi possível salvar novo canteiro :/"
            logger.warning(f"Erro ao adicionar planta '{canteiro.nome_canteiro}', {error_msg}")
            return {"mesage": error_msg}, 400

        # Destribuindo plantas pela area do canteiro
        logger.debug(f"Destribuindo plantas no canteiro: '{canteiro.nome_canteiro}'")
        canteiro.distribuir_plantas()
        return apresenta_canteiro(canteiro), 200
    
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível gerar o Canteiro"
        logger.warning(f"Erro ao gerar o canteiro, {error_msg}")
        return jsonify({
            "error": error_msg,
            "status": "failed"
        }), 500
    
if __name__ == '__main__':
    app.run(debug=True)