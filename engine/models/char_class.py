from pydantic import BaseModel, Field
from .entity import ProficiencyRank, Saves

class WeaponProficiencies(BaseModel):
    """Represents the proficiency ranks of different weapon categories for one entity"""
    unarmed: ProficiencyRank = ProficiencyRank.UNTRAINED
    simple: ProficiencyRank = ProficiencyRank.UNTRAINED
    martial: ProficiencyRank = ProficiencyRank.UNTRAINED
    advanced: ProficiencyRank = ProficiencyRank.UNTRAINED

class ArmorProficiencies(BaseModel):
    """Represents the proficiency ranks of different armor categories for one entity"""
    unarmored: ProficiencyRank = ProficiencyRank.UNTRAINED
    light: ProficiencyRank = ProficiencyRank.UNTRAINED
    medium: ProficiencyRank = ProficiencyRank.UNTRAINED
    heavy: ProficiencyRank = ProficiencyRank.UNTRAINED

class CharacterClass(BaseModel):
    """Blueprint for a player character's class"""
    name : str
    hp_per_level : int = Field(ge = 0)
    key_ability : list[str]
    perception : ProficiencyRank = ProficiencyRank.UNTRAINED
    saves : Saves = Saves()
    weapon_proficiencies : WeaponProficiencies = WeaponProficiencies()
    armor_proficiencies : ArmorProficiencies = ArmorProficiencies()
    free_skills : int = 0
    required_skills : list[str] = Field(default_factory = list)
    is_spellcaster : bool
    spell_dc : ProficiencyRank | None = None
    spell_attack : ProficiencyRank | None = None
    unique_mechanic : str # placeholder - Will replace with either a unique class or classes
    class_feats : list[str] = Field(default_factory = list)