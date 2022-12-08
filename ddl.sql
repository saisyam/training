create table license(
	id serial primary key,
	key varchar(50) ,
	name varchar(200),
	spdx_id varchar(50),
	node_id varchar(50),
	url varchar(300)
);

CREATE TABLE owner(
    login VARCHAR(500),
    id INT NOT NULL PRIMARY KEY,
    node_id VARCHAR(500),
    avatar_url VARCHAR(500),
    gravatar_id VARCHAR(500),
    url VARCHAR(500),
    html_url VARCHAR(500),
    followers_url VARCHAR(500),
    following_url VARCHAR(500),
    gists_url VARCHAR(500),
    starred_url VARCHAR(500),
    subscriptions_url VARCHAR(500),
    organizations_url VARCHAR(500),
    repos_url VARCHAR(500),
    events_url VARCHAR(500),
    received_events_url VARCHAR(500),
    type VARCHAR(500),
    site_admin BOOLEAN
);

create table repository(
	id integer primary key,
	node_id varchar(100) not null,
	name varchar(100) not null,
	full_name varchar(100) not null,
	private boolean not null,
	size integer,
	license_id integer not null,
	foreign key (license_id) references license (id),
	owner_id integer not null,
	foreign key (owner_id) references owner (id)
); 

