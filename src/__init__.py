"""
Pacote principal do projeto.

Este módulo define configurações básicas, versão do pacote
e torna alguns submódulos disponíveis diretamente ao importar `src`.
"""

__version__ = "0.1.0"


__all__ = [
    
]


import logging

logger = logging.getLogger(__name__)
if not logger.handlers:
   
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

logger.info("Pacote src carregado com sucesso!")