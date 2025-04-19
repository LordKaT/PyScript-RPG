from logic.entity import Entity
import math, random

class Battle:
    def __init__(self):
        pass

    '''
        physical_attack

        Inputs:
            attacker
            defender

        Outputs:
            Damage results.
                >= 0, defender takes physical damage
                < 0, miss or other flag
        
        Process:
            TBD

    '''
    def physical_attack(self, attacker: Entity = None, defender: Entity = None) -> list:
        a_d = attacker.stats.derived()
        d_d = defender.stats.derived()

        atk_low = random.uniform(0, a_d["attack"] * 0.25)
        acc_low = random.uniform(0, a_d["accuracy"] * 0.25)

        attack = random.uniform(atk_low, a_d["attack"])
        accuracy = random.uniform(acc_low, a_d["accuracy"])

        def_low = random.uniform(0, d_d["defense"] * 0.25)
        eva_low = random.uniform(0, d_d["evasion"] * 0.25)

        defense = random.uniform(def_low, d_d["defense"])
        evasion = random.uniform(eva_low, d_d["evasion"])

        if accuracy < evasion:
            return ["miss", 0]
        
        damage_type = "normal"
        damage_mod = random.uniform(0, a_d["damage_modifier"])        
        damage = (a_d["attack"] + damage_mod) - d_d["defense"]
        if (100.0 - a_d["crit_chance"]) < random.uniform(0, 100):
            damage *= a_d["crit_damage"]
            damage_type = "crit"
        
        damage = math.floor(damage) if damage > 0 else 0

        return [damage_type, damage]

    def magic_attack(self, attacker: Entity = None, defender: Entity = None, spell: any = None) -> int:
        return 0
