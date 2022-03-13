import argparse

parser = argparse.ArgumentParser()
parser.add_argument('chord_name', type=str, help='Chord name')
parser.add_argument('--fret-from', type=int, required=False, default=0, help='Minimum required number for fret position')
parser.add_argument('--fret-to', type=int, required=False, default=20, help='Maximum required number for fret position')
parser.add_argument('--fret-range', type=int, required=False, default=3, help='Fret range for diagram suggestion')
parser.add_argument('--min-strings', type=int, required=False, default=3, help='Minimum required number of played strings')
parser.add_argument('--ignore-root', action='store_true', help='Allow non-root tone to be the lowest tone if specified')
parser.add_argument('--disable-open-string', action='store_true', help='Do not allow to have open strings at higher positions if specified')
parser.add_argument('--tuning', type=lambda l: l.split(','), required=False, default=['E','A','D','G','B','E'], help='Guitar tuning (comma-separated)')

args = parser.parse_args()
