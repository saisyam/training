from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,Text
from sqlalchemy.orm import relationship

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owner'
    login = Column(Text, nullable=False)
    id  =  Column(Integer, primary_key=True,nullable=False)
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
        return "<owner(login='{}', id='{}', node_id='{}', avatar_url={}, gravatar_id={}, url={},html_url={},followers_url={},following_url={},gists_url={},starred_url={},subscriptions_url={},organizations_url={},repos_url={},events_url={},received_events_url={},type={},site_admin={})>"\
                .format(self.login, self.id, self.node_id, self.avatar_url, self.gravatar_id, self.url,self.html_url,self.followers_url,self.following_url,self.gists_url,self.starred_url,self.subscriptions_url,self.organizations_url,self.repos_url,self.events_url,self.received_events_url,self.type,self.site_admin)

class License(Base):
    __tablename__ = 'license'
    id = Column(Integer,primary_key=True)
    key = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    spdx_id = Column(Text, nullable=False)
    node_id = Column(Text, nullable=False)
    url = Column(Text,nullable=False)
    def __repr__(self):
        return "<License(id='{}' key='{}', name='{}', spdx_id='{}', node_id='{}', url='{}')>"\
                .format(self.id, self.key, self.name, self.spdx_id, self.node_id, self.url)



class Repository(Base):
    __tablename__ = 'repository'
    id = Column(Integer, primary_key=True)
    node_id = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    full_name = Column(Text, nullable=False)
    private = Column(Boolean, nullable=False)
    size = Column(Integer)
    owner_id = Column(Integer, ForeignKey("owner.id"), nullable=False)
    owner = relationship("Owner", foreign_keys='Repository.owner_id')
    license_id = Column(Integer, ForeignKey("license.id"), nullable=False)
    license = relationship("License", foreign_keys='Repository.license_id')

    def __repr__(self):
        return "<Repository(id={}, node_id='{}', name='{}', fullname='{}', private={}, size={}, owner_id={},license_id={})>"\
                .format(self.id, self.node_id, self.name, self.full_name, self.private, self.size, self.owner_id,self.license_id)




