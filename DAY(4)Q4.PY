#Simple Class Definition with Method
class Circle:
    """A class representing a circle."""
    PI = 3.14159  # Class variable for Pi

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        # A = pi * r^2
        return self.PI * (self.radius ** 2)

# Test Case
circle1 = Circle(radius=5)
area_c1 = circle1.area()
print(f"5. Circle with radius 5 has an area of: {area_c1:.2f}")