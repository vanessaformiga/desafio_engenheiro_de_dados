CREATE TABLE store (
  id_store INT PRIMARY KEY AUTO_INCREMENT,
  loc_ref VARCHAR(50) UNIQUE NOT NULL
) ENGINE=InnoDB;

-- Tabela guest_check
CREATE TABLE guest_check (
  id_guest_check INT PRIMARY KEY,
  store_id INT NOT NULL,
  chk_num INT,
  opn_bus_dt DATE,
  opn_utc DATETIME,
  clsd_bus_dt DATE,
  clsd_utc DATETIME,
  gst_cnt INT,
  sub_ttl DECIMAL(10,2),
  chk_ttl DECIMAL(10,2),
  dsc_ttl DECIMAL(10,2),
  pay_ttl DECIMAL(10,2),
  bal_due_ttl DECIMAL(10,2),
  tbl_num INT,
  tbl_name VARCHAR(50),
  emp_num INT,
  clsd_flag TINYINT(1),
  FOREIGN KEY (store_id) REFERENCES store(id_store)
) ENGINE=InnoDB;

-- Tabela detail_line
CREATE TABLE detail_line (
  id_detail_line INT PRIMARY KEY,
  guest_check_id INT NOT NULL,
  line_num INT,
  dtl_id INT,
  detail_utc DATETIME,
  bus_dt DATE,
  dsp_ttl DECIMAL(10,2),
  dsp_qty DECIMAL(10,2),
  agg_ttl DECIMAL(10,2),
  agg_qty DECIMAL(10,2),
  seat_num INT,
  svc_rnd_num INT,
  FOREIGN KEY (guest_check_id) REFERENCES guest_check(id_guest_check)
) ENGINE=InnoDB;

-- Tabela menu_item
CREATE TABLE menu_item (
  id_menu_item INT PRIMARY KEY AUTO_INCREMENT,
  detail_line_id INT NOT NULL,
  mi_num INT,
  mod_flag TINYINT(1),
  incl_tax DECIMAL(10,2),
  prc_lvl INT,
  active_taxes VARCHAR(20),
  FOREIGN KEY (detail_line_id) REFERENCES detail_line(id_detail_line)
) ENGINE=InnoDB;

-- Tabela tax
CREATE TABLE tax (
  id_tax INT PRIMARY KEY AUTO_INCREMENT,
  guest_check_id INT NOT NULL,
  tax_num INT,
  txbl_sls_ttl DECIMAL(10,2),
  tax_coll_ttl DECIMAL(10,2),
  tax_rate DECIMAL(5,4),
  type INT,
  FOREIGN KEY (guest_check_id) REFERENCES guest_check(id_guest_check)
) ENGINE=InnoDB;