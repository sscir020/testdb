drop table if exists items;
create table items(
        item_id int not null auto_increment,
        item_name varchar(32) not null,
        num int not null default 0,
        comment varchar(20) default '',
        primary key(item_id),
        unique(item_name)
);