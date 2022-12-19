from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, Text , ARRAY
from sqlalchemy.orm import relationship

Base = declarative_base()

class Repository(Base):
    __tablename__ = 'repository'
    id = Column(Integer, primary_key=True)
    node_id = Column(String(500))
    name = Column(String(500))
    full_name = Column(String(500))
    private = Column(Boolean)
    html_url = Column(String(500))
    description = Column(String(500))
    fork = Column(Boolean)
    url = Column(String(500))
    forks_url = Column(String(500))
    keys_url = Column(String(500))
    collaborators_url = Column(String(500))
    teams_url = Column(String(500))
    hooks_url = Column(String(500))
    issue_events_url = Column(String(500))
    events_url = Column(String(500))
    assignees_url = Column(String(500))
    branches_url = Column(String(500))
    tags_url = Column(String(500))
    blobs_url = Column(String(500))
    git_tags_url = Column(String(500))
    git_refs_url = Column(String(500))
    trees_url = Column(String(500))
    statuses_url = Column(String(500))
    languages_url = Column(String(500))
    stargazers_url = Column(String(500))
    contributors_url = Column(String(500))
    subscribers_url = Column(String(500))
    subscription_url = Column(String(500))
    commits_url = Column(String(500))
    git_commits_url = Column(String(500))
    comments_url = Column(String(500))
    issue_comment_url = Column(String(500))
    contents_url = Column(String(500))
    compare_url = Column(String(500))
    merges_url = Column(String(500))
    archive_url = Column(String(500))
    downloads_url = Column(String(500))
    issues_url = Column(String(500))
    pulls_url = Column(String(500))
    milestones_url = Column(String(500))
    notifications_url = Column(String(500))
    labels_url = Column(String(500))
    releases_url = Column(String(500))
    deployments_url = Column(String(500))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    pushed_at = Column(TIMESTAMP)
    git_url = Column(String(500))
    ssh_url = Column(String(500))
    clone_url = Column(String(500))
    svn_url = Column(String(500))
    homepage = Column(String(500))
    size = Column(Integer)
    stargazers_count = Column(Integer)
    watchers_count = Column(Integer)
    language = Column(String(500))
    has_issues = Column(Boolean)
    has_projects = Column(Boolean)
    has_downloads = Column(Boolean)
    has_wiki = Column(Boolean)
    has_pages = Column(Boolean)
    has_discussions = Column(Boolean)
    forks_count = Column(Integer)
    mirror_url = Column(String(500))
    archived = Column(Boolean)
    disabled = Column(Boolean)
    open_issues_count = Column(Integer)
    allow_forking = Column(Boolean)
    is_template = Column(Boolean)
    web_commit_signoff_required = Column(Boolean)
    topics = Column(Text)
    visibility = Column(String(500))
    forks = Column(Integer)
    open_issues = Column(Integer)
    watchers = Column(Integer)
    default_branch = Column(String(500))
    score = Column(Integer)
    license_id = Column(ForeignKey("license.id"), nullable=False)
    license = relationship("License", foreign_keys='Repository.license_id')
    owner_id=Column(Integer, ForeignKey("owner.id"), nullable=False)
    owner=relationship('Owner',foreign_keys='Repository.owner_id')
    
    def __repr__(self):
        return "<Repository(id={}, node_id='{}', name='{}', full_name='{}', private={}, html_url = '{}',description = '{}',fork = {}, url = '{}',forks_url = '{}',keys_url = '{}',collaborators_url = '{}',teams_url = '{}',hooks_url = '{}',issue_events_url = '{}',events_url = '{}',assignees_url = '{}',branches_url = '{}',tags_url = '{}',blobs_url = '{}',git_tags_url = '{}',git_refs_url = '{}',trees_url = '{}',statuses_url = '{}',languages_url = '{}', stargazers_url = '{}',contributors_url = '{}',subscribers_url = '{}',subscription_url = '{}',commits_url = '{}',git_commits_url = '{}',comments_url = '{}',issue_comment_url = '{}',contents_url = '{}',compare_url = '{}',merges_url = '{}',archive_url = '{}',downloads_url = '{}',issues_url = '{}',pulls_url = '{}',milestones_url = '{}',notifications_url = '{}',labels_url = '{}',releases_url = '{}',deployments_url = '{}',created_at = {},updated_at = {},pushed_at = {},git_url = '{}',ssh_url = '{}',clone_url = '{}',svn_url = '{}',homepage = '{}',size = {},stargazers_count = {},watchers_count = {},  language = '{}',has_issues = {}, has_projects = {}, has_downloads = {}, has_wiki = {}, has_pages = {},has_discussions = {}, forks_count = {}, mirror_url = '{}', archived = {}, disabled = {}, open_issues_count = {}, allow_forking = {}, is_template = {}, web_commit_signoff_required = {},topics = '{}', visibility = '{}', forks = {}, open_issues = {}, watchers = {}, default_branch = '{}', score = {},owner_id='{}',license_id={})>"\
                .format(self.id, self.node_id, self.name, self.full_name, self.private,self.html_url,self.description,self.fork,self.url,self.forks_url,self.keys_url,self.collaborators_url,self.teams_url,self.hooks_url,self.issue_events_url,self.events_url,self.assignees_url,self.branches_url,self.tags_url,self.blobs_url,self.git_tags_url,self.git_refs_url,self.trees_url, self.statuses_url,self.languages_url,self.stargazers_url,self.contributors_url,self.subscribers_url,self.subscription_url,self.commits_url,self.git_commits_url,self.comments_url,self.issue_comment_url,self.contents_url,self.compare_url,self.merges_url,self.archive_url,self.downloads_url,self.issues_url,self.pulls_url,self.milestones_url,self.notifications_url,self.labels_url,self.releases_url,self.deployments_url,self.created_at,self.updated_at,self.pushed_at,self.git_url,self.ssh_url,self.clone_url,self.svn_url,self.homepage,self.size,self.stargazers_count,self.watchers_count,self.language,self.has_issues,self.has_projects,self.has_downloads,self.has_wiki,self.has_pages,self.has_discussions,self.forks_count,self.mirror_url,self.archived,self.disabled,self.open_issues_count,self.allow_forking,self.is_template, self.web_commit_signoff_required, self.topics, self.visibility, self.forks, self.open_issues,self.watchers,self.default_branch,self.score,self.owner_id,self.license_id)
