from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,TEXT,TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from model import *


Base = declarative_base()


class Parents(Base):
    __tablename__ = 'parents'
    id=Column(Integer,primary_key=True)
    sha = Column(TEXT)
    url = Column(TEXT)
    html_url = Column(TEXT)
   
    def __repr__(self):
        return "<Parents(id={},sha='{}',url='{}',html_url='{}')>"\
            .format(self.id,self.sha,self.url, self.html_url)

class Commit(Base):
    __tablename__ = 'commit'
    id=Column(Integer,primary_key=True)
    message=Column(TEXT)
    url=Column(TEXT)
    comment_count=Column(TEXT)

    def __repr__(self):
        return "<Commit(id={},message='{}',url='{}',comment_count='{}')>"\
            .format(self.id,self.message, self.url, self.comment_count)

class Commit_author(Base):
    __tablename__ = 'commit_author'
    id=Column(Integer,primary_key=True)
    name =Column(TEXT)
    email =Column(TEXT)
    date =Column(TIMESTAMP)

    def __repr__(self):
        return "<Commit_author(id={},name='{}',email='{}',date='{}')>"\
            .format(self.id, self.name, self.email,self.date)

class Commit_committer(Base):
    __tablename__ = 'commit_committer'
    id=Column(Integer,primary_key=True)
    name =Column(TEXT)
    email =Column(TEXT)
    date =Column(TIMESTAMP)

    def __repr__(self):
        return "<Commit_committer(id={},name='{}',email='{}',date='{}')>"\
            .format(self.id, self.name, self.email,self.date)

class Commit_tree(Base):
    __tablename__ = 'commit_tree'
    id =Column(Integer, primary_key=True)
    sha =Column(TEXT)
    url  =Column(TEXT)	

    def __repr__(self):
        return "<Commit_tree(id={},sha='{}',url='{}')>"\
            .format(self.id, self.sha, self.url) 


class Commit_verification(Base):
    __tablename__ = 'commit_verification'
    id =Column(Integer, primary_key=True)
    verified =Column(Boolean)
    reason =Column(TEXT)
    signature =Column(TEXT)
    payload =Column(TEXT)	

    def __repr__(self):
        return "<Commit_verification(id={},verified='{}',reason='{}',signature='{}',payload='{}')>"\
            .format(self.id, self.verified, self.reason,self.signature,self.payload)   

class Author(Base):
    __tablename__ = 'author'
    author_id =Column(Integer, primary_key=True)
    login =Column(TEXT)
    id =Column(Integer)
    node_id= Column(TEXT)
    avatar_url =Column(TEXT)
    gravatar_id =Column(TEXT)
    url  =Column(TEXT)
    html_url =Column(TEXT)
    followers_url =Column(TEXT)
    following_url =Column(TEXT)
    gists_url =Column(TEXT)
    starred_url=Column(TEXT)
    subscriptions_url=Column(TEXT)
    organizations_url =Column(TEXT)
    repos_url =Column(TEXT)
    events_url =Column(TEXT)
    received_events_url =Column(TEXT)
    type =Column(TEXT)
    site_admin =Column(Boolean)

    def __repr__(self):
        return "<Author(author_id={},login='{}',id={},node_id='{}',avatar_url='{}',gravatar_id='{}',url='{}',html_url='{}',followers_url='{}',following_url='{}',gists_url='{}',starred_url='{}',subscriptions_url='{}',organizations_url='{}',repos_url='{}',events_url='{}',received_events_url='{}',type='{}',site_admin='{}')>"\
            .format(self.author_id,self.login,self.id, self.node_id, self.avatar_url,self.gravatar_id,self.url,self.html_url,self.followers_url,self.following_url,self.gists_url,self.starred_url,self.subscriptions_url,self.organizations_url,self.repos_url,self.events_url,self.received_events_url,self.type,self.site_admin)	

class Committer(Base):
    __tablename__ = 'committer'
    committer_id=Column(Integer,primary_key=True)
    login =Column(TEXT)
    id =Column(Integer)
    node_id= Column(TEXT)
    avatar_url =Column(TEXT)
    gravatar_id =Column(TEXT)
    url  =Column(TEXT)
    html_url =Column(TEXT)
    followers_url =Column(TEXT)
    following_url =Column(TEXT)
    gists_url =Column(TEXT)
    starred_url=Column(TEXT)
    subscriptions_url=Column(TEXT)
    organizations_url =Column(TEXT)
    repos_url =Column(TEXT)
    events_url =Column(TEXT)
    received_events_url =Column(TEXT)
    type =Column(TEXT)
    site_admin =Column(Boolean)

    def __repr__(self):
         return "<Committer(committer_id={},login='{}',id={},node_id='{}',avatar_url='{}',gravatar_id='{}',url='{}',html_url='{}',followers_url='{}',following_url='{}',gists_url='{}',starred_url='{}',subscriptions_url='{}',organizations_url='{}',repos_url='{}',events_url='{}',received_events_url='{}',type='{}',site_admin='{}')>"\
                 .format(self.committer_id,self.login,self.id, self.node_id, self.avatar_url,self.gravatar_id,self.url,self.html_url,self.followers_url,self.following_url,self.gists_url,self.starred_url,self.subscriptions_url,self.organizations_url,self.repos_url,self.events_url,self.received_events_url,self.type,self.site_admin)	

class Main(Base):
    __tablename__ = 'main'
    id=Column(Integer,primary_key=True)
    sha = Column(TEXT)
    node_id = Column(TEXT)
    url = Column(TEXT)
    html_url = Column(TEXT)
    comments_url = Column(TEXT)
    parents_id = Column(Integer,ForeignKey("parents.id"))
    parents= relationship("Parents",foreign_keys='Main.parents_id') 
    commit_id = Column(Integer,ForeignKey("commit.id"))
    commit=relationship("Commit",foreign_keys='Main.commit_id')	
    commit_author_id = Column(Integer,ForeignKey("commit_author.id"))
    commit_author=relationship("Commit_author",foreign_keys='Main.commit_author_id')
    commit_committer_id = Column(Integer,ForeignKey("commit_committer.id"))
    commit_committer=relationship("Commit_committer",foreign_keys='Main.commit_committer_id')
    commit_tree_id = Column(Integer,ForeignKey("commit_tree.id"))
    commit_tree=relationship("Commit_tree",foreign_keys='Main.commit_tree_id')
    commit_verification_id = Column(Integer,ForeignKey("commit_verification.id"))
    commit_verfication=relationship("Commit_verification",foreign_keys='Main.commit_verification_id')
    author_id1 = Column(Integer,ForeignKey("author.author_id"))
    author=relationship("Author",foreign_keys='Main.author_id1')
    committer_id1 = Column(Integer,ForeignKey("committer.committer_id"))
    committer=relationship("Committer",foreign_keys='Main.committer_id1')
	
    
    def __repr__(self):
         return "<Main(id={},sha='{}',node_id='{}',url='{}',html_url='{}',comments_url='{}',parents_id={},commit_id='{}',commit_author_id={},commit_committer_id={},commit_tree_id={},commit_verification_id={},author_id1={},committer_id1={})>"\
                 .format(self.id,self.sha, self.node_id, self.url, self.html_url, self.comments_url,self.parents_id,self.commit_id,self.commit_author_id,self.commit_committer_id,self.commit_tree_id,self.commit_verification_id,self.author_id1,self.committer_id1)

