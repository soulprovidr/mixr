# mixr
> Generate an MP3 mix from the command line.

mixr leverages the excellent [pydub](https://github.com/jiaaro/pydub) library to generate a mix from an M3U playlist file, with crossfading and normalization.

```
$ mixr -h
usage: mixr [-h] [--bitrate <bitrate=320k>] [--crossfade <seconds=2>] [--fade-out <seconds=20>] [--gain <dBFS=-10.0>] [--intro] [--output <filename>] <filename>

Generate a mix from an M3U playlist.

positional arguments:
  <filename>            Path to the playlist file.

optional arguments:
  -h, --help            show this help message and exit
  --bitrate <bitrate=320k>
                        Bitrate of output file.
  --crossfade <seconds=2>
                        Crossfade duration (in seconds).
  --fade-out <seconds=20>
                        Fade out duration (in seconds).
  --gain <dBFS=-10.0>   Target gain level for mix.
  --intro               Intro mode (i.e. don't crossfade first track).
  --output <filename>   Path to the output file.
```

## Installation

**OS X & Linux:**

1. Install [Python](https://www.python.org/downloads/).
2. Run the following commands:

    ```
    $ git clone https://github.com/soulprovidr/mixr.git
    $ cd mixr
    $ pip install .
    ```

## Usage example

**playlist.m3u**
```
#EXTM3U
#EXTINF:345,11 2Pac - Can U Get Away (Me Against The World)
/storage/Music/staging/2Pac - Me Against The World/2Pac - Can U Get Away.mp3
#EXTINF:279,9 2Pac - Dear Mama (Me Against The World)
/storage/Music/staging/2Pac - Me Against The World/2Pac - Dear Mama.mp3
#EXTINF:294,10 2Pac - It Ain't Easy (Me Against The World)
/storage/Music/staging/2Pac - Me Against The World/2Pac - It Ain't Easy.mp3
```

```
$ mixr playlist.txt --bitrate 128kbps
Mix successfully exported as: Sep-04-2019-23:49:32.mp3
```

## License

Distributed under the GNU GPLv3 license. See ``LICENSE`` for more information.