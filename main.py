import copy

from arg_parser import args
from modules import (
        get_type,
        get_note_by_fret_number,
        step_by_half_tone,
        get_chord_factors,
        has_valid_root,
        get_min_fret,
        print_diagram
    )

def main():
    factors = get_chord_factors(args.chord_name)
    root_note = factors[0]
    chord_frets_all = set()
    for fret_from in range(args.fret_from, args.fret_to-args.fret_range+1):
        chord_frets = []
        for string_index, tuned_note in enumerate(args.tuning):
            note = None
            for fret_offset in range(args.fret_range+1) if fret_from==0 else range(args.fret_range):
                if step_by_half_tone(tuned_note, fret_from + fret_offset, type = get_type(root_note)) in factors:
                    note = fret_from + fret_offset
                    break
            if not args.disable_open_string and note is None and get_note_by_fret_number(string_index, 0, args.tuning, type = get_type(root_note)) in factors:
                note = 0
            chord_frets.append(note)
        chord_frets_all.add(tuple(chord_frets))

    _chord_frets_all = copy.deepcopy(chord_frets_all)
    for chord_frets in _chord_frets_all:
        _chord_frets = list(chord_frets)
        for string_index, fret in enumerate(_chord_frets):
            if string_index > 0:
                if len(args.tuning) - _chord_frets.count(None) >= args.min_strings:
                    chord_frets_all.add(tuple(_chord_frets))
                    _chord_frets[string_index] = None
                else:
                    break
            else:
                _chord_frets[string_index] = None

    for chord_frets in sorted([tuple(chord_frets) for chord_frets in chord_frets_all], key = lambda chord_frets: get_min_fret(chord_frets)):
        if args.ignore_root or has_valid_root(args.chord_name, chord_frets, args.tuning):
            print_diagram(args.chord_name, chord_frets, args.fret_range, args.tuning)

if __name__=='__main__':
    main()