class License(Base):
    __tablename__ = 'license'
    id = Column(Integer,autoincrement=True, primary_key=True)
    key = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    spdx_id = Column(String(50), nullable=False)
    node_id = Column(String(50), nullable=False)
    url = Column(String(300))
    
    def __repr__(self):
        return "<License(id={}, node_id='{}', name='{}', key='{}', spdx_id={}, node_id={}, url={})>"\
                .format(self.id, self.node_id, self.name, self.key, self.spdx_id, self.node_id, self.url)


class Owner(Base):
    __tablename__ = "owner"

    login=Column(String(500))
    id = Column(Integer, primary_key=True,nullable=False)
    node_id = Column(String(500))
    avatar_url = Column(String(500))
    gravatar_id = Column(String(500))
    url = Column(String(500))
    html_url = Column(String(500))
    followers_url = Column(String(500))
    following_url = Column(String(500))
    gists_url = Column(String(500))
    starred_url = Column(String(500))
    subscriptions_url = Column(String(500))
    organizations_url = Column(String(500))
    repos_url = Column(String(500))
    events_url = Column(String(500))
    received_events_url = Column(String(500))
    type = Column(String(500))
    site_admin = Column(Boolean)

def __repr__(self):
        return "<owner(login='{}', id='{}', node_id='{}',avatar_url='{}',gravatar_id='{}',url='{}',html_url='{}',followers_url='{}',following_url='{}',gists_url='{}',starred_url='{}',subscriptions_url='{}',organizations_url='{}',repos_url='{}',events_url='{}',received_events_url='{}',type='{}',site_admin='{}')>"\
        .format(self.login,self.id,self.node_id,self.avatar_url,self.gravatar_id,self.url,self.html_url,self.followers_url,self.following_url,self.gists_url,self.starred_url,self.subscriptions_url,self.organizations_url,self.repos_url,self.events_url,self.received_events_url,self.type,self.site_admin,)


