from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, Text
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
    owner_id=Column(Integer, ForeignKey("owner.id"), nullable=False)
    owner=relationship('Owner',foreign_keys='Repository.owner_id')
    
    def __repr__(self):
        return "<Repository(id={}, node_id='{}', name='{}', full_name='{}', private={}, html_url = '{}',description = '{}',fork = {}, url = '{}',forks_url = '{}',keys_url = '{}',collaborators_url = '{}',teams_url = '{}',hooks_url = '{}',issue_events_url = '{}',events_url = '{}',assignees_url = '{}',branches_url = '{}',tags_url = '{}',blobs_url = '{}',git_tags_url = '{}',git_refs_url = '{}',trees_url = '{}',statuses_url = '{}',languages_url = '{}', stargazers_url = '{}',contributors_url = '{}',subscribers_url = '{}',subscription_url = '{}',commits_url = '{}',git_commits_url = '{}',comments_url = '{}',issue_comment_url = '{}',contents_url = '{}',compare_url = '{}',merges_url = '{}',archive_url = '{}',downloads_url = '{}',issues_url = '{}',pulls_url = '{}',milestones_url = '{}',notifications_url = '{}',labels_url = '{}',releases_url = '{}',deployments_url = '{}',created_at = {},updated_at = {},pushed_at = {},git_url = '{}',ssh_url = '{}',clone_url = '{}',svn_url = '{}',homepage = '{}',size = {},stargazers_count = {},watchers_count = {},  language = '{}',has_issues = {}, has_projects = {}, has_downloads = {}, has_wiki = {}, has_pages = {},has_discussions = {}, forks_count = {}, mirror_url = '{}', archived = {}, disabled = {}, open_issues_count = {}, allow_forking = {}, is_template = {}, web_commit_signoff_required = {},topics = '{}', visibility = '{}', forks = {}, open_issues = {}, watchers = {}, default_branch = '{}', score = {},owner_id='{}')>"\
                .format(self.id, self.node_id, self.name, self.full_name, self.private,self.html_url,self.description,self.fork,self.url,self.forks_url,self.keys_url,self.collaborators_url,self.teams_url,self.hooks_url,self.issue_events_url,self.events_url,self.assignees_url,self.branches_url,self.tags_url,self.blobs_url,self.git_tags_url,self.git_refs_url,self.trees_url, self.statuses_url,self.languages_url,self.stargazers_url,self.contributors_url,self.subscribers_url,self.subscription_url,self.commits_url,self.git_commits_url,self.comments_url,self.issue_comment_url,self.contents_url,self.compare_url,self.merges_url,self.archive_url,self.downloads_url,self.issues_url,self.pulls_url,self.milestones_url,self.notifications_url,self.labels_url,self.releases_url,self.deployments_url,self.created_at,self.updated_at,self.pushed_at,self.git_url,self.ssh_url,self.clone_url,self.svn_url,self.homepage,self.size,self.stargazers_count,self.watchers_count,self.language,self.has_issues,self.has_projects,self.has_downloads,self.has_wiki,self.has_pages,self.has_discussions,self.forks_count,self.mirror_url,self.archived,self.disabled,self.open_issues_count,self.allow_forking,self.is_template, self.web_commit_signoff_required, self.topics, self.visibility, self.forks, self.open_issues,self.watchers,self.default_branch,self.score,self.owner_id)
class License(Base):
    __tablename__ = 'license'
    id = Column(Integer,autoincrement=True, primary_key=True)
    key = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    spdx_id = Column(String(50), nullable=False)
    node_id = Column(String(50), nullable=False)
    url = Column(String(300))
    repo_id=Column(Integer, ForeignKey("repository.id"), nullable=False)
    repository=relationship('Repository',foreign_keys='License.repo_id')
    
    def __repr__(self):
        return "<License(id={}, node_id='{}', name='{}', key='{}', spdx_id={}, node_id={}, url={},repo_id='{}')>"\
                .format(self.id, self.node_id, self.name, self.key, self.spdx_id, self.node_id, self.url,self.repo_id)


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
    