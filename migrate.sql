create table blogs2 (
    id serial8 not null,
    title character varying(128),
    pub_date character varying,
    author_id integer,
    category_id integer
);

insert into blogs2(id, title, pub_date, author_id, category_id) select id, title, pub_date, author_id, category_id from blogs;

alter table blogs add column pub_date2 timestamp NULL;
update blogs set pub_date2=to_timestamp(pub_date, 'YYYY-MM-DD HH:MI:SS');
alter table blogs drop column pub_date;
alter table blogs rename column pub_date2 to pub_date;
