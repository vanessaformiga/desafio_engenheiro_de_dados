-- Tabela store
CREATE TABLE store (
  id_store INT PRIMARY KEY,
  loc_ref VARCHAR(50) UNIQUE NOT NULL
);

-- Tabela guest_check
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

-- Tabela detail_line
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

-- Tabela menu_item
CREATE TABLE menu_item (
  id_menu_item INT PRIMARY KEY,
  detail_line_id INT NOT NULL REFERENCES detail_line(id_detail_line),
  mi_num INT,
  mod_flag BOOLEAN,
  incl_tax NUMERIC(10,2),
  prc_lvl INT,
  active_taxes VARCHAR(20)
);

-- Tabela tax
CREATE TABLE tax (
  id_tax SERIAL PRIMARY KEY,
  guest_check_id INT NOT NULL REFERENCES guest_check(id_guest_check),
  tax_num INT,
  txbl_sls_ttl NUMERIC(10,2),
  tax_coll_ttl NUMERIC(10,2),
  tax_rate NUMERIC(5,4),
  type INT
);