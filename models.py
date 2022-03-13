from modules import step_by_half_tone

class Chord:
    def __init__(self, name):
        import re
        result = re.match('^([ABCDEFG][b|#]?)(m?)([a-z0-9M\-]*)(\/[ABCDEFG][b|#]?)?$', name)
        if result is None:
            raise Exception('Invalid chord name')
        groups = result.groups()
        self.name = name
        self.root = groups[0]
        self.is_minor = groups[1] == 'm'
        self.base = groups[0]+groups[1]
        self.type = groups[2]
        self.on = groups[3][1:] if groups[3] else None
        self.triad = self._get_triad()
        self.factors = self.triad # FIXME

    def _get_triad(self):
        third_offset = 0
        fifth_offset = 0
        if self.is_minor or 'dim' in self.type:
            third_offset = -1
        elif 'sus4' in self.type:
            third_offset = 1

        if 'dim' in self.type or '-5' in self.type:
            fifth_offset = -1
        elif 'aug' in self.type:
            fifth_offset = 1

        third = step_by_half_tone(self.root, 4+third_offset)
        fifth = step_by_half_tone(self.root, 7+fifth_offset) 
        return [self.root, third, fifth]
