from pydantic import BaseModel, Field, model_validator
from typing import Self

class Background(BaseModel):
    """Blueprint for creating a background"""
    name : str
    skill : list[str] = Field(default_factory =  list)
    restricted_boosts : list[list[str]] = Field(default_factory = list)
    free_boosts : int = Field(ge = 0)
    skill_feat : str | None = None

    @model_validator(mode = "after")
    def validate_skills(self) -> Self:
        if len(self.skill) > 2:
            raise ValueError("Background can only train up to 2 skills")
        return self