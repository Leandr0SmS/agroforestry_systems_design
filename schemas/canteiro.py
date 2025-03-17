from pydantic import BaseModel
#from typing import Optional, List
from model.canteiro import Canteiro


class CanteiroSchema(BaseModel):
    """ Define como um novo canteiro deve ser representado
    """
    nome_canteiro: str = "Canteiro1"
    svg_canteiro: str = "<svg xmlns=\"http://www.w3.org/2000/svg\" ... </svg>"
 
    
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
    svg_canteiro: str = "<svg xmlns=\"http://www.w3.org/2000/svg\" ... </svg>"


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
        "svg_canteiro": canteiro.svg_canteiro
    }

