from database import get_db
from database.models import UserJob
from datetime import datetime


def register_job_db(user_id, job_title, job_city, jobs_tag=None):
    db = next(get_db())
    new_job = UserJob(user_id=user_id, job_title=job_title, job_city=job_city, reg_date=datetime.now(),
                      update_time=datetime.now(), jobs_tag=jobs_tag)
    db.add(new_job)
    db.commit()
    return True


def get_user_jobs_db(user_id):
    db = next(get_db())
    if user_id:
        exact_user_job = db.query(UserJob).filter_by(user_id=user_id).first()
        return exact_user_job
