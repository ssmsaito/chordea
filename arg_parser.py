import argparse

parser = argparse.ArgumentParser()
parser.add_argument('chord_name', type=str, help='コード名')
parser.add_argument('--fret-from', type=int, required=False, default=0, help='フレット最小値')
parser.add_argument('--fret-to', type=int, required=False, default=20, help='フレット最大値')
parser.add_argument('--fret-range', type=int, required=False, default=3, help='フレット数の幅')
parser.add_argument('--min-strings', type=int, required=False, default=3, help='演奏する弦の最小本数')
parser.add_argument('--ignore-root', action='store_true', help='ルート音が違っても出力')
parser.add_argument('--disable-open-string', action='store_true', help='ポジション外の開放弦を無効化する')
parser.add_argument('--tuning', type=lambda l: l.split(','), required=False, default=['E','A','D','G','B','E'], help='ギターチューニング')

args = parser.parse_args()
