import pytest
from source.day1 import process_calibrations

def test_process_calibrations():
    """
    Test the process_calibrations function.

    Args:
        File Test
    
    Returns:
        True or False depending on the test run
    """
    # Given
    expected_result = 54632

    # When
    result = process_calibrations("source/calibrations.txt")

    # Then
    assert result == expected_result

