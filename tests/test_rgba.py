import pytest
from project.rgba import generate_rgba, fetch_rgba_element


@pytest.mark.parametrize(
    "expected_rgba, index",
    [
        ((0, 0, 0, 0), 1),  # First RGBA value
        ((0, 0, 0, 2), 2),  # Second RGBA value
        ((0, 0, 0, 4), 3),  # Third RGBA value
        ((0, 0, 0, 6), 4),  # Fourth RGBA value
        ((0, 0, 1, 0), 52),  # The 52nd element
    ],
)
def test_generate_rgba(expected_rgba, index):
    """
    Tests the RGBA generator by iterating to the given index and comparing
    the generated RGBA value to the expected one.
    """
    gen = generate_rgba()  # Get the generator instance
    for _ in range(index - 1):  # Skip to the desired index
        next(gen)
    assert next(gen) == expected_rgba  # Compare the expected and actual RGBA values


@pytest.mark.parametrize(
    "i, expected",
    [
        (1, (0, 0, 0, 0)),  # First element
        (10, (0, 0, 0, 18)),  # Tenth element
        (52, (0, 0, 1, 0)),  # 52nd element, start of next blue value
        (51 * 256 + 1, (0, 1, 0, 0)),  # Change in green channel
        (51 * 256 * 256 + 1, (1, 0, 0, 0)),  # Change in red channel
    ],
)
def test_fetch_rgba_element(i, expected):
    """
    Tests the fetch_rgba_element function to ensure it retrieves the correct RGBA
    value for a given index.
    """
    assert fetch_rgba_element(i) == expected


@pytest.mark.parametrize(
    "i, expected_error",
    [
        (-1, "Error: index must be greater than 0. Element numbering starts from 1."),
        (0, "Error: index must be greater than 0. Element numbering starts from 1."),
        (
            256**3 * 51 + 1,
            "Error: index exceeds the total number of possible vectors.",
        ),
        ("invalid", "Error: index must be an integer."),
    ],
)
def test_fetch_rgba_element_errors(i, expected_error):
    """
    Tests the fetch_rgba_element function to ensure proper error handling
    for invalid and out-of-range indices.
    """
    assert fetch_rgba_element(i) == expected_error
