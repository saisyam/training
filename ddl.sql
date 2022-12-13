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

create table commit_branch_url(
    sha varchar(500) primary key not null,
    url varchar(500)
);

create table branch_url(
    id serial primary key not null,
    name varchar(500),
    commit_sha varchar(500) not null,
    foreign key (commit_sha) references commit_branch_url(sha),
    protected BOOLEAN
);

create table issue(
    url	
    repository_url varchar(500)
    labels_url varchar(500)
    comments_url varchar(500)
    events_url varchar(500)	
    html_url varchar(500)	
    id Integer
    node_id varchar(500)
    number Integer
    title varchar(500)	
    user(FOREING KEY)	
    labels array[]
    state varchar(500)	
    locked BOOLEAN
    assignee varchar(500)	
    assignees array[]
    milestone varchar(500)	
    comments Integer
    created_at datetime
    updated_at datetime
    closed_at datetime
    author_association varchar(500)	
    active_lock_reason varchar(500)
    draft varchar(500)
    pull_request(foreign key)	
    body varchar(1000)	
    reactions(foreign key)	
    timeline_url varchar(500)	
    performed_via_github_app varchar(500)	
    state_reason varchar(500)

);


