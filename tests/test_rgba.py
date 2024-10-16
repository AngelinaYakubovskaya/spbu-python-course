import pytest
from project.rgba import rgba_vector


@pytest.mark.parametrize(
    "index, expected_rgba",
    [
        (0, (0, 0, 0, 0)),  # First RGBA value
        (1, (0, 0, 0, 2)),  # Second RGBA value
        (2, (0, 0, 0, 4)),  # Third RGBA value
        (1000000, (15, 151, 151, 100)),  # Large index, random valid value
        (16581375, (255, 255, 255, 100)),  # Last valid RGBA value in range
    ],
)
def test_rgba_vector(index, expected_rgba):
    """Test RGBA vector generator for various indices."""
    assert rgba_vector(index) == expected_rgba


def test_rgba_out_of_range():
    """Test RGBA generator for out of range index."""
    assert rgba_vector(16581376) == (None,)  # Index out of bounds returns None
