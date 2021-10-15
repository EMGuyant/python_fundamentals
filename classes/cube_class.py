""" A program that defines and uses a cube class. """

# define the cube class with module documentation
class Cube:
    """Creates a cube with a specificed side length and provides various calculations
        of cube features including the volumn, surface area, face diagonal, and space diagonal"""
    def __init__ (self, sideLength):
        """Initialize cube with specified side length"""
        self.sideLength = sideLength

    def getLength(self):
        """Returns the length of the cubes sides"""
        return self.sideLength
    
    def volume (self):
        """Caluculates and returns the volumne of the cube"""
        volume = self.sideLength**3
        return volume

    def surfaceArea(self):
        """Calculates and returns the surface area of the cube"""
        surfaceArea = self.sideLength**2 * 6
        return surfaceArea
    
    def faceDiagonal(self):
        """Calculates and returns the face diagonal of the cube"""
        faceDiagonal = (2**(1/2)) * self.sideLength
        return faceDiagonal

    def spaceDiagonal(self):
        """Calculates and returns the space diagonal of the cube"""
        spaceDiagonal = (3**(1/2)) * self.sideLength
        return spaceDiagonal

        
def writeCube(c) :
    """ A function that takes a cube as a parameter and
        prints its information."""
    print("Edge Length =",c.getLength())
    print("Volume =",c.volume())
    print("Surface Area =",c.surfaceArea())
    print("Face Diagonal =",c.faceDiagonal())
    print("Space Diagonal =",c.spaceDiagonal())
    

def main() :
    """ A function that tests the cube class. """
    c1 = Cube(5.3) # cube with edge length of 5.3
    c2 = Cube(3.1) # cube with edge length of 3.1

    print("Cube 1:")
    writeCube(c1)
    print()
    print("Cube 2:")
    writeCube(c2)


main()    
    
