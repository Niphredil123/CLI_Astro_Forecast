"""Tests for user input validation logic."""
###############################################################################
# IMPORTS
###############################################################################
import pytest
from app.utils.validation_utils import validate_length, validate_lat, validate_lng, \
    validate_yes_no, validate_key

###############################################################################
# TESTS
###############################################################################
# ===== Testing validate_length() =====
@pytest.mark.parametrize('input_value, expected_output',[
    ('1', 1),
    ('2 ', 2),
    (' 3', 3),
    ])
def test_valid_lengths(input_value, expected_output):
    """Test valid forecast lengths including with trailing spaces."""
    assert validate_length(input_value) == expected_output


@pytest.mark.parametrize('input_value',['0','-1','5'])
def test_length_out_of_range(input_value):
    """Test forecast lengths that are out of range."""
    with pytest.raises(ValueError, match='Out of forecast range'):
        validate_length(input_value)


@pytest.mark.parametrize('input_value',['abc', '', ' ', '3.4', '1.5'])
def test_length_not_int(input_value):
    """Test none integer inputs for the forecast length."""
    with pytest.raises(ValueError, match='Not Int'):
        validate_length(input_value)


###############################################################################
# ===== Testing validate_lat() =====
@pytest.mark.parametrize('input_value, expected_output',[
    ('90.0', 90.0),
    ('-90 ', -90.0),
    (' 56.654', 56.654),
    ])
def test_valid_lats(input_value, expected_output):
    """Test valid latitude values including with trailing spaces."""
    assert validate_lat(input_value) == expected_output


@pytest.mark.parametrize('input_value',['-98.77', '90.1'])
def test_invalid_lats(input_value):
    """Test invalid latitude values."""
    with pytest.raises(ValueError, match='Invalid latitude'):
        validate_lat(input_value)


@pytest.mark.parametrize('input_value',['abc', '', ' '])
def test_lat_not_float(input_value):
    """Test non-numeric inputted latitude values."""
    with pytest.raises(ValueError, match='Not float'):
        validate_lat(input_value)


###############################################################################
# ===== Testing validate_lng() =====
@pytest.mark.parametrize('input_value, expected_output',[
    ('180.0', 180.0),
    ('-180 ', -180.0),
    (' 2.54', 2.54),
    ])
def test_valid_lngs(input_value, expected_output):
    """Test valid longitude values including with trailing spaces."""
    assert validate_lng(input_value) == expected_output


@pytest.mark.parametrize('input_value',['-195', '180.1'])
def test_invalid_lngs(input_value):
    """Test invalid longitude values."""
    with pytest.raises(ValueError, match='Invalid longitude'):
        validate_lng(input_value)


@pytest.mark.parametrize('input_value',['abc', '', ' '])
def test_lng_not_float(input_value):
    """Test non-numeric inputted longitude values."""
    with pytest.raises(ValueError, match='Not float'):
        validate_lng(input_value)


###############################################################################
# ===== Testing validate_yes_no() =====
@pytest.mark.parametrize('input_value',['Yes', 'yes', 'Y', 'y'])
def test_valid_yes(input_value):
    """Test that valid yes entries return True."""
    assert validate_yes_no(input_value) is True


@pytest.mark.parametrize('input_value',['No', 'no', 'N', 'n'])
def test_valid_no(input_value):
    """Test that valid no entries return False."""
    assert validate_yes_no(input_value) is False


@pytest.mark.parametrize('input_value',['abc', '', ' ', 'yeah'])
def test_invalid_yes_no(input_value):
    """Test that invalid inputs raise a ValueError"""
    with pytest.raises(ValueError, match='Invalid input'):
        validate_yes_no(input_value)

###############################################################################
# ===== Testing validate_key() =====
@pytest.mark.parametrize('input_value, expected_output',[
    ('xxx', 'xxx'),
    ('XXX', 'xxx'),
    ('Xxx', 'xxx'),
    ('xxX ', 'xxx'),
    (' XXx', 'xxx'),
    ('1NNNN2NNNN3NNNN4NNNN5NNNN', '1NNNN2NNNN3NNNN4NNNN5NNNN'),
    ('1ABDJ2hajf3andf4AFBS5LNSK ', '1ABDJ2hajf3andf4AFBS5LNSK'),
    (' SFAF1KNFA2OBFI3NION4LSFK5', 'SFAF1KNFA2OBFI3NION4LSFK5'),
    ])
def test_valid_api_key(input_value, expected_output):
    """Tests that valid API keys or 'xxx' are correctly returned."""
    assert validate_key(input_value) == expected_output


@pytest.mark.parametrize('input_value',[
    'abc',
    '',
    ' ',
    '1aaaa2aaaa3aaaa',
    ])
def test_invalid_api_key(input_value):
    """Test that invalid inputs raise a ValueError"""
    with pytest.raises(ValueError, match='Invalid input'):
        validate_key(input_value)
