from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,TEXT,TIMESTAMP
from sqlalchemy.orm import relationship

Base = declarative_base()

class Repository(Base):
    __tablename__ = 'item'
    item1_id = Column(Integer, primary_key=True) 
    id = Column(Integer,nullable=False)
    node_id = Column(TEXT, nullable=False)
    name = Column(TEXT, nullable=False)
    full_name = Column(TEXT, nullable=False)
    private = Column(Boolean, nullable=False)
    html_url = Column(TEXT, nullable=False)
    description = Column(TEXT, nullable=False)
    fork = Column(Boolean, nullable=False)
    url = Column(TEXT, nullable=False)
    forks_url = Column(TEXT, nullable=False)
    keys_url = Column(TEXT, nullable=False)
    collaborators_url = Column(TEXT, nullable=False)
    teams_url = Column(TEXT, nullable=False)
    hooks_url = Column(TEXT, nullable=False)
    issue_events_url = Column(TEXT, nullable=False)
    events_url = Column(TEXT, nullable=False)
    assignees_url = Column(TEXT, nullable=False)
    branches_url = Column(TEXT, nullable=False)
    tags_url = Column(TEXT, nullable=False)
    blobs_url = Column(TEXT, nullable=False)
    git_tags_url = Column(TEXT, nullable=False)
    git_refs_url = Column(TEXT, nullable=False)
    trees_url = Column(TEXT, nullable=False)
    statuses_url = Column(TEXT, nullable=False)
    languages_url = Column(TEXT, nullable=False)
    stargazers_url = Column(TEXT, nullable=False)
    contributors_url = Column(TEXT, nullable=False)
    subscribers_url = Column(TEXT, nullable=False)
    subscription_url = Column(TEXT, nullable=False)
    commits_url = Column(TEXT, nullable=False)
    git_commits_url = Column(TEXT, nullable=False)
    comments_url = Column(TEXT, nullable=False)
    issue_comment_url = Column(TEXT, nullable=False)
    contents_url = Column(TEXT, nullable=False)
    compare_url = Column(TEXT, nullable=False)
    merges_url = Column(TEXT, nullable=False)
    archive_url = Column(TEXT, nullable=False)
    downloads_url = Column(TEXT, nullable=False)
    issues_url = Column(TEXT, nullable=False)
    pulls_url = Column(TEXT, nullable=False)
    milestones_url = Column(TEXT, nullable=False)
    notifications_url = Column(TEXT, nullable=False)
    labels_url = Column(TEXT, nullable=False)
    releases_url = Column(TEXT, nullable=False)
    deployments_url = Column(TEXT, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at= Column(TIMESTAMP, nullable=False)
    pushed_at = Column(TIMESTAMP, nullable=False)
    git_url = Column(TEXT, nullable=False)
    ssh_url = Column(TEXT, nullable=False)
    clone_url = Column(TEXT, nullable=False)
    svn_url = Column(TEXT, nullable=False)
    homepage = Column(TEXT, nullable=False)
    size = Column(Integer)
    stargazers_count = Column(TEXT, nullable=False)
    watchers_count = Column(TEXT, nullable=False)
    language= Column(TEXT, nullable=False)
    has_issues = Column(Boolean, nullable=False)
    has_projects = Column(Boolean, nullable=False)
    has_downloads= Column(Boolean, nullable=False)
    has_wiki = Column(Boolean, nullable=False)
    has_pages = Column(Boolean, nullable=False)
    has_discussions= Column(Boolean, nullable=False)
    forks_count = Column(Integer)
    mirror_url= Column(TEXT, nullable=False)
    archived= Column(Boolean, nullable=False)
    disabled= Column(Boolean, nullable=False)
    open_issues_count= Column(Integer)
    allow_forking= Column(Boolean, nullable=False)
    is_template= Column(Boolean, nullable=False)
    web_commit_signoff_required= Column(Boolean, nullable=False)
    visibility= Column(TEXT, nullable=False)
    forks= Column(Integer, nullable=False)
    open_issues= Column(Boolean,nullable=False)
    watchers= Column(TEXT)
    default_branch= Column(TEXT, nullable=False)
    score= Column(Integer)
    topics= Column(TEXT, nullable=False)
    license_id = Column(Integer, ForeignKey("license.id"), nullable=False)
    license = relationship("License", foreign_keys='Repository.license_id')
    

    def __repr__(self):
        return "<Repository(id={}, node_id='{}', name='{}', fullname='{}', private={}, size={}, license_id={})>"\
                .format(self.id, self.node_id, self.name, self.full_name, self.private, self.size, self.license_id)

class License(Base):
    __tablename__ = 'license'
    id = Column(Integer, primary_key=True)
    key = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    spdx_id = Column(String(50), nullable=False)
    node_id = Column(String(50), nullable=False)
    url = Column(String(300))

    def __repr__(self):
        return "<License(id={}, node_id='{}', name='{}', key='{}', spdx_id={}, node_id={}, url={})>"\
                .format(self.id, self.node_id, self.name, self.key, self.spdx_id, self.node_id, self.url)
                