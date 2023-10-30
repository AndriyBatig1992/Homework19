from .db import session
from .models import User
from sqlalchemy.exc import SQLAlchemyError


def get_user(login):
    user = session.query(User).filter(User.login == login).first()
    return user


def create_record(model_class, **kwargs):
    try:
        with session.begin_nested():
            last_record = session.query(model_class).order_by(model_class.id.desc()).first()
            if last_record:
                new_id = last_record.id + 1
            else:
                new_id = 1
            record = model_class(id=new_id, **kwargs)
        session.add(record)
        session.commit()
        print(f"{model_class.__name__} created successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error creating {model_class.__name__}: {e}")
    finally:
        session.close()


def list_records(model_class, user=None):
    records = session.query(model_class).all()
    if hasattr(model_class, 'id') and hasattr(model_class, 'name'):
        records_dict = {record.id: record.name for record in records}
        for record_id, record_name in records_dict.items():
            print(f"{record_id}: {record_name}")
    else:
        for record in records:
            attributes = [f'{key}: {getattr(record, key)}' for key in record.__dict__.keys() if
                              not key.startswith('_')]
            print(f"{model_class.__name__} ID: {record.id}, {', '.join(attributes)}")


def remove_record(model_class, record_id, user):
    try:
        record = session.query(model_class).filter(model_class.id == record_id).first()
        if record:
            session.delete(record)
            session.commit()
            session.close()
            print(f"{model_class.__name__} {record_id} removed successfully.")
        else:
            print(f"{model_class.__name__} {record_id} not found.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error removing {model_class.__name__}: {e}")
        return False


def update_record(model_class, record_id, user, **kwargs):
    try:
        record = session.query(model_class).filter(model_class.id == record_id).first()
        if record:
            # Оновлюємо властивості запису на нові значення з kwargs
            for key, value in kwargs.items():
                setattr(record, key, value)
            session.commit()
            print(f"{model_class.__name__} {record_id} updated successfully.")
        else:
            print(f"{model_class.__name__} {record_id} not found.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error updating {model_class.__name__}: {e}")
    finally:
        session.close()


