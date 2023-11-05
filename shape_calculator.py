class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height
    
    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self) -> str:
        nlines = self.height
        line_width = self.width
        if (nlines > 50 or line_width > 50):
            return "Too big for picture."
        else:
            return ("*" * line_width + "\n") * nlines 
        
    def get_amount_inside(self, shape):
        amount_inside = int(self.get_area() / shape.get_area())
        return amount_inside
    
    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
         

class Square(Rectangle):
    def __init__(self, length: int) -> None:
        self.width = length
        self.height = length

    def set_side(self, length):
        self.width = length
        self.height = length
        
    def __repr__(self) -> str:
        return f"Square(side={self.width})"