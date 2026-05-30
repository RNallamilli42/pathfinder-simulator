from pydantic import Field
from .entity import Entity
from .ancestry import Ancestry
from .background import Background
from .char_class import ArmorProficiencies, WeaponProficiencies, CharacterClass

class PlayerCharacter(Entity):
    """A blueprint for creating Player characters"""
    ancestry : Ancestry
    background : Background
    player_class : CharacterClass
    hero_point : int = Field(0, ge = 0, le = 3)
    chosen_boosts : list[str] = Field(default_factory = list)
    chosen_languages : list[str] = Field(default_factory = list)
    weapon_proficiencies : WeaponProficiencies = WeaponProficiencies()
    armor_proficiencies : ArmorProficiencies = ArmorProficiencies()

    def model_post_init(self, __context: any):
        super().model_post_init(__context)
        self.__dict__["max_hp"] = self.ancestry.hp + self.player_class.hp_per_level + self.ability_scores.constitution
        self.__dict__["current_hp"] = self.max_hp
        self.__dict__["weapon_proficiencies"] = self.player_class.weapon_proficiencies
        self.__dict__["armor_proficiencies"] = self.player_class.armor_proficiencies