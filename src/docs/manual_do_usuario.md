# Manual de Usuário

## Descrição do Projeto:

Este projeto tem como objetivo realizar a injeção de arquivos no banco de dados após testes com 5 endpoints que simulam respostas de APIs.

As principais etapas incluem:

Geração de arquivos JSON com base em uma hierarquia pré-definida;
Criação automática das tabelas no MySQL;
Testes de integração com os dados injetados no banco.


## Tecnologias:
- Python
- Mysql

## Instalações e Execução do Projeto:

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

E para inserir no banco mysql 

python ingestao_mock_mysql.py

Para salvar os registros no banco

python src\desafio02\ingestao_mock_mysql.py

``````

## Observações:

Para a utilização de testes com a criação das tabelas pode ser executado o script 
script_banco que está disponível no repositário dentro da pasta do desafio02. Que já realiza a crição do banco com as tabelas.

## Arquitetura / Estrutura do Projeto:

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

## Testes:

Para os testes executar dentro do projeto principal executar o comando pytest dentro do repositório principal.

``````
pytest
``````

``````
pytest -v
``````

## Melhorias e Futuras implementações:

Criação de uma DAG no Apache Airflow para agendamento do pipeline (opcional);

Implementação de CI/CD com GitHub Actions para:

- Executar testes automatizados a cada push;

- Validar o schema do banco e pipelines;

- Publicar imagens Docker para facilitar deploy.

## Autores e Contato:

Projeto criado por Vanessa Formiga