import turtle

def identify_shape(num_sides):
    if num_sides < 3:
        return "Invalid input: Polygon must have at least 3 sides"
    elif num_sides == 3:
        return "Triangle"
    elif num_sides == 4:
        return "Square"
    elif num_sides == 5:
        return "Pentagon"
    elif num_sides == 6:
        return "Hexagon"
    elif num_sides == 7:
        return "Heptagon"
    else:
        return "Polygon with {} sides".format(num_sides)
    
def visualize_shape(num_sides):
    if num_sides < 3:
        print("Invalid input: Polygon must have at least 3 sides")
    else:
        window = turtle.Screen()
        t = turtle.Turtle()
        angle = 360 / num_sides
        for _ in range(num_sides):
            t.forward(100)  # Adjust the length as needed
            t.right(angle)
        window.exitonclick()

if __name__ == "__main__":
    num_sides = int(input("Enter the number of sides: "))
    
    # Identify the shape
    shape = identify_shape(num_sides)
    print(f"The shape with {num_sides} sides is a {shape}")
    
    # Visualize the shape (optional)
    visualize = input("Visualize the shape? (y/n): ")
    if visualize.lower() == "y":
        visualize_shape(num_sides)