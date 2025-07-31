### Como você armazenaria os dados? Crie uma estrutura de pastas capaz de armazenar as srespostas da API. Ela deve permitir manipulação, verificações, buscas e pesquisas rápidas.  

Para armazenar as respostas das APIs de forma organizada, eficiente e que permita fácil manipulação, verificações e buscas rápidas, sugiro a seguinte estrutura de pastas:

``````
data_lake/
│
├── raw/
├── schemas/
├── metadata/
├── logs/
└── processed/
``````

raw - Contém os dados brutos coletados das APIs, sistemas externos ou arquivos importados,
│   sem qualquer modificação. Cada fonte pode ter uma subpasta identificando a origem
│   ou a data da ingestão.

schemas - Serve para garantir padronização e validação dos dados ingeridos.

metadatas - Contém arquivos de metadados sobre os datasets, como data de extração, versão do arquivo,
status da carga, histórico de transformações ou dicionário de dados.

logs - Guarda arquivos de log das execuções dos pipelines de ingestão e processamento.

processed - Contém os dados já tratados, limpos e estruturados, prontos para consumo
por relatórios, análises ou cargas em Data Warehouse.