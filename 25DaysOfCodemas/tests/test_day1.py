import pytest
from source.day1 import process_calibrations

def test_process_calibrations():
    """Test for the process_calibrations function."""
    # Arrange
    expected_result = 54632
    # Act
    result = process_calibrations("source/calibrations.txt")
    # Assert
    assert result == expected_result