from pydantic import BaseModel
from typing import Optional, List
from model.canteiro import Canteiro

# Define nested schemas
class PlantaSchema(BaseModel):
    espacamento: int
    estrato: str
    nome_planta: str
    sombra: int
    tempo_colheita: int

class PlantasCanteiroSchema(BaseModel):
    plantas: List[PlantaSchema] =  [
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
        ]# Explicitly validate the list structure

class CanteiroSchema(BaseModel):
    """ Define como um novo canteiro deve ser representado
    """
    nome_canteiro: str = "Canteiro1"
    x_canteiro: int = 800
    y_canteiro: int = 200
    plantas_canteiro: PlantasCanteiroSchema  
    #dict = {
    #    "plantas": [
    #        {
    #          "espacamento": 200,
    #          "estrato": "emergente",
    #          "nome_planta": "Embaúba",
    #          "sombra": 20,
    #          "tempo_colheita": 1095
    #        },
    #        {
    #          "espacamento": 100,
    #          "estrato": "alto",
    #          "nome_planta": "Jucara",
    #          "sombra": 40,
    #          "tempo_colheita": 2555
    #        },
    #        {
    #          "espacamento": 50,
    #          "estrato": "medio",
    #          "nome_planta": "Pimenta-do-reino",
    #          "sombra": 60,
    #          "tempo_colheita": 1460
    #        },
    #        {
    #          "espacamento": 40,
    #          "estrato": "baixo",
    #          "nome_planta": "Abacaxi",
    #          "sombra": 80,
    #          "tempo_colheita": 730
    #        }
    #    ]
    #}
    
class CanteiroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do Canteiro.
    """
    nome_canteiro: str = "Canteiro1"


class CanteiroViewSchema(BaseModel):
    """ Define como um canteiro será retornado.
    """
    id_cantiero: int = 1
    nome_canteiro: str = "Canteiro1"

    
class CanteiroUpdateSchema(BaseModel):
    """ Define como um canteiro deve ser editado
    """
    nome_canteiro: str = "Canteiro1"
    x_canteiro: Optional[int] = 1100
    y_canteiro: Optional[int] = 250
    plantas_canteiro: Optional[dict] = {
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

class CanteiroDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome_canteiro: str
    
    
class ListagemCanteirosSchema(BaseModel):
    """ Define como uma listagem dos Canteiro será retornada.
    """
    plantas:List[CanteiroSchema]


def apresenta_canteiro(canteiro: Canteiro):
    """ Retorna uma representação de um canteiro seguindo o schema definido em
        CanteiroViewSchema.
    """
    return {
        "nome_canteiro": canteiro.nome_canteiro,
        "x_canteiro": canteiro.x_canteiro,
        "y_canteiro": canteiro.y_canteiro,
        "plantas_canteiro": canteiro.plantas_canteiro
    }

def apresenta_canteiros(canteiros: List[Canteiro]):
    """ Retorna uma representação de um canteiro seguindo o schema definido em
        CanteiroViewSchema.
    """
    result = []
    for canteiro in canteiros:
        result.append({
            "id_canteiro": canteiro.id_canteiro,
            "nome_canteiro": canteiro.nome_canteiro,
            "x_canteiro": canteiro.x_canteiro,
            "y_canteiro": canteiro.y_canteiro,
            "plantas_canteiro": canteiro.plantas_canteiro,
        })

    return {"canteiro": result}

