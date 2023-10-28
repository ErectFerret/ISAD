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
        pass

def test_get_user_input():
    assert get_user_input(4, 'y') == (4, 'y')   # Partition 6
    assert get_user_input(2, 'n') == (2, 'n')   # Partition 7
    assert get_user_input(6, 'x') == (6, 'x')   # Partition 8
    assert get_user_input(1, 'z') == (1, 'z')   # Partition 9

def main():
    test_identify_shape()
    test_get_user_input()
    print("All tests passed!")
main()