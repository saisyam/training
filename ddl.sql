create table repository(
	id integer primary key,
	node_id varchar(100) not null,
	name varchar(100) not null,
	full_name varchar(100) not null,
	private boolean not null,
	size integer,
	license_id integer not null,
	foreign key (license_id) references license (id)
) 

create table license(
	id serial primary key,
	key varchar(50) not null,
	name varchar(200) not null,
	spdx_id varchar(50) not null,
	node_id varchar(50) not null,
	url varchar(300)
)