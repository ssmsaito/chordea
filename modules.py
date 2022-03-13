from consts import SHARP_NOTES, FLAT_NOTES

def is_flat_note(note: str):
    return 'b' in note

def get_note_index(note: str):
    return FLAT_NOTES.index(note) if is_flat_note(note) else SHARP_NOTES.index(note)

def get_note_by_index(index: int, type='sharp'):
    return SHARP_NOTES[index] if type=='sharp' else FLAT_NOTES[index]

def get_note_by_fret_number(string_index: int, fret: int, tuning: list[str]):
    return step_by_half_tone(tuning[string_index], fret)

def step_by_half_tone(note: str, steps: int = 1, return_note: bool = True):
    index = (get_note_index(note) + steps)%12
    return get_note_by_index(index, 'flat' if is_flat_note(note) else 'sharp') if return_note else index

def get_chord_factors(chord_name):
    root_note = chord_name
    triad = [root_note, step_by_half_tone(root_note, +4), step_by_half_tone(root_note, +7)]
    return triad

def has_valid_root(chord_name: str, chord_frets: list[int], tuning: list[str]):
    for string_index, fret in enumerate(chord_frets):
        if fret is None: continue
        else:
            # FIXME
            return get_note_by_fret_number(string_index, fret, tuning) == chord_name
    return False

def get_min_fret(chord_frets):
    return min([fret for fret in chord_frets if fret is not None])

def get_max_fret(chord_frets):
    return max([fret for fret in chord_frets if fret is not None])

def print_diagram(chord_frets: list[int], fret_range: int, tuning: list[str]):
    min_fret = get_min_fret(chord_frets)
    if min_fret == 0:
        min_fret = get_min_fret([fret if fret is not None and fret>0 else None for fret in chord_frets])
    max_fret = get_max_fret(chord_frets)
    for string_index, fret in reversed(list(enumerate(chord_frets))):
        if fret is None:
            line = '   x'
        else:
            line = get_note_by_fret_number(string_index, fret, tuning).ljust(3)
            if fret == 0:
                line += 'o'
            else:
                line += ' '
        for offset in range(max(fret_range, max_fret-min_fret)):
            if fret is not None and offset == fret-min_fret:
                line += '|-*-'
            else:
                line += '|---'
        line += '|'
        print(line)
    fret_number_line = '    '
    for offset in range(max(fret_range, max_fret-min_fret)):
        fret_number_line += f'  {offset+min_fret}'.ljust(4)
    print(fret_number_line)
    print('')
