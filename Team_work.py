class Rectangle:
    """
    This Class Show Properties of a Rectangle
    and calculates the perimeter and area.
    """
    
    
    #calculates the perimeter and area.
    #Codes from Ms.Oghani
    
    def __init__(self , length , width , Height):
        self.length = length
        self.width = width
        self.Height = Height
        

        
        
    def area(self):
        print (self.length * self.width)
        
    
    def perimeter(self):
        print(2*(self.length + self.width))
        
    def Volume(self):
        print(self.width * self.length * self.Height)

        
        #Rectangle information
        #Codes from Ms.Nazari
        
        
    def Symmetry_line(self):
        print("2")
            
            
    def size_of_angle(self):
        print("90")
        
    def sum_of_the_angles(self):
        print("360")
            
            
    def number_of_sides(self):
        print("4")