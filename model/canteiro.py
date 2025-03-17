from sqlalchemy import Column, String, Integer#, ForeignKey

from  model import Base


class Canteiro(Base):
    __tablename__ = 'canteiros'

    id_canteiro = Column(Integer, primary_key=True)
    nome_canteiro = Column(String(140), unique=True, nullable=False)
    svg_canteiro = Column(String(140), nullable=False)
    

    ### Definição de ForeignKey da tabela estrato.
    ##estrato = Column(String(50), ForeignKey("estrato.nome_estrato"), nullable=False)

    def __init__(self, nome_canteiro:str, svg_canteiro:str):
        """
        Cria um Canteiro

        Arguments:
            nome_canteiro: O nome da canteiro;
            svg_canteiro: Svg Json do canteiro;
        """
        self.nome_canteiro = nome_canteiro
        self.svg_canteiro = svg_canteiro
        
    def __repr__(self):
        return f'Canteiro("{self.nome_canteiro}","{self.svg_canteiro}")'
