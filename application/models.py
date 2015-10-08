from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSON
from application import db

class programs(db.Model):
    __tablename__ = 'programs'

    id = Column(Integer, primary_key=True)
    program_name = Column(String(100), nullable=False)

    def __init__(self, program_name):
        self.program_name = program_name
