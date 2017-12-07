drop table if exists accounts;
create table accounts (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);

drop table if exists apis;
create table apis (
    id integer primary key autoincrement,
    account_id integer,
    exchange text not null,
    key text not null,
    secret text not null,
    phrase text not null
);