class Branch_url(Base):
    __tablename__="branch_url"

    
    id = Column(Integer,primary_key=True)
    name= Column(String(100))
    commit_sha= Column(String(500), ForeignKey("commit_branch_url.sha"), nullable=False)
    Commit_branch_url=relationship('Commit_branch_url',foreign_keys='Branch_url.commit_sha')
    protected= Column(Boolean)

    def __repr__(self):
        return "<branch_url(id='{}',name='{}',commit_id='{}',protected='{}')>"\
            .format(self.id,self.name,self.commit_sha,self.protected)

class Commit_branch_url(Base):
    __tablename__="commit_branch_url"


    sha= Column(String(500),primary_key=True)
    url= Column(String(500))

    def __repr__(self):
        return "<commit_branch_url(id='{}',sha='{}',url='{}'>"\
            .format(self.id,self.sha,self.url)
    


class Users(Base):
    __tablename__ = 'users'
    login =Column(String(500))
    id =Column(Integer, primary_key=True,nullable=False)
    node_id =Column(String(500))
    avatar_url =Column(String(500))
    gravatar_id=Column(String(500))
    url =Column(String(500))
    html_url=Column(String(500))
    followers_url=Column(String(500))
    following_url=Column(String(500))
    gists_url=Column(String(500))
    starred_url=Column(String(500))
    subscriptions_url=Column(String(500))
    organizations_url=Column(String(500))
    repos_url=Column(String(500))
    events_url=Column(String(500))
    received_events_url=Column(String(500))
    type=Column(String(500))
    site_admin=Column(String(500))
    def __repr__(self):
        return "<Users(login={},id={} ,node_id='{}', avatar_url='{}', url='{}', html_url='{}', followers_url='{}',following_url='{}',gists_url={},starred_url='{}',subscriptions_url='{}',organizations_url='{}',repos_url='{}',events_url='{}',received_events_url='{}',type='{}',site_admin='{}')>"\
                .format(self.login,self.id, self.node_id, self.avatar_url, self.url, self.html_url, self.followers_url,self.following_url,self.gists_url,self.starred_url,self.subscriptions_url,self.organizations_url,self.repos_url,self.events_url,self.received_events_url,self.type,self.site_admin)


class Reactions(Base):
    __tablename__ = 'reactions'
    id =Column(Integer, primary_key=True,nullable=False)
    url = Column(String(500))
    total_count =Column(Integer)
    laugh =Column(Integer)
    hooray =Column(Integer)
    confused=Column(Integer)
    heart=Column(Integer)
    rocket=Column(Integer)
    eyes=Column(Integer)
    def __repr__(self):
        return "<Reactions(id= {},url='{}', total_count={}, laugh='{}', hooray='{}', confused='{}', heart='{}', eyes='{}')>"\
                .format(self.id,self.url, self.total_count, self.laugh, self.hooray, self.confused, self.heart, self.eyes)



class Labels(Base):
    __tablename__ = 'labels'
    id = Column(Integer, primary_key=True,nullable=False)
    node_id = Column(String(500))
    url = Column(String(500))
    name = Column(String(500)) 
    color = Column(String(500))
    defult = Column(String(500))
    description = Column(String(500))
    def __repr__(self):
        return "<Lables(id={}, node_id={}, url='{}', name='{}', color={}, defult={}, description={})>"\
                .format(self.id, self.node_id, self.url, self.name, self.color, self.defult, self.description)




class Assignee(Base):
    __tablename__ = 'assignee'
    id =Column(Integer, primary_key=True,nullable=False)
    login =Column(String(500))
    assignee_id =Column(Integer)
    node_id =Column(String(500))
    avatar_url =Column(String(500))
    gravatar_id=Column(String(500))
    url =Column(String(500))
    html_url=Column(String(500))
    followers_url=Column(String(500))
    following_url=Column(String(500))
    gists_url=Column(String(500))
    starred_url=Column(String(500))
    subscriptions_url=Column(String(500))
    organizations_url=Column(String(500))
    repos_url=Column(String(500))
    events_url=Column(String(500))
    received_events_url=Column(String(500))
    type=Column(String(500))
    site_admin=Column(String(500))
    def __repr__(self):
        return "Assignee<(id={},login='{}',assignee_id={} ,node_id='{}', avatar_url='{}', url='{}', html_url='{}', followers_url='{}',following_url='{}',gists_url={},starred_url='{}',subscriptions_url='{}',organizations_url='{}',repos_url='{}',events_url='{}',received_events_url='{}',type='{}',site_admin='{}')>"\
                .format(self.id,self.login,self.assignee_id, self.node_id, self.avatar_url, self.url, self.html_url, self.followers_url,self.following_url,self.gists_url,self.starred_url,self.subscriptions_url,self.organizations_url,self.repos_url,self.events_url,self.received_events_url,self.type,self.site_admin)



