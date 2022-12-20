CREATE TABLE repository(
    id INT NOT NULL PRIMARY KEY,
    node_id VARCHAR(500),
    name VARCHAR(500),
    full_name VARCHAR(500),
    private BOOLEAN,
    html_url VARCHAR(500),
    description VARCHAR(500),
    fork BOOLEAN,
    url VARCHAR(500),
    forks_url VARCHAR(500),
    keys_url VARCHAR(500),
    collaborators_url VARCHAR(500),
    teams_url VARCHAR(500),
    hooks_url VARCHAR(500),
    issue_events_url VARCHAR(500),
    events_url VARCHAR(500),
    assignees_url VARCHAR(500),
    branches_url VARCHAR(500),
    tags_url VARCHAR(500),    
    blobs_url VARCHAR(500),
    git_tags_url VARCHAR(500),
    git_refs_url VARCHAR(500),
    trees_url VARCHAR(500),    
    statuses_url VARCHAR(500),
    languages_url VARCHAR(500),
    stargazers_url VARCHAR(500),    
    contributors_url VARCHAR(500),    
    subscribers_url VARCHAR(500),    
    subscription_url VARCHAR(500),    
    commits_url VARCHAR(500),    
    git_commits_url VARCHAR(500),    
    comments_url VARCHAR(500),
    issue_comment_url VARCHAR(500),    
    contents_url VARCHAR(500),    
    compare_url VARCHAR(500),    
    merges_url VARCHAR(500),    
    archive_url VARCHAR(500),    
    downloads_url VARCHAR(500),    
    issues_url VARCHAR(500),    
    pulls_url VARCHAR(500),    
    milestones_url VARCHAR(500),    
    notifications_url VARCHAR(500),    
    labels_url VARCHAR(500),    
    releases_url VARCHAR(500),    
    deployments_url VARCHAR(500),    
    created_at TIMESTAMP,    
    updated_at TIMESTAMP,
    pushed_at TIMESTAMP,    
    git_url    VARCHAR(500),
    ssh_url VARCHAR(500),    
    clone_url VARCHAR(500),    
    svn_url VARCHAR(500),    
    homepage VARCHAR(500),
    size int,
    stargazers_count int,    
    watchers_count int,
    language VARCHAR(500),
    has_issues BOOLEAN,
    has_projects BOOLEAN,    
    has_downloads BOOLEAN,
    has_wiki BOOLEAN,
    has_pages BOOLEAN,
    has_discussions BOOLEAN,
    forks_count INT,
    mirror_url VARCHAR(500),    
    archived BOOLEAN,    
    disabled BOOLEAN,
    open_issues_count INT,    
    allow_forking BOOLEAN,    
    is_template BOOLEAN,
    web_commit_signoff_required BOOLEAN,
    topics TEXT [],
    visibility VARCHAR(500),    
    forks INT,    
    open_issues INT,
    watchers INT,    
    default_branch VARCHAR(500),
    score INT,
	license_id INT NOT NULL,
    owner_id INT NOT NULL,
	FOREIGN KEY(license_id) REFERENCES license(id),
	FOREIGN KEY(owner_id) REFERENCES owner(id)
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




create table license(
    id serial primary key,
    key varchar(100),
    name varchar(200),
    spdx_id varchar(100),
    url varchar(300),
	node_id varchar(100)
);








create table commit_branch_url(
		sha varchar(500) primary key not null,
		url varchar(500)
	);
	
	
create table branch_url(
    id serial primary key not null,
    name varchar(500),
	protected BOOLEAN,
    commit_sha varchar(500) not null,
    foreign key (commit_sha) references commit_branch_url(sha)
    
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
	id Integer not null primary key,
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
	id Integer not null primary key,
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



create table parents(
id serial primary key, 	
sha TEXT,
url TEXT,
html_url TEXT
);



create table commit_main(
	id serial primary key,
	sha TEXT,
    node_id TEXT,
	url TEXT,
	html_url TEXT,
	comments_url TEXT,
	commit_id INT not null,
	commit_author_id INT not null,
	commit_committer_id INT not null,
	commit_tree_id INT not null,
	commit_verification_id INT not null,
	author_id1 INT not null,
	committer_id1 INT not null,
    parents_id INT not null,
	foreign key (parents_id) references parents(id),
	foreign key (commit_author_id) references commit_author(id),
	foreign key (commit_committer_id) references commit_committer(id),
	foreign key (commit_id) references commit(id),
	foreign key (commit_tree_id) references commit_tree(id),
	foreign key (commit_verification_id) references commit_verification(id),
	foreign key (author_id1) references author(id),
	foreign key (committer_id1) references committer(id)
);




