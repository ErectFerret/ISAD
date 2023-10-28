import turtle
from main import identify_shape
from main import get_user_input

def test_identify_shape():
    # Test valid shapes
    assert identify_shape(5) == "Pentagon"  # Partition 1
    assert identify_shape(3) == "Triangle"  # Partition 2
    assert identify_shape(7) == "Heptagon"  # Partition 3

    # Test invalid shapes
    try:
        identify_shape(4)  # Partition 4
        assert False, "No exception raised for invalid shape"
    except ValueError:
        pass  # Expecting a ValueError
    try:
        identify_shape(8)  # Partition 5
        assert False, "No exception raised for invalid shape"
    except ValueError:
        pass  # Expecting a ValueError

