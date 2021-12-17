class Rectangle:

    def __init__(self, length, width, height):
        try:
            self.length = int(length)
            self.width = int(width)
            self.height = int(height)
        except:
            raise ValueError()

        if length < 0 or width < 0 or height < 0:
            raise ValueError()


    def calculate_volume(self):
        return self.length*self.width*self.height

