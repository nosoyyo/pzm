__help__ = '''
PinZimu 0.0.7 (default, Sep 18 2018, 20:39:16)
A simple tool for subtitles splicing of video captures.
Any problems: https://github.com/nosoyyo/pzm/issues

Usage:
  pzm <start> [end] [height]

Options:
  start                       Must indicate where to start.
  end                         Indicate where to end.
  height                      If `end` is specified, `height` will be ignored.

Example:
  pzm -200 -100
  pzm --start -200 --end -100
  pzm -200 --height 100

                '''
