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