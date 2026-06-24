import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("    Hello!", "Hello!"),
    ("    python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("no_space", "no_space"),
    ("", ""),
    (" space and space ", "space and space "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Hello", "H", True),
    ("4you", "4", True),
    ("Skypro", "o", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Code", "c", False),
    ("4you", "for", False),
    (" ", "!", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, del_symbol, expected", [
    ("Hello world", "world", "Hello "),
    ("Masha", "a", "Msh"),
    ("Skypro", "S", "kypro"),
])
def test_delete_symbol_positive(input_str, del_symbol, expected):
    assert string_utils.delete_symbol(input_str, del_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, del_symbol, expected", [
    ("Code", "z", "Code"),
    ("", "a", ""),
    ("String", "", "String"),
])
def test_delete_symbol_negative(input_str, del_symbol, expected):
    assert string_utils.delete_symbol(input_str, del_symbol) == expected
