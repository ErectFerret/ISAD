import turtle
from main import identify_shape, visualize_shape

def test_identify_shape_valid_shapes():
    # Test Case 1
    valid_sides = [3, 4, 5, 6, 7]
    for sides in valid_sides:
        assert identify_shape(sides) in ["Triangle", "Square", "Pentagon", "Hexagon", "Heptagon"]

def test_identify_shape_invalid_input():
    # Test Case 2
    invalid_sides = [-1, 0, 2, 8, 10]
    for sides in invalid_sides:
        try:
            identify_shape(sides)
            assert False, f"No exception raised for invalid side: {sides}"
        except ValueError:
            pass  # Expecting a ValueError

def test_visualize_shape_valid():
    # Test Case 3
    valid_visualization = [4, 5, 6]
    for sides in valid_visualization:
        assert visualize_shape(sides) is None

def test_visualize_shape_invalid():
    # Test Case 4
    try:
        visualize_shape(2)
        assert False, "No exception raised for invalid visualization"
    except ValueError:
        pass  # Expecting a ValueError
