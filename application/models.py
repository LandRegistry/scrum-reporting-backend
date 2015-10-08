from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSON
from application import db

class programmes(db.Model):
    __tablename__ = 'programmes'

    id = Column(Integer, primary_key=True)
    programme_name = Column(String(100), nullable=False)
    programme_manager = Column(String(100), nullable=True)
    service_manager = Column(String(100), nullable=True)

    def __init__(self, programme_name, programme_manager, service_manager):
        self.programme_name = programme_name
        self.programme_manager = programme_manager
        self.service_manager = service_manager


class projects(db.Model):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    programme_id = Column(Integer, nullable=False)
    project_name = Column(String(100), nullable=False)
    product_owner = Column(String(100), nullable=True)
    scrum_master = Column(String(100), nullable=True)

    def __init__(self, programme_id, project_name, product_owner, scrum_master):
        self.programme_id = programme_id
        self.project_name = project_name
        self.product_owner = product_owner
        self.scrum_master = scrum_master
