import re

import pytest

from randre import randre


def validate_pattern(pattern, runs=1000):
    # ugh I would love this to be deterministically testable
    # but this is better than nothing
    compiled = re.compile(pattern)
    for i in range(runs):
        generated = randre(pattern)
        match = compiled.fullmatch(generated)
        assert match is not None, '%r does not match %r' % (generated, pattern)


def test_randre_literal():
    assert randre('aaa') == 'aaa'
    assert randre('') == ''
    assert randre('x') == 'x'


def test_randre_category():
    validate_pattern(r'\d')
    validate_pattern(r'\D')
    validate_pattern(r'\s')
    validate_pattern(r'\S')
    validate_pattern(r'\w')
    validate_pattern(r'\W')


def test_randre_any():
    validate_pattern('.')


def test_randre_in():
    validate_pattern('[abcde]')
    validate_pattern('[^abcde]')


def test_randre_repeat():
    validate_pattern('a?')
    validate_pattern('a*')
    validate_pattern('a+')
    validate_pattern('a{10}')
    validate_pattern('a{1,10}')
    assert randre(r'a{0}') == ''
    assert randre(r'a{1}') == 'a'
    assert randre(r'a{5}') == 'aaaaa'


def test_randre_range():
    validate_pattern('[a-z]')
    validate_pattern('[^a-z]')
    validate_pattern(r'[\x00-\xff]')
    with pytest.raises(RuntimeError):
        validate_pattern('r[^\x00-\xff]')


def test_randre_subpattern():
    validate_pattern('(abcd)')
    validate_pattern('a([bc])+')


def test_randre_branch():
    validate_pattern('(aaa|bbb)')
    validate_pattern('(a{0,5}|b{0,5})')


def test_randre_groupref():
    assert randre(r'(abc) \1') == 'abc abc'
    validate_pattern(r'([a-z]+)\1')
    validate_pattern(r'(?P<hello>[a-z]+)(?P=hello)')


def test_randre_groupref_exists():
    assert randre(r'(aaa)(?(1)yes|no)') == 'aaayes'
    assert randre(r'(?(1)yes|no)') == 'no'
    assert randre(r'(?(1)yes)') == ''


def test_randre_not_literal():
    validate_pattern('[^a]')
    validate_pattern('[^ ]')


def test_lookahead():
    assert randre('a(?=xxx)b') == 'ab'
    assert randre('a(?!xxx)b') == 'ab'


def test_at():
    assert randre('^a') == 'a'
    assert randre('a$') == 'a'
    assert randre('^a$') == 'a'
