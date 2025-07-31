-- MySQL Script ajustado com nomes de constraints e NOT NULL em IDs
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `mydb`;

CREATE TABLE IF NOT EXISTS `store` (
  `id_store` INT NOT NULL AUTO_INCREMENT,
  `loc_ref` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id_store`),
  UNIQUE KEY `uk_store_loc_ref` (`loc_ref`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `guest_check` (
  `id_guest_check` INT NOT NULL,
  `store_id` INT NOT NULL,
  `chk_num` INT NULL DEFAULT NULL,
  `opn_bus_dt` DATE NULL DEFAULT NULL,
  `opn_utc` DATETIME NULL DEFAULT NULL,
  `clsd_bus_dt` DATE NULL DEFAULT NULL,
  `clsd_utc` DATETIME NULL DEFAULT NULL,
  `gst_cnt` INT NULL DEFAULT NULL,
  `sub_ttl` DECIMAL(10,2) NULL DEFAULT NULL,
  `chk_ttl` DECIMAL(10,2) NULL DEFAULT NULL,
  `dsc_ttl` DECIMAL(10,2) NULL DEFAULT NULL,
  `pay_ttl` DECIMAL(10,2) NULL DEFAULT NULL,
  `bal_due_ttl` DECIMAL(10,2) NULL DEFAULT NULL,
  `tbl_num` INT NULL DEFAULT NULL,
  `tbl_name` VARCHAR(50) NULL DEFAULT NULL,
  `emp_num` INT NULL DEFAULT NULL,
  `clsd_flag` TINYINT(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id_guest_check`),
  KEY `fk_guest_check_store_idx` (`store_id`),
  CONSTRAINT `fk_guest_check_store` FOREIGN KEY (`store_id`) REFERENCES `store` (`id_store`)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `detail_line` (
  `id_detail_line` INT NOT NULL,
  `guest_check_id` INT NOT NULL,
  `line_num` INT NULL DEFAULT NULL,
  `dtl_id` INT NULL DEFAULT NULL,
  `detail_utc` DATETIME NULL DEFAULT NULL,
  `bus_dt` DATE NULL DEFAULT NULL,
  `dsp_ttl` DECIMAL(10,2) NULL DEFAULT NULL,
  `dsp_qty` DECIMAL(10,2) NULL DEFAULT NULL,
  `agg_ttl` DECIMAL(10,2) NULL DEFAULT NULL,
  `agg_qty` DECIMAL(10,2) NULL DEFAULT NULL,
  `seat_num` INT NULL DEFAULT NULL,
  `svc_rnd_num` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_detail_line`),
  KEY `fk_detail_line_guest_check_idx` (`guest_check_id`),
  CONSTRAINT `fk_detail_line_guest_check` FOREIGN KEY (`guest_check_id`) REFERENCES `guest_check` (`id_guest_check`)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `menu_item` (
  `id_menu_item` INT NOT NULL AUTO_INCREMENT,
  `detail_line_id` INT NOT NULL,
  `mi_num` INT NULL DEFAULT NULL,
  `mod_flag` TINYINT(1) NULL DEFAULT NULL,
  `incl_tax` DECIMAL(10,2) NULL DEFAULT NULL,
  `prc_lvl` INT NULL DEFAULT NULL,
  `active_taxes` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id_menu_item`),
  KEY `fk_menu_item_detail_line_idx` (`detail_line_id`),
  CONSTRAINT `fk_menu_item_detail_line` FOREIGN KEY (`detail_line_id`) REFERENCES `detail_line` (`id_detail_line`)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `tax` (
  `id_tax` INT NOT NULL AUTO_INCREMENT,
  `guest_check_id` INT NOT NULL,
  `tax_num` INT NULL DEFAULT NULL,
  `txbl_sls_ttl` DECIMAL(10,2) NULL DEFAULT NULL,
  `tax_coll_ttl` DECIMAL(10,2) NULL DEFAULT NULL,
  `tax_rate` DECIMAL(5,4) NULL DEFAULT NULL,
  `type` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_tax`),
  KEY `fk_tax_guest_check_idx` (`guest_check_id`),
  CONSTRAINT `fk_tax_guest_check` FOREIGN KEY (`guest_check_id`) REFERENCES `guest_check` (`id_guest_check`)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
