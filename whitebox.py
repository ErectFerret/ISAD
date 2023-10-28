import turtle
from main import identify_shape, visualize_shape

def test_identify_shape_valid_shapes():
    # Test Case 1
    valid_sides = [3, 4, 5, 6, 7]
    for sides in valid_sides:
        assert identify_shape(sides) in ["Triangle", "Square", "Pentagon", "Hexagon", "Heptagon"]

