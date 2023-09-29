class Circle:
    # Constructor
    def __init__(self, color: str, radius: float):
        self.color = color
        self.radius = radius

    # Function to calculate the diameter of the circle
    def diameter(self):
        return 2 * self.radius

    # Function to calculate the circumference of the circle
    def circumfrence(self):
        return 2 * self.radius * 3.14

    # Function to check if the circle is red
    def isRed(self):
        return self.color == 'red'


class GraduateStudent:
    # Constructor
    def __init__(self, first_name: str, last_name: str, year: int, major: str):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major

    # Function to calculate the year the student matriculated
    def year_matriculated(self):
        return 2020 - self.year
# Main program


def main():
    # Create an object of type Circle
    c1 = Circle('red', 5)

    # Print the diameter of the circle
    print('The diameter of the circle is:', c1.diameter())
    # Print the circumfrence of the circle
    print('The circumfrence of the circle is:', c1.circumfrence())
    # Print whether the circle is red
    print('Is the circle red?', c1.isRed())

# Create an object of type GraduateStudent
    g1 = GraduateStudent('John', 'Smith', 2018, 'Computer Science')
    # Print the year the student matriculated
    print('The year the student matriculated is:', g1.year_matriculated())


if __name__ == '__main__':
    main()


