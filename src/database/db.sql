CREATE DATABASE IF NOT EXISTS vault_database;
USE vault_database;

CREATE TABLE IF NOT EXISTS category(
    id tinyint NOT NULL,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS produto(
    code INT(4) UNSIGNED ZEROFILL NOT NULL,
    name VARCHAR(100) NOT NULL,
    stock VARCHAR(55) NOT NULL,
    value FLOAT NOT NULL,
    id_category tinyint NULL,
    PRIMARY KEY(code),
    FOREIGN KEY(id_category) REFERENCES category(id)
);