**Etapas da Modelagem Relacional**

A partir da estrutura do arquivo do ERP.json, podemos identificar:

Descrição das entidades

store.localRef - unidade do restaurante

guestCheck - pedido realizado

detailLines - item do pdido

taxes - impostos aplicados

As principais entidades separadas terão em suas ligações através do relacionamentos as chaves primárias e a depender do relacionamento as estrangeiras.

Modelagem Relacional com Chaves

**Tabela store**

CREATE TABLE store (
  id_store INT PRIMARY KEY,
  loc_ref VARCHAR(50) UNIQUE NOT NULL
);

Armazena as informações referentes a unidade

Descrição dos Campos:

id_store: Identificador único da unidade 

loc_ref: Referência da localização da unidade, como código ou nome interno.



**Tabela guest_check**

CREATE TABLE guest_check (
  id_guest_check INT PRIMARY KEY,
  store_id INT NOT NULL REFERENCES store(id_store),
  chk_num INT,
  opn_bus_dt DATE,
  opn_utc TIMESTAMP,
  clsd_bus_dt DATE,
  clsd_utc TIMESTAMP,
  gst_cnt INT,
  sub_ttl NUMERIC(10,2),
  chk_ttl NUMERIC(10,2),
  dsc_ttl NUMERIC(10,2),
  pay_ttl NUMERIC(10,2),
  bal_due_ttl NUMERIC(10,2),
  tbl_num INT,
  tbl_name VARCHAR(50),
  emp_num INT,
  clsd_flag BOOLEAN
);

Terá a chave estrangeira referente a unidade o id da unidade

Descrição dos Campos:

id_guest_check: Identificador do pedido (comanda).

store_id: Unidade onde o pedido foi feito (chave estrangeira para store).

chk_num: Número da comanda.

opn_bus_dt / clsd_bus_dt: Datas de abertura e fechamento da comanda (formato de negócios).

opn_utc / clsd_utc: Datas de abertura e fechamento em UTC (para auditoria).

gst_cnt: Número de clientes na mesa.

sub_ttl: Subtotal sem descontos ou impostos.

chk_ttl: Valor total da comanda.

dsc_ttl: Total de descontos aplicados.

pay_ttl: Valor total pago.

bal_due_ttl: Saldo restante a pagar.

tbl_num: Número da mesa.

tbl_name: Nome da mesa (se aplicável).

emp_num: Número do colaborador que atendeu.

clsd_flag: Indicador se a comanda foi encerrada.


**Tabela detaill_line**

CREATE TABLE detail_line (
  id_detail_line INT PRIMARY KEY,
  guest_check_id INT NOT NULL REFERENCES guest_check(id_guest_check),
  line_num INT,
  dtl_id INT,
  detail_utc TIMESTAMP,
  bus_dt DATE,
  dsp_ttl NUMERIC(10,2),
  dsp_qty NUMERIC(10,2),
  agg_ttl NUMERIC(10,2),
  agg_qty NUMERIC(10,2),
  seat_num INT,
  svc_rnd_num INT
);

Terá a chave a estrangeira referente ao pedido da comanda

Descrição dos Campos:

id_detail_line: Identificador da linha de item.

guest_check_id: Identificador do pedido ao qual o item pertence.

line_num: Número da linha no pedido.

dtl_id: Identificador detalhado do item no sistema.

detail_utc: Data e hora da inclusão da linha.

bus_dt: Data do movimento (negócio).

dsp_ttl: Total exibido para o item.

dsp_qty: Quantidade exibida.

agg_ttl: Total agregado de valores (por exemplo, combinando promoções).

agg_qty: Quantidade agregada.

seat_num: Número do assento do cliente (se o sistema controlar por assento).

svc_rnd_num: Número do serviço ou rodada (caso haja controle de rodadas).

**Tabela menu_item**

CREATE TABLE menu_item (
  id_menu_item INT PRIMARY KEY,
  detail_line_id INT NOT NULL REFERENCES detail_line(id_detail_line),
  mi_num INT,
  mod_flag BOOLEAN,
  incl_tax NUMERIC(10,2),
  prc_lvl INT,
  active_taxes VARCHAR(20)
);


Terá a chave a chave estrangeira referente ao detail_line

Descrição dos Campos:

id_menu_item: Identificador único do item de menu.

detail_line_id: Linha do pedido em que o item foi solicitado.

mi_num: Código do item no cardápio.

mod_flag: Indica se o item foi modificado (ex: sem cebola).

incl_tax: Valor de imposto incluso no preço.

prc_lvl: Nível de precificação (pode variar conforme o horário ou campanha).

active_taxes: Identificação dos impostos ativos aplicados.

**Tabela tax**

CREATE TABLE tax (
  id_tax SERIAL PRIMARY KEY,
  guest_check_id INT NOT NULL REFERENCES guest_check(id_guest_check),
  tax_num INT,
  txbl_sls_ttl NUMERIC(10,2),
  tax_coll_ttl NUMERIC(10,2),
  tax_rate NUMERIC(5,4),
  type INT
);

Terá a chave estrangeira estrangeira referente ao item da pedido

id_tax: Identificador do imposto aplicado.

guest_check_id: Comanda associada ao imposto.

tax_num: Código do tipo de imposto.

txbl_sls_ttl: Valor total sobre o qual o imposto foi calculado.

tax_coll_ttl: Valor total de imposto recolhido.

tax_rate: Taxa de imposto aplicada.

type: Tipo de imposto (ex: estadual, municipal).



