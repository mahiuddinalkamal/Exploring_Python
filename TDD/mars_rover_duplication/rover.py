from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Rover(object):
    facing: str

    def go(self, instruction):
        compass = ['N', 'E', 'S', 'W']
        current = compass.index(self.facing)
        if instruction == 'R':
            return replace(self, facing=compass[(current + 1) % 4])
        else:
            if current == 0:
                current = 4
            return replace(self, facing=compass[(current - 1) % 4])
