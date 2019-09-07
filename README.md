# mixr
> Generate an MP3 mix from the command line.

mixr leverages the excellent [pydub](https://github.com/xxx/pydub) library to concatenate a list of MP3 files, with crossfading and normalization.

```
$ mixr -h
usage: mixr [-h] [--crossfade <seconds=2>] [--fade-out <seconds=20>]
            [--gain <dBFS=-20.0>] [--intro] [--output <filename>]
            <tracklist>

Generate an MP3 mix from the command line.

positional arguments:
  <tracklist>            Path to the tracklist file.

optional arguments:
  -h, --help            show this help message and exit
  --crossfade <seconds=2>
                        Crossfade duration (in seconds).
  --fade-out <seconds=20>
                        Fade out duration (in seconds).
  --gain <dBFS=-20.0>   Target gain level for mix.
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

**tracklist.txt**
```
/home/soulprovidr/Music/Michael Jackson - Rock With You.mp3
/home/soulprovidr/Music/Michael Henderson - Let Love Enter.mp3
/home/soulprovidr/Music/Michael Franks - Down In Brazil.mp3
/home/soulprovidr/Music/Quincy Jones - Betcha' Wouldn't Hurt Me.mp3
```

```
$ mixr tracklist.txt
Mix successfully exported as: Sep-04-2019-23:49:32.mp3
```

## License

Distributed under the GNU GPLv3 license. See ``LICENSE`` for more information.