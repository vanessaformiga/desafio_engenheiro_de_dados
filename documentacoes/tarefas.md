# Cronograma

- Definir a solução
- Implementar a solução
- Fazer os testes
- Coloca o docker
- E talvez a implementação do airflow

# Cronograma Técnico — Desafio Engenharia de Dados Coco Bambu

## ✅ Fase 1 — Definir a Solução

**Objetivo:** Entender o desafio, analisar o JSON e criar o plano técnico.

- [ ]  Analisar o `ERP.json` e mapear entidades e relacionamentos
- [ ]  Modelar o banco de dados relacional (diagrama ER)
- [ ]  Planejar a estrutura de diretórios do Data Lake
- [ ]  Listar os pontos que serão documentados no README



## 💻 Fase 2 — Implementar a Solução

**Objetivo:** Codificar os scripts e estrutura conforme o planejado.

- [ ]  Criar o script SQL com todas as tabelas (`modelo-relacional.sql`)
- [ ]  Criar script Python para simular chamadas às 5 APIs
- [ ]  Armazenar as respostas mockadas na estrutura de pastas do Data Lake
- [ ]  Documentar todas as decisões no `README.md`


## 🧪 Fase 3 — Testes

**Objetivo:** Verificar se o modelo e os scripts funcionam corretamente.

- [ ]  Validar o schema SQL com dados fictícios
- [ ]  Testar ingestão e armazenamento das respostas simuladas
- [ ]  Verificar se a estrutura permite consultas e versionamento


## 🐳 Fase 4 — Dockerização

**Objetivo:** Criar um ambiente isolado e replicável.

- [ ]  Criar `Dockerfile` com Python + dependências
- [ ]  Criar `docker-compose.yml` com banco (MySQL/Postgres) + volume para o data lake
- [ ]  Adicionar instruções de uso no `README.md`

---

## ⚙️ Fase 5 — (Opcional) Airflow

**Objetivo:** Automatizar a ingestão de dados no data lake.

- [ ]  Criar DAG simples para consumir as APIs mockadas
- [ ]  Salvar os arquivos no data lake com estrutura de partição
- [ ]  Documentar como rodar e visualizar a DAG no Airflow

## Fase 6 — Ajustes Finais e Entrega

- [ ]  Revisar a estrutura do repositório (nomes de arquivos, organização, README)
- [ ]  Garantir que todos os arquivos estejam comitadinhos e o README esteja completo
- [ ]  Testar o clone e execução do projeto em um novo ambiente (ideal com Docker)
- [ ]  Escrever e revisar o e-mail de entrega
- [ ]  Enviar para `lab@cocobambu.com` com o assunto **Desafio Engenharia Dados Coco Bambu 2025** e o link do repositório