from database.models import User
from database import get_db
from datetime import datetime


def register_user_db(name, phone, user_location, tg_id=None):
    db = next(get_db())
    checker = check_phone_db(name, phone, user_location)
    if checker == True:
        new_user = User(name=name, phone=phone, user_location=user_location, tg_id=tg_id, reg_date=datetime.now(),
                        update_time=datetime.now())
        db.add(new_user)
        db.commit()
        return new_user.user_id
    return checker


def check_user_db(tg_id):
    db = next(get_db())
    check = db.query(User).filter_by(tg_id=tg_id).all()
    if check:
        return True
    else:
        return False


def check_phone_db(name, phone, user_location):
    db = next(get_db())
    # checker_name = db.query(User).filter_by(name=name).first()
    checker_phone = db.query(User).filter_by(phone=phone).first()
    # checker_user_location = db.query(User).filter_by(user_location).first()
    # if checker_name:
    #    return "Нет имени"
    if checker_phone:
        return "Номер телефона занят"
    # elif checker_user_location:
    #    return "Нету локации"
    return True


def profile_info_db(user_id):
    db = next(get_db())
    user_info = db.query(User).filter_by(user_id=user_id).first()
    if user_info:
        return user_info
    return False


# change data
def change_user_data_db(user_id, changeable_info, new_data):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        try:
            if changeable_info == "name":
                user.name = new_data
                db.commit()
                return True
            elif changeable_info == "phone":
                user.phone = new_data
                db.commit()
                return True
        except:
            return "Unfortunately at this moment change of data unavailable"
    return False


def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users

