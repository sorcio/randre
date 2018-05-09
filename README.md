[![PyPI](https://img.shields.io/pypi/v/randre.svg)](https://pypi.org/project/randre)
[![Build Status](https://travis-ci.org/sorcio/randre.svg?branch=master)](https://travis-ci.org/sorcio/randre)

# randre
Generate random text from regular expression patterns

## What is this?

This is a Python module that exploits the internals of Python `re` module generate random text that matches a given regular expression pattern. I made this mostly for fun. Most patterns will work, but feel free to send feedback if you need something better. Contributions are welcome.


## Usage

```python
>>> randre(r'a[bc]+a')
'accbbccbbcccbcccbbbbcccccbbbccbcbbbbbbbcccbcbbccbcbbcbbbcbbccccbcbbccbbccba'
>>> randre(r'a[bc]+a')
'abbcbcbbbbbccbcbcccbbcbcbbccbcbcbcbbccca'
>>> randre(r'a[bc]+a')
'abbcbcbbbbcccbccba'
>>> randre(r'a([a-z]{1,3})\1')
'aufuf'
>>> randre(r'a([a-z]{1,3})\1')
'assussu'
>>> randre(r'INTERNALDATE "'
...         r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
...         r'(?P<year>[0-9][0-9][0-9][0-9])'
...         r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
...         r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
...         r'"')
'INTERNALDATE "36-Wap-0255 18:61:83 +0201"'
```


## Command line usage

```
$ python -m randre "(foo|bar)+"
barbarfoofoofoobarfoofoobarbarbarbarbarbarfoobarfoofoofoofoofoobarfoobarfoobarfoofoobarbarbarbarfoobarbarbarbarfoobarfoofoofoobarbarbarfoofoofoofoofoofoobarbarfoofoobarbarbarbarfoofoobarbarbarbarfoobarbarfoobarbarbarfoobarbarfoofoofoofoofoobarbarbarbarbarfoobarbarbar
```
