# Desafio Engenheiro de Dados

## Objetivo: 

O objetivo deste desafio é, a partir de um arquivo JSON contendo um pedido, criar as tabelas SQL necessárias e implementar uma API com 5 endpoints que sejam capazes de se comunicar com o data lake.


## Visão geral:

Esta aplicação tem como finalidade, a partir de um JSON fornecido, elaborar a modelagem das tabelas necessárias para a solução. A implementação será testada por meio de 5 endpoints responsáveis pela inserção dos dados, utilizando um script com dados mockados.


## Instalçôes e Execuções:

### Instalções:

``````
git clone https://github.com/vanessaformiga/desafio_engenheiro_de_dados

python -m venv venv

venv/Scripts/activate (windows)

source venv/bin/activate (linux)

pip install -r requirements.txt

pip freeze > requirements.txt
``````

### Execução:

Para a execução dos script:

Acesse a pasta 

``````
cd src 

Depois acesse a pasta desafio02

cd desafio02

E execute 

python ingestao_mock.py

Também pode executar somente o comando 

python src\desafio02\ingestao_mock.py

``````

### Bibliotecas Utilizadas:

- python
- mysql

## Estrutura das Pastas:

``````
DESAFIO_ENGENHEIRO_DE_DADOS/
│
├── src/
│   ├── desafio01/                 # Modelagem do JSON e SQL do primeiro desafio
│   ├── desafio02/                 # Scripts de ingestão e testes com endpoints
│   ├── docs/                      # Documentação adicional do projeto
│   └── __init__.py                # Torna o diretório src um pacote Python
│
├── tests/                         # Scripts de teste unitário e integração
│
├── venv/                          # Ambiente virtual Python (não subir para Git)
├── .env                           # Variáveis de ambiente (senha do MySQL, etc.)
├── .gitignore                     # Arquivos e pastas ignoradas pelo Git
├── kanbam.md                      # Kanban e planejamento do desafio
├── README.md                      # Manual principal do projeto
└── requirements.txt               # Dependências Python
``````


## Testes

Para os testes executar dentro do projeto principal executar

``````
pytest
``````

``````
pytest -v
``````

## Contato

- Projeto desenvolvido por Vanessa Formiga
- Contato vanessaformiga21@gmail.com
