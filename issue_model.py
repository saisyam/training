from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,Text,TIMESTAMP,JSON
from sqlalchemy.orm import relationship

Base = declarative_base()

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
    #milestone =Column(String(500))
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



