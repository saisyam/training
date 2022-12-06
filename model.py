from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,Text
from sqlalchemy.orm import relationship

Base = declarative_base()

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
    __tablename__ = 'owner'
    id = Column(Integer, primary_key=True)
    login = Column(Text, nullable=False)
    owner_id  =  Column(Integer, nullable=False)
    node_id = Column(Text, nullable=False)
    avatar_url = Column(Text, nullable=False)
    gravatar_id = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    html_url = Column(Text, nullable=False)
    followers_url = Column(Text, nullable=False)
    following_url = Column(Text, nullable=False)
    gists_url = Column(Text, nullable=False)
    starred_url = Column(Text, nullable=False)
    subscriptions_url = Column(Text, nullable=False)
    organizations_url = Column(Text, nullable=False)
    repos_url = Column(Text, nullable=False)
    events_url = Column(Text, nullable=False)
    received_events_url = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    site_admin = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<owner(id={}, login='{}', owner_id='{}', node_id='{}', avatar_url={}, gravatar_id={}, url={},html_url={},followers_url={},following_url={},gists_url={},starred_url={},subscriptions_url={},organizations_url={},repos_url={},events_url={},received_events_url={},type={},site_admin={})>"\
                .format(self.id, self.login, self.owner_id, self.node_id, self.avatar_url, self.gravatar_id, self.url,self.html_url,self.followers_url,self.following_url,self.gists_url,self.starred_url,self.subscriptions_url,self.organizations_url,self.repos_url,self.events_url,self.received_events_url,self.type,self.site_admin)

class Repository(Base):
    __tablename__ = 'repository'
    id = Column(Integer, primary_key=True)
    node_id = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    full_name = Column(String(100), nullable=False)
    private = Column(Boolean, nullable=False)
    size = Column(Integer)
    license_id = Column(Integer, ForeignKey("license.id"), nullable=False)
    owner_id = Column(Integer, ForeignKey("owner.id"), nullable=False)
    license = relationship("License", foreign_keys='Repository.license_id')
    owner = relationship("Owner", foreign_keys='Repository.owner_id')

    def __repr__(self):
        return "<Repository(id={}, node_id='{}', name='{}', fullname='{}', private={}, size={}, license_id={},owner_id={})>"\
                .format(self.id, self.node_id, self.name, self.full_name, self.private, self.size, self.license_id,self.owner_id)
