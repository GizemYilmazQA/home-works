# ExersizeTwo
"""
# exersize 1
class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3

    number_of_sides=3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
             return True
        else:
             return False

my_triangle=Triangle(90,30,60)
print(my_triangle.check_angles())
print(my_triangle.number_of_sides)
"""


"""
# exersize 2

class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

    happy_bday = Song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])

# print(happy_bday.sing_me_a_song())
"""



# Exersice 3

"""
class Lunch(object):
    def __init__(self, menu):
        self.menu=menu

    def menu_price(self):
        if self.menu== "menu 1":
            print("Your choice:", self.menu,"Price 12.00")
        elif self.menu == "menu 2":
            print("Your choice:", self.menu, "Price 13.40")
        else:
            print("Error in Menu")

ben_ne_ödiycem= Lunch("menu 1")
ben_ne_ödiycem.menu_price()
"""

"""
# Exersize 4

class Inside (object):
    def __init__(self):
        pass

class Point3D (Inside):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
my_point = Point3D(1,2,3)
# print(my_point)
"""






