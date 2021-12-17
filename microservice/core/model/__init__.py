# TODO: En este paquete van los clases que representan los datos que va a
#       manejar el micro servicio. Pueden estar en este archivo o estar
#       ordenados en diferentes archivos dentro de este paquete.

from typing import Any, List
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from bson import ObjectId


@dataclass_json
@dataclass
class User:
    """User model."""

    email: str = None
    hashed_password: str = None
    is_active: bool = None

    def to_dict(self):
        return {
            "email": self.email,
            "is_active": self.is_active
        }

    def __repr__(self):
        return f"email=\"{self.email}\", " \
               f"is_active={self.is_active})>"
