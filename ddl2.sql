create table main(
	id serial primary key,
	sha TEXT,
    node_id TEXT,
	url TEXT,
	html_url TEXT,
	comments_url TEXT,
	parents_id INT not null,
	commit_author_id INT not null,
	commit_committer_id INT not null,
	commit_id INT not null,
	commit_tree_id INT not null,
	commit_verification_id INT not null,
	author_id INT not null,
	committer_id INT not null,
	foreign key (parents_id) references parents(id),
	foreign key (commit_author_id) references commit_author(id),
	foreign key (commit_committer_id) references commit_committer(id),
	foreign key (commit_id) references commit(id),
	foreign key (commit_tree_id) references commit_tree(id),
	foreign key (commit_verification_id) references commit_verification(id),
	foreign key (author_id) references author(id),
	foreign key (committer_id) references committer(id)
);

create table parents(
id serial primary key, 	
sha TEXT,
url TEXT,
html_url TEXT
);

create table commit(
id serial primary key,	
message TEXT,
url TEXT,
comment_count INT	
);

create table commit_author(
id serial primary key,	
name TEXT,
email TEXT,
date TIMESTAMP
);
create table commit_committer(
id serial primary key, 
name TEXT,
email TEXT,
date TIMESTAMP
);
create table commit_tree(
	id serial primary key,
	sha TEXT,
	url  TEXT	
);
create table commit_verification(
id serial primary key,	
verified Boolean,
reason TEXT,
signature TEXT,
payload TEXT
);

create table author(
	login  TEXT,
	id Integer primary key,
	node_id  TEXT,
	avatar_url  TEXT,
	gravatar_id  TEXT,
	url  TEXT,
	html_url  TEXT,
	followers_url  TEXT,
	following_url  TEXT,
	gists_url  TEXT,
	starred_url  TEXT,
	subscriptions_url  TEXT,
	organizations_url  TEXT,
	repos_url  TEXT,
	events_url  TEXT,
	received_events_url  TEXT,
	type  TEXT,
	site_admin Boolean	
);


create table committer(
	login  TEXT,
	id Integer primary key,
	node_id  TEXT,
	avatar_url  TEXT,
	gravatar_id  TEXT,
	url  TEXT,
	html_url  TEXT,
	followers_url  TEXT,
	following_url  TEXT,
	gists_url  TEXT,
	starred_url  TEXT,
	subscriptions_url  TEXT,
	organizations_url  TEXT,
	repos_url  TEXT,
	events_url  TEXT,
	received_events_url  TEXT,
	type  TEXT,
	site_admin Boolean	
);
drop table commit
select * from main
select * from commit
select * from commit_author
select * from parents
select * from commit_committer
select * from commit_tree
select * from commit_verification
select * from author
select * from committer