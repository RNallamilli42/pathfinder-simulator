from pydantic import BaseModel, Field
from enum import Enum
from .entity import Size

class Vision(Enum):
    """Enums for the different types of vision"""
    NORMAL = "normal"
    LOWLIGHT = "low-light"
    DARKVISION = "darkvision"


class Ancestry(BaseModel):
    """Immutable template for ancestries"""
    name : str
    hp : int = Field(ge = 0)
    size : Size
    speed : int = Field(ge = 0)
    restricted_boosts : list[list[str]] = Field(default_factory = list)
    free_boosts : int = Field(ge = 0)
    flaws : list[str] = Field(default_factory = list)
    base_languages : list[str] = Field(default_factory = list)
    bonus_languages : list[str] = Field(default_factory = list)
    base_vision : Vision = Vision.NORMAL
    # Replace these str with Feat when Feat is made
    traits : list[str] = Field(default_factory = list)
    ancestry_feats : list[str] = Field(default_factory = list)