class Assignees(Base):
    __tablename__ = 'assignees'
    id =Column(Integer, primary_key=True,nullable=False)
    login =Column(String(500))
    assignees_id =Column(Integer)
    node_id =Column(String(500))
    avatar_url =Column(String(500))
    gravatar_id=Column(String(500))
    url =Column(String(500))
    html_url=Column(String(500))
    followers_url=Column(String(500))
    following_url=Column(String(500))
    gists_url=Column(String(500))
    starred_url=Column(String(500))
    subscriptions_url=Column(String(500))
    organizations_url=Column(String(500))
    repos_url=Column(String(500))
    events_url=Column(String(500))
    received_events_url=Column(String(500))
    type=Column(String(500))
    site_admin=Column(String(500))
    def __repr__(self):
        return "Assignees<(id={},login={},assignees_id={} ,node_id='{}', avatar_url='{}', url='{}', html_url='{}', followers_url='{}',following_url='{}',gists_url={},starred_url='{}',subscriptions_url='{}',organizations_url='{}',repos_url='{}',events_url='{}',received_events_url='{}',type='{}',site_admin='{}')>"\
                .format(self.id,self.login,self.assignees_id, self.node_id, self.avatar_url, self.url, self.html_url, self.followers_url,self.following_url,self.gists_url,self.starred_url,self.subscriptions_url,self.organizations_url,self.repos_url,self.events_url,self.received_events_url,self.type,self.site_admin)




class Issue_url(Base):
    __tablename__ = 'issue_url'
    id  =  Column(Integer, primary_key=True,nullable=False)
    url = Column(String(500))
    repository_url = Column(String(500))
    labels_url = Column(String(500))
    comments_url = Column(String(500))
    events_url = Column(String(500))
    html_url = Column(String(500))
    node_id = Column(String(500))
    number = Column(Integer,nullable=False)
    title = Column(String(500))
    state = Column(String(500))
    locked = Column(Boolean)
    # milestone =Column(String(500))
    comments =Column(Integer)
    created_at =Column(TIMESTAMP)
    updated_at =Column(TIMESTAMP)
    closed_at =Column(TIMESTAMP)
    author_association =Column(String(500))
    active_lock_reason =Column(String(500))
    body =Column(String(500))
    timeline_url =Column(String(500))
    performed_via_github_app =Column(String(500))
    state_reason=Column(String(500))
    
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("Users", foreign_keys='Issue_url.user_id')
    assignee_id = Column(Integer, ForeignKey("assignee.id"))
    assignee = relationship("Assignee", foreign_keys='Issue_url.assignee_id')
    assignees_id = Column(Integer, ForeignKey("assignees.id"))
    assignees = relationship("Assignees", foreign_keys='Issue_url.assignees_id')
    labels_id = Column(Integer, ForeignKey("labels.id"))
    labels = relationship("Labels", foreign_keys='Issue_url.labels_id')
    reactions_id = Column(Integer, ForeignKey("reactions.id"))
    reactions = relationship("Reactions", foreign_keys='Issue_url.reactions_id')


    def __repr__(self):
        return "Issue_url<(id={},url='{}' repository_url='{}', labels_url='{}', comments_url='{}', events_url='{}', html_url='{}',node_id='{}',number={},title='{},'state='{}',locked='{}',comments='{}',created_at='{}',updated_at='{}',closed_at='{}',author_association='{}',active_lock_reason='{}',body='{}',timeline_url='{}',performed_via_github_app='{}',state_reason='{}',user_id={},assignee_id={},assignees_id={},labels_id={},reactions_id={})>"\
                .format(self.id,self.url, self.repository_url, self.labels_url, self.comments_url, self.events_url, self.html_url,self.node_id,self.number,self.title,self.state,self.locked,self.comments,self.created_at,self.updated_at,self.closed_at,self.author_association,self.active_lock_reason,self.body,self.timeline_url,self.performed_via_github_app,self.state_reason,self.user_id,self.assignee_id,self.assignees_id,self.labels_id,self.reactions_id)