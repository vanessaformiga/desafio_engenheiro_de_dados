# Descreva a abordagem escolhida em detalhes

## A abordagem escolhida

Com a análise do arquivo `ERP.json`, foi possível identificar e considerar as principais entidades e seus respectivos relacionamentos. Dessa forma, foram escolhidas as entidades `store`, `guest_check`, `detail_line`, `menu_item` e `tax`.

Porém, durante algumas análises, foi identificado que poderia ser criada uma entidade `guest_check_tax`, para que seja realizada uma avaliação ou uma análise mais ampla dos impostos que um produto pode ter, ou para fazer uma divisão dos impostos que um produto possui. Entretanto, neste momento, foi identificado que essa entidade e seu respectivo relacionamento não serão incluídos. Contudo, caso seja necessária a ampliação das análises em relação aos impostos, poderá ser feita a inclusão da mesma.

Também foi analisado, a partir do arquivo `ERP.json`, que não estão apresentados os campos `discount`, por exemplo. Por esse motivo, e pela necessidade de apresentar uma abordagem mais simples, optou-se por não inserir uma entidade cujo nome se relaciona com `discount` e que teria um relacionamento com a entidade `detailLines`.