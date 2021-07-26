class Prism:
    def __init__(self,width,height,depth):
        self.__width = width
        self.__height = height
        self.__depth = depth
    
    def content(self):
        return (self.__width * self.__height * self.__depth)

p1 = Prism(10,20,30)
print(p1.content())