### Relacionamentos

store (1) ───< guest_check (N)
guest_check (1) ───< detail_line (N)
detail_line (1) ───< menu_item (1)
guest_check (1) ───< tax (N)

### **Justificativa da Modelagem**

Normalização: A estrutura das tabelas serão utilizadas a 3ª Forma Normal (3FN), separando as entidades em tabelas destintas

Chaves estrangeiras - para garantir a integridade dos item e no relacionamento entre pedidos e item

Uma unidade store - referente a unidade caso ocorra a expansão de outras unidades

Relacionamento: O gueck_check pode ter vários detail_lines e taxes, porém cada detail_line terá somente um menu_item

## Mapeamento JSON → SQL

| JSON (exemplo) | Tabela SQL | Campo SQL | Observação |
| --- | --- | --- | --- |
| `"locRef": "99 CB CB"` | `store` | `loc_ref` | Código/identificador da unidade |
| `"guestChecks"` (array) | `guest_check` | --- | Cada objeto é um registro |
| `"guestCheckId": 1122334455` | `guest_check` | `id_guest_check` | ID do pedido (comanda) |
| `"chkNum": 1234` | `guest_check` | `chk_num` | Número da comanda |
| `"opnBusDt": "2024-01-01"` | `guest_check` | `opn_bus_dt` | Data de abertura (negócio) |
| `"opnUTC": "2024-01-01T09:09:09"` | `guest_check` | `opn_utc` | Data/hora abertura UTC |
| `"clsdBusDt": "2024-01-01"` | `guest_check` | `clsd_bus_dt` | Data fechamento (negócio) |
| `"clsdUTC": "2024-01-01T12:12:12"` | `guest_check` | `clsd_utc` | Data/hora fechamento UTC |
| `"gstCnt": 1` | `guest_check` | `gst_cnt` | Número de clientes |
| `"subTtl": 109.9` | `guest_check` | `sub_ttl` | Subtotal |
| `"chkTtl": 109.9` | `guest_check` | `chk_ttl` | Total da comanda |
| `"dscTtl": -10` | `guest_check` | `dsc_ttl` | Total descontos |
| `"payTtl": 109.9` | `guest_check` | `pay_ttl` | Total pago |
| `"tblNum": 1` | `guest_check` | `tbl_num` | Número da mesa |
| `"tblName": "90"` | `guest_check` | `tbl_name` | Nome da mesa |
| `"empNum": 55555` | `guest_check` | `emp_num` | Número do funcionário |
| `"clsdFlag": true` | `guest_check` | `clsd_flag` | Indicador se comanda está fechada |

### Detail Lines (Itens do pedido)

| JSON Detail Line | Tabela SQL | Campo SQL | Observação |
| --- | --- | --- | --- |
| `"guestCheckLineItemId": 9988776655` | `detail_line` | `id_detail_line` | ID da linha do pedido |
| `"guestCheckId"` (pai) | `detail_line` | `guest_check_id` | FK para a comanda |
| `"lineNum": 1` | `detail_line` | `line_num` | Número da linha no pedido |
| `"dtlId": 1` | `detail_line` | `dtl_id` | ID detalhado do item |
| `"detailUTC": "2024-01-01T09:09:09"` | `detail_line` | `detail_utc` | Data/hora do item |
| `"busDt": "2024-01-01"` | `detail_line` | `bus_dt` | Data negócio |
| `"dspTtl": 119.9` | `detail_line` | `dsp_ttl` | Total exibido do item |
| `"dspQty": 1` | `detail_line` | `dsp_qty` | Quantidade exibida |
| `"aggTtl": 119.9` | `detail_line` | `agg_ttl` | Total agregado |
| `"aggQty": 1` | `detail_line` | `agg_qty` | Quantidade agregada |
| `"seatNum": 1` | `detail_line` | `seat_num` | Número do assento |
| `"svcRndNum": 1` | `detail_line` | `svc_rnd_num` | Número da rodada de serviço |

### Menu Item (Detalhes do item de menu)

| JSON Menu Item | Tabela SQL | Campo SQL | Observação |
| --- | --- | --- | --- |
| `"miNum": 6042` | `menu_item` | `mi_num` | Código do item no cardápio |
| `"modFlag": false` | `menu_item` | `mod_flag` | Indica modificação no item |
| `"inclTax": 20.809091` | `menu_item` | `incl_tax` | Valor do imposto incluído |
| `"prcLvl": 3` | `menu_item` | `prc_lvl` | Nível de precificação |
| `"activeTaxes": "28"` | `menu_item` | `active_taxes` | Lista/IDs dos impostos ativos |
| `"guestCheckLineItemId"` (pai) | `menu_item` | `detail_line_id` | FK para a linha de detalhe |

### Taxes (Impostos)

| JSON Tax (dentro de guestCheck) | Tabela SQL | Campo SQL | Observação |
| --- | --- | --- | --- |
| `"taxNum": 28` | `tax` | `tax_num` | Código do imposto |
| `"txblSlsTtl": 119.9` | `tax` | `txbl_sls_ttl` | Base tributável |
| `"taxCollTtl": 20.81` | `tax` | `tax_coll_ttl` | Valor do imposto recolhido |
| `"taxRate": 21` | `tax` | `tax_rate` | Percentual da taxa |
| `"type": 3` | `tax` | `type` | Tipo de imposto (classificação) |
| `guestCheckId` (pai) | `tax` | `guest_check_id` | FK para a comanda |