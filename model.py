from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Repository(Base):
    __tablename__ = 'repository'
    id = Column(Integer, primary_key=True)
    node_id = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    full_name = Column(String(100), nullable=False)
    private = Column(Boolean, nullable=False)
    size = Column(Integer)
    license_id = Column(Integer, ForeignKey("license.id"), nullable=False)
    license = relationship("License", foreign_keys='Repository.license_id')
    owner_id=Column(Integer, ForeignKey("owner.id"), nullable=False)
    owner=relationship('Owner',foreign_keys='Repository.owner_id')
    
    def __repr__(self):
        return "<Repository(id={}, node_id='{}', name='{}', fullname='{}', private={}, size={}, license_id={} ,owner_id='{}')>"\
                .format(self.id, self.node_id, self.name, self.full_name, self.private, self.size, self.license_id, self.owner_id)

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
