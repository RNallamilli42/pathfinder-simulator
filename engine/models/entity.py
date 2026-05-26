from pydantic import BaseModel, Field
from enum import Enum 

class ProficiencyRank(Enum):
    """Enums of the modifier for each proficiency level"""
    UNTRAINED = 0
    TRAINED = 2
    EXPERT = 4
    MASTER = 6
    LEGENDARY = 8

class Size(Enum):
    """Enums of the size of an entity"""
    TINY = "tiny"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    HUGE = "huge"
    GARGANTUAN = "gargantuan"

class Conditions(Enum):
    """Enums of conditions that can inflict an entity"""
    BLINDED = "blinded"
    BROKEN = "broken"
    CLUMSY = "clumsy"
    CONCEALED = "concealed"
    CONFUSED = "confused"
    CONTROLLED = "controlled"
    DAZZLED = "dazzled"
    DEAFENED = "deafened"
    DOOMED = "doomed"
    DRAINED = "drained"
    DYING = "dying"
    ENCUMBERED = "encumbered"
    ENFEEBLED = "enfeebled"
    FASCINATED = "fascinated"
    FATIGUED = "fatigued"
    FLEEING = "fleeing"
    FRIENDLY = "friendly"
    FRIGHTENED = "frightened"
    GRABBED = "grabbed"
    HELPFUL = "helpful"
    HIDDEN = "hidden"
    HOSTILE = "hostile"
    IMMOBILIZED = "immobilized"
    INDIFFERENT = "indifferent"
    INVISIBLE = "invisible"
    OBSERVED = "observed"
    OFFGUARD = "off-guard"
    PARALYZED = "paralyzed"
    PERSISTENTDAMAGE = "persistent-damage"
    PETRIFIED = "petrified"
    PRONE = "prone"
    QUICKENED = "quickened"
    RESTRAINED = "restrained"
    SICKENED = "sickened"
    SLOWED = "slowed"
    STUNNED = "stunned"
    STUPEFIED = "stupefied"
    UNCONSCIOUS = "unconscious"
    UNDETECTED = "undetected"
    UNFRIENDLY = "unfriendly"
    UNNOTICED = "unnoticed"
    WOUNDED = "wounded"

class DamageTypes(Enum):
    """Enums for each damage type that can affect an entity"""
    PHYSICAL = "physical"
    ENERGY = "energy"
    SPIRIT = "spirit"
    MENTAL = "mental"
    POISON = "poison"
    BLEED = "bleed"
    PRECISION = "precision"
    # PRECIOUS METALS CAN SOMETIMES BYPASS RESISTANCES TO CERTAIN DAMAGE TYPES

class AbilityScores(BaseModel):
    """Represent the ability scores of an entity"""
    strength : int = 0
    dexterity : int = 0
    constitution : int = 0
    intelligence : int = 0
    wisdom : int = 0
    charisma : int = 0

class TotalModifier(BaseModel):
    """Represents the total modifier given for a skill or save with proficiency, ability score, and item bonus"""
    ability : str
    proficiency : ProficiencyRank = ProficiencyRank.UNTRAINED
    item_bonus : int = 0

class LoreModifier(TotalModifier):
    """An extension of TotalModifier that allows Lores to have different names"""
    name : str | None = None
    ability : str = "intelligence"

class Skills(BaseModel):
    """Represents all of the entities different skills through TotalModifier and LoreModifier"""
    acrobatics : TotalModifier = TotalModifier(ability = "dexterity")
    arcana : TotalModifier = TotalModifier(ability = "intelligence")
    athletics : TotalModifier = TotalModifier(ability = "strength")
    crafting : TotalModifier = TotalModifier(ability = "intelligence")
    deception : TotalModifier = TotalModifier(ability = "charisma")
    diplomacy : TotalModifier = TotalModifier(ability = "charisma")
    intimidation : TotalModifier = TotalModifier(ability = "charisma")
    lore : list[LoreModifier] = Field(default_factory = list)
    medicine : TotalModifier = TotalModifier(ability = "wisdom")
    nature : TotalModifier = TotalModifier(ability = "wisdom")
    occultism : TotalModifier = TotalModifier(ability = "intelligence")
    performance : TotalModifier = TotalModifier(ability = "charisma")
    religion : TotalModifier = TotalModifier(ability = "wisdom")
    society : TotalModifier = TotalModifier(ability = "intelligence")
    stealth : TotalModifier = TotalModifier(ability = "dexterity")
    survival : TotalModifier = TotalModifier(ability = "wisdom")
    thievery : TotalModifier = TotalModifier(ability = "dexterity")

class Saves(BaseModel):
    """Represents an entity's different saves using TotalModifier"""
    fortitude : TotalModifier = TotalModifier(ability = "constitution")
    reflex : TotalModifier = TotalModifier(ability = "dexterity")
    will : TotalModifier = TotalModifier(ability = "wisdom")

class MovementSpeeds(BaseModel):
    """Represents an entity's different movement speeds"""
    speed : int | None = None
    burrow_speed : int | None = None
    climb_speed : int | None = None
    fly_speed  : int | None = None
    swim_speed : int | None = None