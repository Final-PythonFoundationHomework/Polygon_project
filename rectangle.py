class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b
        my_object = YourClassName(3.0, 4.5)

    def is_valid(self) -> bool:
        """
        This method checks if the rectangle is valid
        
        Args:
            No
        Returns: 
            bool: True if the rectangle is valid, False otherwise
        """ 
        if self.length > 0 and self.width > 0:
            return True
        else:
            return False

    def perimeter(self) -> float:
        """
        This method finds the perimeter of the rectangle.
        Args:
            No
        Returns:
            float or int: return perimeter of the rectangle if the rectangle is valid, 0 otherwise
        """
        if self.is_valid():
            return 2 * (self.length + self.width)
        else:
            return 0

    def area(self) -> float:
        """
        This method finds the area of the rectangle.
        Args:
            No
        Returns:
            float or int:  return area of the rectangle if the rectangle is valid, 0 otherwise 
        """
        if self.is_valid():  
            return self.length * self.width
        else:
            return 0
