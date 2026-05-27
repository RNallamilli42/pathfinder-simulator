import pytest
from pydantic import ValidationError
from engine.models.entity import (
    ProficiencyRank, 
    Size, 
    Conditions, 
    DamageTypes, 
    AbilityScores,
    TotalModifier, 
    LoreModifier, 
    Skills, 
    Saves, 
    MovementSpeeds, 
    Entity
)

def test_Enums():
    assert ProficiencyRank.TRAINED.value == 2
    assert ProficiencyRank.MASTER.value == 6
    assert ProficiencyRank.LEGENDARY.value == 8
    assert Size.TINY.value == "tiny"
    assert Size.HUGE.value == "huge"
    assert Conditions.BLINDED.value == "blinded"
    assert Conditions.PERSISTENTDAMAGE.value == "persistent-damage"
    assert Conditions.OFFGUARD.value == "off-guard"

def test_AbilityScores():
    test = AbilityScores(strength = 4, charisma = 0, dexterity = 7, wisdom = -3)
    assert test.strength == 4
    assert test.dexterity == 7
    assert test.constitution == 0
    assert test.intelligence == 0
    assert test.wisdom == -3
    assert test.charisma == 0

def test_TotalModifier():
    test = TotalModifier(ability = "dexterity")
    assert test.ability == "dexterity"
    assert test.proficiency == ProficiencyRank.UNTRAINED
    assert test.item_bonus == 0
    with pytest.raises(ValidationError):
        test = TotalModifier()

def test_LoreModifier():
    test = LoreModifier()
    assert test.name == None
    assert test.ability == "intelligence"
    assert test.proficiency == ProficiencyRank.UNTRAINED
    assert test.item_bonus == 0

def test_Skills_Saves_Movement():
    testSkills = Skills()
    testSaves = Saves()
    testMovement = MovementSpeeds()
    assert testSkills.acrobatics.ability == "dexterity"
    assert testSkills.nature.ability == "wisdom"
    assert testSkills.deception.ability == "charisma"
    assert testSaves.fortitude.ability == "constitution"
    assert testSaves.reflex.ability == "dexterity"
    assert testSaves.will.ability == "wisdom"
    assert testMovement.speed == None
    assert testMovement.burrow_speed == None
    assert testMovement.climb_speed == None
    assert testMovement.fly_speed == None
    assert testMovement.swim_speed == None

class TestEntity():
    def test_Entity_defaults(self):
        test = Entity()
        assert test.name == None
        assert test.level == 0
        assert test.size == Size.MEDIUM
        assert test.ability_scores == AbilityScores()
        assert test.saves == Saves()
        assert test.skills == Skills()
        assert test.movement == MovementSpeeds()
        assert test.current_hp == 0
        assert test.max_hp == 0
        assert test.ac == 10
        assert test.perception.ability == "wisdom"
        assert test.conditions == {}
        assert test.resistances == {}
        assert test.weaknesses == {}
        assert test.actions == 3
        assert test.reactions == 1

    def test_valid_values(self):
        test = Entity(level = 17, ability_scores = AbilityScores(dexterity = 7))
        assert test.level == 17
        assert test.ability_scores.dexterity == 7
        assert test.ac == 17
        
    @pytest.mark.parametrize("level", [-1, 21])
    def test_invalid_level(self, level):
        with pytest.raises(ValidationError):
            Entity(level = level)

    def test_invalid_current_hp(self):
        with pytest.raises(ValidationError):
            Entity(current_hp = -1)

    def test_invalid_max_hp(self):
        with pytest.raises(ValidationError):
            Entity(max_hp = -1)
    
    def test_invalid_actions(self):
        with pytest.raises(ValidationError):
            Entity(actions = -1)
    
    def test_invalid_reactions(self):
        with pytest.raises(ValidationError):
            Entity(reactions = -1)