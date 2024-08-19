DROP DATABASE IF EXISTS `exemplo_db`;

CREATE DATABASE  `exemplo_db`;

USE `exemplo_db`;

create table if not exists `clientes` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `nome` varchar(255) NOT NULL,
    `email` varchar(255) NOT NULL,
    `cpf` varchar(11) NOT NULL,
    PRIMARY KEY (`id`)
);

insert into `clientes` (`nome`, `email`, `cpf`) values ("João", "joao@joao", "11111111111");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Maria", "maria@maria", "22222222222");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Pedro", "pedro@pedro", "33333333333");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Ana", "ana@ana", "44444444444");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Carlos", "carlos@carlos", "55555555555");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Lucas", "lucas@lucas", "66666666666");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Julia", "julia@julia", "77777777777");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Bruno", "bruno@bruno", "88888888888");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Vitor", "vitor@vitor", "99999999999");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Luciana", "luciana@luciana", "10101010101");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Bruna", "bruna@bruna", "11111111111");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Lucas", "lucas@lucas", "12121212121");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Juliana", "juliana@juliana", "13131313131");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Bruno", "bruno@bruno", "14141414141");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Vitoria", "vitoria@vitoria", "15151515151");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Lucas", "lucas@lucas", "16161616161");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Juliana", "juliana@juliana", "17171717171");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Bruno", "bruno@bruno", "18181818181");
insert into `clientes` (`nome`, `email`, `cpf`) values ("Vitoria", "vitoria@vitoria", "19191919191");