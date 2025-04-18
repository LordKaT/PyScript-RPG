from logic.entity import Entity

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
    def physical_attack(self, attacker: Entity = None, defender: Entity = None) -> int:
        return 0

    def magic_attack(self, attacker: Entity = None, defender: Entity = None, spell: any = None) -> int:
        return 0
