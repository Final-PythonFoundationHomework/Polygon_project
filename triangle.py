from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        return self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        if self.is_valid():
            if self.a == self.b == self.c:
                return 'Equilateral' 
            elif self.a == self.b or self.b == self.c or self.c == self.a:
                return 'Isosceles'  
            else:
                return 'Scalene'  
        else:
            return 'Invalid'
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        if self.is_valid():
            return self.a + self.b + self.c
        else:
            return 0


    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        if self.is_valid():
            s = (self.a + self.b + self.c) / 2
            return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        else:
            return 0
