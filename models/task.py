from sqlalchemy import ForeignKey
from utils.database import db


# Modelo Task
def relationship(param, back_populates):
    pass


class Task(db.Model):

    # Define colunas para a tabela
    task_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(80))

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    start_date = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    end_date = db.Column(db.DateTime, server_default=db.func.now())

    work_id = db.Column(db.Integer, ForeignKey('work.work_id'), nullable=False)
    relationship("Work", back_populates="tasks")

    employee_id = db.Column(db.Integer, ForeignKey('employee.employee_id'), nullable=False)
    relationship("Employee", back_populates="tasks")

    def __repr__(self):
        return (f"<Task ID: {self.task_id}, "
                f"Description: {self.description}, "
                f"Start Date: {self.start_date}, "
                f"End Date: {self.end_date}, "
                f"Status: {self.status}, "
                f"Work ID: {self.work_id}, "
                f"Employee ID: {self.employee_id}>")
