"""

A Python dataclass representation of the data publisher PANGAEA's data model, 
based on https://wiki.pangaea.de/wiki/data_model.

"""

from typing import List, Optional
from enum import Enum
from dataclasses import dataclass
import datetime

@dataclass    
class Staff:
    # https://wiki.pangaea.de/wiki/Staff
    last_name: str
    first_name: str
    phone: str = None
    email: str = None
    orcid: str = None
    institute: str = None
    url: str = None

@dataclass
class Project:
    # https://wiki.pangaea.de/wiki/Project
    name: str
    acronym: str = None
    type: str = None
    coordinator : Staff = None
    institute : str = None
    url : str = None

@dataclass
class Campaign:
    # https://wiki.pangaea.de/wiki/Campaign
    label : str

    
@dataclass
class Method:
    # https://wiki.pangaea.de/wiki/Method
    name: str
    abbreviation : str
    url : str = None


@dataclass
class Event:
    # https://wiki.pangaea.de/wiki/Event
    label : str
    latitude : float
    longitude : float    
    datetime : datetime.datetime
    optional_label : str = None
    method : Method = None
    elevation : float = None
    project : Project = None
    location : str = None
    comment : str = None
    uri : str = None

    