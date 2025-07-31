"""
Pacote realizado para os test.

Módulo utilizado para testar a aplicação.
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

logger.info("Pacote tests carregado com sucesso!")