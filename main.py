# imports
import math

# custom classes
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_diameter(self):
        return self.radius * 2

    def calculate_circumference(self):
        return self.radius * 2 * math.pi

    def calculate_area(self):
        return self.radius ** 2 * math.pi

    def grow(self):
        return self.calculate_diameter()

    def get_radius(self):
        return self.radius


# main script start
# prompt user for radius, repeat if not valid
valid_radius = False
user_radius = 0
while not valid_radius:
    user_radius = input(f"Please specify a radius: ")
    try:
        user_radius = float(user_radius)
        valid_radius = True
    except ValueError:
        print("That's not a valid radius.  Numbers only (2 decimals permitted).")

# Calculate circle & report results, then ask to grow or exit
repeat = True
while repeat:
    user_circle = Circle(user_radius)
    print(f"Your circle has diameter {user_circle.calculate_diameter()}, "
          f"Circumference {user_circle.calculate_circumference()}, "
          f"and Area {user_circle.calculate_area()}")

    do_grow = input(f"Would you like your circle to grow? (y/n) ")
    if do_grow == 'y':
        print("Stand by while your circle grows...")
        user_radius = user_circle.grow()
    else:
        repeat = False
        print(f"Goodbye.  Your final circle radius was {user_circle.get_radius()}")
