from sqlalchemy import (
    JSON,
    Table,
    Column,
    Integer,
    String,
    TIMESTAMP,
    func,
)

from database import metadata

event_class = Table(
    'event_class',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('event_type_name_ru', String),  # TODO: not null
    Column('event_type_name_en', String),  # TODO: not null
    Column('added_dttm', TIMESTAMP, server_default=func.now()),
)

event_type = Table(
    'event_type',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('event_class_id', Integer),
    Column('event_type_name_en', String),
    Column('event_type_name_ru', String),
    Column('added_dttm', TIMESTAMP, server_default=func.now()),
    Column('param', JSON, nullable=True),
)

event = Table(
    'event',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('event_dttm', TIMESTAMP),
    Column('event_qty', Integer, nullable=True),
    Column('added_dttm', TIMESTAMP, server_default=func.now()),
    Column('params', JSON, nullable=True),
)


def ResponseModel(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message,
    }
