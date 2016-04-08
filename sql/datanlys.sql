select count(distinct item_id) from interactions;
select count(*) from items where active_during_test = 1;
load data infile '/media/psf/Home/Desktop/recsys/RecsysChallenge/submit/online/target_users.csv' into table target_users CHARACTER SET utf8 FIELDS TERMINATED BY ',' ENCLOSED BY '"';

create table local_interactions as
select * from interactions where created_at < 1446422400;

drop table if exists local_target_users;
create table local_target_users as
select distinct user_id from interactions where created_at >= 1446422400 and interaction_type != 4;

drop table if exists local_predicted_interactions;
create table local_predicted_interactions as
	select * from interactions where created_at >= 1446422400;

alter table local_interactions add week int(11) default 0;

drop table if exists local_interactions_week;
create table local_interactions_week as
	select user_id, item_id, interaction_type, created_at, WEEK(FROM_UNIXTIME(created_at-3600*8),1) as week 
	from local_interactions;

drop table if exists interactions_week;
create table interactions_week as
	select user_id, item_id, interaction_type, created_at, WEEK(FROM_UNIXTIME(created_at-3600*8),1) as week 
	from interactions;

-- select count(distinct item_id) from 
-- (
-- 	select item_id from local_interactions_week where week = 44
-- 	intersect
-- 	select item_id from local_interactions_week where week = 45
-- );

select count(distinct b.item_id) from 
(
	select distinct item_id from interactions_week where week = 44
)a
left join 
(
	select distinct item_id from interactions_week where week = 45
)b on a.item_id = b.item_id;




