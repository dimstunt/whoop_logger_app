from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class EventType(Enum):
    SLEEP = "sleep"
    AIRPLANE = "airplane"
    ALCOHOL = "alcohol"
    CAFFEINE = "caffeine"
    MARIJUANA = "marijuana"
    MASTURBATION = "masturbation"
    SEX = "sex"
    TOBACCO = "tobacco"
    MASSAGE = "massage"
    MEDITATION = "meditation"
    SAUNA = "sauna"
    MELATONIN = "melatonin"


class EventCreate(BaseModel):
    event_dttm: datetime.datetime
    quantity: int
    event_type: EventType
    additional_info: dict
