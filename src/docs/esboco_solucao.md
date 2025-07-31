## Solução para o Desafio Técnico – Engenharia de Dados

1. Entendimento do Problema
O desafio está dividido em duas partes:

A partir de um JSON contendo um pedido com apenas uma linha (por exemplo: "Torta de Maracujá"), modelar esse pedido em um banco relacional, considerando a escalabilidade para uma rede de restaurantes. A modelagem deve permitir pedidos com múltiplos itens e múltiplas lojas.

Integrar com uma API contendo 5 endpoints, que fornecem informações financeiras e operacionais da rede de restaurantes, para que essas informações alimentem um data lake estruturado e consultável.

2. Estratégia de Solução
Dividi a resolução em etapas:

- Análise do JSON.

- Modelagem das tabelas SQL.

- Simulação com 5 endpoints, cujo método é POST; um exemplo é fornecido.

- Ingestão dos dados no data lake (camada raw).

