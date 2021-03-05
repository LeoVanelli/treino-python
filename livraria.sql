DROP DATABASE IF EXISTS livraria;
create database livraria;
use livraria;

CREATE TABLE pessoas (
    id_pessoa SMALLINT(5) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(80),
    idade INT(2),
    cpf BIGINT(11) NOT NULL,
    cep VARCHAR(20)
);

CREATE TABLE livros (
    id_livro SMALLINT(5) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(80),
    genero VARCHAR(50),
    preco REAL
);

CREATE TABLE funcionarios (
    nome VARCHAR(80),
    cargo VARCHAR(30),
    cpf BIGINT(11) PRIMARY KEY NOT NULL
);

insert into pessoas(nome,idade,cpf,cep)
 values('Leandro','19','35456317885','11730-000');
insert into funcionarios(nome,cargo,cpf)
 values('George','Vendedor','12345678912');
insert into funcionarios(nome,cargo,cpf)
 values('Betânia','Caixa','98765432112');