drop table if exists py151120;
create table py040121 (id serial, tag varchar, val float);
delete from py040121 where val < 10;
create table py151120 (id serial, tag varchar, val float);
delete from py151120 where val < 10;
create table pyres040121 (id serial, tag varchar, val float);
delete from pyres040121 where val < 100;
create table pyres151120 (id serial, tag varchar, val float);
delete from pyres151120 where val < 100;
create table ds040121 (id serial, tag varchar, val float);
delete from ds040121 where val < 10;
create table ds151120 (id serial, tag varchar, val float);
delete from ds151120 where val < 10;
create table dsres040121 (id serial, tag varchar, val float);
delete from dsres040121 where val < 70;
create table dsres151120 (id serial, tag varchar, val float);
delete from dsres151120 where val < 70;
create table js040121 (id serial, tag varchar, val float);
delete from js040121 where val < 10;
create table js151120 (id serial, tag varchar, val float);
delete from js151120 where val < 10;

select * from py040121;
select * from py151120;
truncate py040121 restart identity;

select p.tag, round((p.val/(select max(val) from py040121))*100) as rang, 
round(((p.val/(select max(val) from py040121))/(p2.val/(select max(val) from py151120)) - 1)*100) as r_r_old
from py040121 p 
left join py151120 p2 
on p.tag = p2.tag order by r_r_old;

select p.tag, round((p.val/(select max(val) from pyres040121))*100) as rang, 
round(((p.val/(select max(val) from pyres040121))/(p2.val/(select max(val) from pyres151120)) - 1)*100) as r_r_old
from pyres040121 p 
left join pyres151120 p2 
on p.tag = p2.tag order by r_r_old;

select p.tag, round((p.val/(select max(val) from ds040121))*100) as rang, 
round(((p.val/(select max(val) from ds040121))/(p2.val/(select max(val) from ds151120)) - 1)*100) as r_r_old
from ds040121 p 
left join ds151120 p2 
on p.tag = p2.tag order by r_r_old;

select p.tag, round((p.val/(select max(val) from dsres040121))*100) as rang, 
round(((p.val/(select max(val) from dsres040121))/(p2.val/(select max(val) from dsres151120)) - 1)*100) as r_r_old
from dsres040121 p 
left join dsres151120 p2 
on p.tag = p2.tag order by r_r_old;

select p.tag, round((p.val/(select max(val) from js040121))*100) as rang, 
round(((p.val/(select max(val) from js040121))/(p2.val/(select max(val) from js151120)) - 1)*100) as r_r_old
from js040121 p 
left join js151120 p2 
on p.tag = p2.tag order by r_r_old;