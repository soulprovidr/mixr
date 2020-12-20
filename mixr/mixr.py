import argparse
import datetime
import json
from urllib.parse import unquote

from pydub import AudioSegment
from pydub.playback import play

# Generate a default filename, based on the current datetime.
def get_default_output_name():
    return '{0}.mp3'.format(datetime.datetime.today().strftime('%b-%d-%Y-%H:%M:%S'))

# Extract artist + title from each playlist entry.
def get_audio_meta(playlist_lines):
    # #EXTINF:345,2Pac - Can U Get Away (Me Against The World)
    is_meta = lambda str: bool(str) and str.startswith('#EXTINF')
    entries = filter(is_meta, playlist_lines)
    # 2Pac - Can U Get Away (Me Against The World)
    strip_headers = lambda str: str.split(',', 1)[1]
    entries = map(strip_headers, entries)
    # { 'artist': '2Pac', 'title': 'Can U Get Away (Me Against The World)' }
    create_dict = lambda entry: dict([
        ('artist', entry.split(' - ')[0]),
        ('title', entry.split(' - ')[1])
    ])
    entries = map(create_dict, entries)
    return list(entries)

# Create a list of AudioSegments in the order listed in the `playlist` file.
def get_audio_segments(playlist_lines):
    is_file_path = lambda str: bool(str) and str[0] != '#'
    file_list = filter(is_file_path, playlist_lines)
    file_list = map(unquote, file_list)
    return [
        AudioSegment.from_mp3(file_path) for file_path in file_list
    ]


# Adjust the volume to match the target gain level.
def normalize(sound, target_dBFS):
    change = target_dBFS - sound.dBFS
    return sound.apply_gain(change)


###############################################################################


parser = argparse.ArgumentParser(
    description='Generate a mix from an M3U playlist.')
parser.add_argument('playlist', metavar='<filename>',
                    help='Path to the playlist file.')
parser.add_argument('--bitrate', metavar='<bitrate=320k>', default='320k',
                    type=str, help='Bitrate of output file.')
parser.add_argument('--crossfade', metavar='<seconds=2>', default=2,
                    type=int, help='Crossfade duration (in seconds).')
parser.add_argument('--fade-out', metavar='<seconds=20>', default=20,
                    type=int, help='Fade out duration (in seconds).')
parser.add_argument('--gain', metavar='<dBFS=-10.0>', type=float, default=-10.0,
                    help='Target gain level for mix.')
parser.add_argument('--output', metavar='<filename>',
                    default=get_default_output_name(),
                    help='Path to the output file.')
parser.add_argument('--json', action='store_true', help='Print metadata to JSON file.')


###############################################################################

# Parse arguments and run the program.
def main():
    args = parser.parse_args()

    audio_meta = []
    audio_segments = []
    mix = AudioSegment.empty()

    with open(args.playlist) as f:
        playlist_lines = f.read().split("\n")
        audio_segments = get_audio_segments(playlist_lines)
        if args.json:
            audio_meta = get_audio_meta(playlist_lines)


    # Concatenate audio_segments with specified crossfade duration.
    for i in range(len(audio_segments)):
        # Update corresponding audio_meta entry with track start time.
        if args.json:
            audio_meta[i]['start'] = len(mix)
        # Normalize audio segment.
        segment = audio_segments[i]
        segment = normalize(segment, args.gain)
        # Append segment to mix.
        crossfade_duration = args.crossfade * 1000 if i != 0 else 0
        mix = mix.append(segment, crossfade=crossfade_duration)

    # Fade the mix out.
    fadeout_duration = args.fade_out * 1000
    mix = mix.fade_out(fadeout_duration)

    # Save the mix as an .mp3 file.
    output = open(args.output, 'wb')
    mix.export(output, format='mp3', bitrate=args.bitrate)
    print('Mix successfully exported as: {0}'.format(args.output))

    # Save JSON metadata
    if args.json:
        json_output = open(args.output + '.json', 'w', encoding='utf8')
        json.dump(audio_meta, json_output)


###############################################################################


if __name__ == "__main__":
    main()
