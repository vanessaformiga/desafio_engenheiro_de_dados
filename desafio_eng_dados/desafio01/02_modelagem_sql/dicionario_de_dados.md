Tabela: store
Campo	Tipo	Descrição
id_store	INT	Identificador único da loja (PK)
loc_ref	VARCHAR(50)	Referência/código da unidade (único)

Tabela: guest_check
Campo	Tipo	Descrição
id_guest_check	INT	Identificador único da comanda (PK)
store_id	INT	Referência à loja (FK → store.id_store)
chk_num	INT	Número da comanda
opn_bus_dt	DATE	Data de abertura da comanda
opn_utc	DATETIME	Timestamp UTC de abertura
clsd_bus_dt	DATE	Data de fechamento da comanda
clsd_utc	DATETIME	Timestamp UTC de fechamento
gst_cnt	INT	Quantidade de clientes na comanda
sub_ttl	DECIMAL(10,2)	Subtotal antes de descontos e taxas
chk_ttl	DECIMAL(10,2)	Total final da comanda
dsc_ttl	DECIMAL(10,2)	Total de descontos aplicados
pay_ttl	DECIMAL(10,2)	Total pago
bal_due_ttl	DECIMAL(10,2)	Saldo devedor restante
tbl_num	INT	Número da mesa
tbl_name	VARCHAR(50)	Nome/identificação da mesa
emp_num	INT	Número do funcionário responsável
clsd_flag	TINYINT(1)	Indicador se a comanda está fechada (0/1)

Tabela: detail_line
Campo	Tipo	Descrição
id_detail_line	INT	Identificador único da linha de detalhe (PK)
guest_check_id	INT	Referência à comanda (FK → guest_check.id_guest_check)
line_num	INT	Número da linha na comanda
dtl_id	INT	Identificador interno do detalhe
detail_utc	DATETIME	Timestamp UTC do detalhe
bus_dt	DATE	Data comercial da transação
dsp_ttl	DECIMAL(10,2)	Valor total exibido
dsp_qty	DECIMAL(10,2)	Quantidade exibida
agg_ttl	DECIMAL(10,2)	Valor agregado total
agg_qty	DECIMAL(10,2)	Quantidade agregada
seat_num	INT	Número do assento
svc_rnd_num	INT	Número de rodada de serviço (serviço por turno)

Tabela: menu_item
Campo	Tipo	Descrição
id_menu_item	INT	Identificador único do item do menu (PK)
detail_line_id	INT	Referência ao detalhe (FK → detail_line.id_detail_line)
mi_num	INT	Código do item do menu
mod_flag	TINYINT(1)	Indicador se houve modificação (0/1)
incl_tax	DECIMAL(10,2)	Valor de imposto incluído
prc_lvl	INT	Nível de preço aplicado
active_taxes	VARCHAR(20)	Identificação das taxas ativas

Tabela: tax
Campo	Tipo	Descrição
id_tax	INT	Identificador único do imposto (PK)
guest_check_id	INT	Referência à comanda (FK → guest_check.id_guest_check)
tax_num	INT	Número/código do imposto
txbl_sls_ttl	DECIMAL(10,2)	Total de vendas tributáveis
tax_coll_ttl	DECIMAL(10,2)	Total de impostos coletados
tax_rate	DECIMAL(5,4)	Alíquota do imposto aplicada
type	INT	Tipo de imposto (ex: 1 = municipal, 2 = estadual, etc.)