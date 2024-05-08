CREATE DATABASE IF NOT EXISTS vault_database;
USE vault_database;

CREATE TABLE IF NOT EXISTS category(
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS produto(
    code INT NOT NULL,
    name varchar(255) NOT NULL,
    stock INT NOT NULL,
    value FLOAT NOT NULL,
    id_category INT NULL,
    PRIMARY KEY(code),
    FOREIGN KEY(id_category) REFERENCES category(id)
);