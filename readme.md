# Chordea: Command line tool for generating guitar chord ideas in diagrams

## Requirements

Python 3

## Usage
```
python main.py [-h] [--fret-from FRET_FROM] [--fret-to FRET_TO] [--fret-range FRET_RANGE] [--min-strings MIN_STRINGS] [--ignore-root] [--disable-open-string] [--tuning TUNING] chord_name

kositional arguments:
  chord_name            Chord name

optional arguments:
  -h, --help            show this help message and exit
  --fret-from FRET_FROM
                        Minimum required number for fret position
  --fret-to FRET_TO     Maximum required number for fret position
  --fret-range FRET_RANGE
                        Fret range for diagram suggestion
  --min-strings MIN_STRINGS
                        Minimum required number of played strings
  --ignore-root         Allow non-root tone to be the lowest tone if specified
  --disable-open-string
                        Do not allow to have open strings at higher positions if specified
  --tuning TUNING       Guitar tuning (comma-separated)
```

## Output example

```
$ python main.py --fret-to 5 C
E  o|---|---|---|
C   |-*-|---|---|
G  o|---|---|---|
E   |---|-*-|---|
C   |---|---|-*-|
   x|---|---|---|
      1   2   3

G   |---|---|-*-|
C   |-*-|---|---|
G  o|---|---|---|
E   |---|-*-|---|
C   |---|---|-*-|
   x|---|---|---|
      1   2   3

G   |---|-*-|---|
   x|---|---|---|
G  o|---|---|---|
E   |-*-|---|---|
C   |---|-*-|---|
   x|---|---|---|
      2   3   4
```

```
python main.py --fret-to 7 --tuning D,A,D,G,A,D D
D  o|---|---|---|
A  o|---|---|---|
A   |-*-|---|---|
D  o|---|---|---|
   x|---|---|---|
   x|---|---|---|
      2   3   4

D  o|---|---|---|
A  o|---|---|---|
A   |-*-|---|---|
D  o|---|---|---|
A  o|---|---|---|
D  o|---|---|---|
      2   3   4

F#  |-*-|---|---|
D   |---|-*-|---|
   x|---|---|---|
F#  |-*-|---|---|
D   |---|-*-|---|
   x|---|---|---|
      4   5   6
```
