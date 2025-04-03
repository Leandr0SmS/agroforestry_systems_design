from pydantic import BaseModel
#from typing import Optional, List
from model.canteiro import Canteiro


class CanteiroSchema(BaseModel):
    """ Define como um novo canteiro deve ser representado
    """
    nome_canteiro: str = "Canteiro1"
    x_canteiro: int = 800
    y_canteiro: int = 200
    plantas_canteiro: dict = {
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


# class PlantaDelSchema(BaseModel):
#     """ Define como deve ser a estrutura do dado retornado após uma requisição
#         de remoção.
#     """
#     mesage: str
#     nome_planta: str
#     
# class PlantaUpdateSchema(BaseModel):
#     """ Define como uma nova planta a ser editada deve ser representada
#     """
#     nome_planta: str = "Bananeira Prata"
#     tempo_colheita: Optional[int] = 300
#     estrato: Optional[str] = "medio"
#     espacamento: Optional[float] = 2
#     
#     
# class ListagemPlantasSchema(BaseModel):
#     """ Define como uma listagem das plantas será retornada.
#     """
#     plantas:List[PlantaSchema]
# 
# 
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

