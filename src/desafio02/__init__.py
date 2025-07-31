"""
Pacote desafio02

Este módulo faz parte do projeto de Engenharia de Dados.
Responsável por:
- Criação de banco e tabelas no MySQL
- Ingestão de arquivos JSON mockados
- Testes unitários e de integração
"""

__version__ = "1.0.0"
__author__ = "Vanessa Formiga"

# Imports principais para facilitar acesso externo
# from . import script_banco
# from . import ingestao_mock


__all__ = [
    
]


import logging

logger = logging.getLogger(__name__)
if not logger.handlers:
   
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

logger.info("Pacote desafio02 carregado com sucesso!")