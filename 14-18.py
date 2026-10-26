
# def agents(**agentsteam):
#     print (agents)

# agents(data_analist= "analyze data", data_scientist="create models")

# print(agents)


# # letter = (lambda name:name[-1])
# print(list(map(lambda let: let[-1],['jon','rivka','dana'])))





# class Libarybook:
#     def __init__(self,title,author,year,is_checked_out=False):
#         self.title=title
#         self.author=author
#         self.year=year
#         self.is_checked_out=is_checked_out

#     def describe_book(self):
#         """describe the book auther and year"""
#         return f"{self.title} is {self.author} {self.year}{self.is_checked_out}"
#     def check_out(self):
#         if not self.is_checked_out:
#             self.is_checked_out = True
#             print(f"'{self.title}' was checked out")
#         else:
#             print(f"'{self.title}' is already checked out")
    


class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def describe(self):
        return (f"{self.name} , {self.age}")

class Dog(Animal):
    def bark(self):
        print("woof")

dog1 = Dog("raxy",6)
dog1.bark()