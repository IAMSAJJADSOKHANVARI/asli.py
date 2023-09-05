# text = input("Enter your text: ")
# a = len(text)
# print(f"Title length is {a}")
####################################
# from math import hypot
#
#
# class Point:
#     # method
#     # attribute ->default/ non default
#     def __init__(self, x: float = 0, y: float = 0):
#         self.x = x
#         self.y = y
#
#     def move(self, x: float, y: float) -> None:
#         self.x = x
#         self.y = y
#
#     def rest(self):
#         self.move(0, 0)
#
#     def distance(self, other: "Point") -> float:
#         return hypot(self.x - other.x, self.y - other.y)


# p1 = Point()
# p2 = Point()
#
# p1.rest()
# print(p1.x, p1.y)
#
# p2.move(3, 4)
# print(p2.x, p2.y)
# distance
# print(p1.distance(p2))
# ________________
# __new__  ->create
# __init__ ->  initialize
# p3 = Point(10, 12)
# print(p3.x)
# print(p3.y)
#
# print(p2.x)
# print(p2.y)
#
# print(p1.x)
# print(p1.y)
###############
# meals = ['pasta', 'pizza', 'salad']
# for meal in meals:
#     print(meal.capitalize())
# print("Bye! ")
#############
# def main():
#     while True:
#         h=int(input("enter num:"))
#         if h > 8 or h<1 :
#             continue
#         else:
#             break
#     draw(h)

# def draw(h):
#     for i in range (h):
#         print((h-(i+1))* " "+ (i+1)*"#"+" "+(i+1)*"#")
# main()
#########333
# b=[]
# i=1
# print("if you want to exit to programm enter a char!")
# while True:
#     try:

#         b.append(float(input(f"enter{i} number:")))
#         i +=1 
#         continue
#     except:
#         break
# print(f"avarge:{sum(b)/len(b)}")
####3
import csv 
with open ("favorites.csv","r")as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        fa=row[1]
        print(fa)