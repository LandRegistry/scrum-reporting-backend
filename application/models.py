from sqlalchemy import Column, Integer, String, DateTime, Float
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
    delivery_manager = Column(String(100), nullable=True)
    project_description = Column(String(2000), nullable=True)
    scrum_tool_link = Column(String(2000), nullable=True)

    def __init__(self, programme_id, project_name, product_owner, scrum_master, project_description, delivery_manager, scrum_tool_link):
        self.programme_id = programme_id
        self.project_name = project_name
        self.product_owner = product_owner
        self.scrum_master = scrum_master
        self.project_description = project_description
        self.delivery_manager = delivery_manager
        self.scrum_tool_link = scrum_tool_link


class sprints(db.Model):
    __tablename__ = 'sprints'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, nullable=False)
    start_date = Column(String(100), nullable=False)
    end_date = Column(String(100), nullable=True)
    sprint_number = Column(Integer, nullable=True)
    sprint_rag = Column(String(1), nullable=False)
    sprint_goal = Column(String(2000), nullable=True)
    sprint_deliverables = Column(String(2000), nullable=True)
    sprint_challenges = Column(String(2000), nullable=False)
    agreed_points = Column(Integer, nullable=True)
    delivered_points = Column(Integer, nullable=True)
    started_points = Column(Integer, nullable=False)
    sprint_issues = Column(String(2000), nullable=True)
    sprint_risks = Column(String(2000), nullable=True)
    sprint_dependencies = Column(String(2000), nullable=True)
    sprint_days = Column(Integer, nullable=True)
    sprint_teamdays = Column(Integer, nullable=True)

    def __init__(self, project_id, start_date, end_date, sprint_number, sprint_rag, sprint_goal, sprint_deliverables, sprint_challenges, agreed_points, delivered_points, started_points, sprint_issues, sprint_risks, sprint_dependencies, sprint_days, sprint_teamdays):
        self.project_id = project_id
        self.start_date = start_date
        self.end_date = end_date
        self.sprint_number = sprint_number
        self.sprint_rag = sprint_rag
        self.sprint_goal = sprint_goal
        self.sprint_deliverables = sprint_deliverables
        self.sprint_challenges = sprint_challenges
        self.delivered_points = delivered_points
        self.started_points = started_points
        self.agreed_points = agreed_points
        self.sprint_issues = sprint_issues
        self.sprint_risks = sprint_risks
        self.sprint_dependencies = sprint_dependencies
        self.sprint_days = sprint_days
        self.sprint_teamdays = sprint_teamdays

class burndown(db.Model):
    __tablename__ = 'burndown'

    id = Column(Integer, primary_key=True)
    sprint_id = Column(Integer, nullable=False)
    sprint_day = Column(Integer, nullable=False)
    sprint_done = Column(Integer, nullable=True)

    def __init__(self, sprint_id, sprint_day, sprint_done):
        self.sprint_id = sprint_id
        self.sprint_day = sprint_day
        self.sprint_done = sprint_done

class sprintpeople(db.Model):
    __tablename__ = 'sprintpeople'

    id = Column(Integer, primary_key=True)
    sprint_id = Column(Integer, nullable=False)
    person_name = Column(String(100), nullable=False)

    def __init__(self, sprint_id, person_name):
        self.sprint_id = sprint_id
        self.person_name = person_name

class sprintpeoplerecord(db.Model):
    __tablename__ = 'sprintpeoplerecord'

    id = Column(Integer, primary_key=True)
    sprintpeople_id = Column(Integer, nullable=False)
    sprint_day = Column(Integer, nullable=False)
    sprint_daystatus = Column(Integer, nullable=False)

    def __init__(self, sprintpeople_id, sprint_day, sprint_daystatus):
        self.sprintpeople_id = sprintpeople_id
        self.sprint_day = sprint_day
        self.sprint_daystatus = sprint_daystatus

class daytypes(db.Model):
    __tablename__ = 'daytypes'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, nullable=False)
    daytype_status = Column(String(3), nullable=False)
    daytype_name = Column(String(100), nullable=False)
    daytype_color = Column(String(6), nullable=False)
    daytype_day = Column(Float, nullable=False)
    daytype_order = Column(Integer, nullable=False)

    def __init__(self, project_id, daytype_status, daytype_name, daytype_color, daytype_day, daytype_order):
        self.project_id = project_id
        self.daytype_status = daytype_status
        self.daytype_name = daytype_name
        self.daytype_color = daytype_color
        self.daytype_day = daytype_day
        self.daytype_order = daytype_order
