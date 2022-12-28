create user uhp@'localhost' identified by 'bRLu4XkT';
create database hp default character set utf8 collate utf8_general_ci;
grant all on hp.* to uhp@'localhost';

create table news (
id int(11) not null auto_increment,
title varchar(128),
content longtext,
date_up timestamp default current_timestamp,
primary key (id)
);
