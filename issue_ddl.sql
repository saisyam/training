create table users(
   login text,
	id bigint not null primary key,
	node_id text,
	avatar_url text,
	gravatar_id text,
	url text,
	html_url text,
	followers_url text,
	following_url text,
	gists_url text,
	starred_url text,
	subscriptions_url text,
	organizations_url text,
	repos_url text,
	events_url text,
	received_events_url text,
	type text,
	site_admin text
);



create table reactions(
	id serial not null primary key,
	url text,
	total_count int,
	laugh int,
    hooray int,
	confused int,
	heart int,
	rocket int,
	eyes int
);

create table labels(
	id bigint not null primary key,
	node_id text,
	url text,
	name text,
	color text,
	defult text,
	description text
);

create table assignee(
	id serial not null primary key,
    login text,
	assignee_id bigint,
	node_id text,
	avatar_url text,
	gravatar_id text,
	url text,
	html_url text,
	followers_url text,
	following_url text,
	gists_url text,
	starred_url text,
	subscriptions_url text,
	organizations_url text,
	repos_url text,
	events_url text,
	received_events_url text,
	type text,
	site_admin text
);

create table assignees(
	id serial not null primary key,
    login text,
	assignees_id bigint,
	node_id text,
	avatar_url text,
	gravatar_id text,
	url text,
	html_url text,
	followers_url text,
	following_url text,
	gists_url text,
	starred_url text,
	subscriptions_url text,
	organizations_url text,
	repos_url text,
	events_url text,
	received_events_url text,
	type text,
	site_admin text
);

CREATE TABLE issue_url(
id bigint not null primary key,
url text,
repository_url text,
labels_url text,
comments_url text,
events_url text,
html_url text,
node_id text,
number bigint not null,
title text,
state text,
locked Boolean,
milestone text,
comments bigint not null,
created_at timestamp,
updated_at timestamp,
closed_at timestamp,
author_association text,
active_lock_reason text,
body text,
timeline_url text,
performed_via_github_app text,
state_reason text,
user_id bigint,
labels_id bigint,
reactions_id bigint,
assignee_id bigint,
assignees_id bigint,
foreign key(user_id) references users(id),
foreign key(labels_id) references labels(id),
foreign key(reactions_id) references reactions(id),
foreign key(assignee_id) references assignee(id),
foreign key(assignee_id) references assignees(id)
);