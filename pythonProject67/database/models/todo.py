from pythonProject67.database.engine import db

class Task(db.Model):
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)