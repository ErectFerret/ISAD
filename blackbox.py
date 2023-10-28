import turtle
from main import identify_shape

def test_identify_shape():
    # Test valid shapes
    assert identify_shape(5) == "Pentagon"  # Partition 1
    assert identify_shape(3) == "Triangle"  # Partition 2
    assert identify_shape(7) == "Heptagon"  # Partition 3

    # Test invalid shapes
    try:
        identify_shape(4)  # Partition 2: Invalid number of sides (< 3)
