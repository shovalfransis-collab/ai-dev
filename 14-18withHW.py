
# def agents(**agentsteam):
#     print (agents)

# agents(data_analist= "analyze data", data_scientist="create models")

# print(agents)


# # letter = (lambda name:name[-1])
# print(list(map(lambda let: let[-1],['jon','rivka','dana'])))



# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def describe(self):
#         return (f"{self.name} , {self.age}")

# class Dog(Animal):
#     def bark(self):
#         print("woof")

# dog1 = Dog("raxy",6)
# dog1.bark()



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
    


# class BankAccount:
#     def __init__(self,name,balance=0):
#         self.name = name
#         self.balance=balance
    
#     def deposit(self,amount):
#         self.balance+=amount
#         return self.balance
    
#     def withdraw(self,amount):
#         if self.balance-amount <0 :
#             print(self.balance,"not enough balance")
#         else:
#             self.balance=self.balance-amount

#         return self.balance
    
#     def display(self):
#         print(self.balance , self.name)
 

# acc = BankAccount("דנה", 100)
# acc.display()
# acc.withdraw(30)
# print(acc.balance)    # 70
# acc.withdraw(500)     # מודפס: not enough balance
# print(acc.balance)    # עדיין 70




def uppercase_decorator(func):
    def case():
        big=func()
        return big.upper()
    return case

@uppercase_decorator
def greet():
    return "hello world"

print(greet())





# def stars_decorator(func):          # 1. מקבל פונקציה
#     def wrapper():                  # 2. העטיפה
#         result = func()             # 3. מפעיל את המקורית ושומר תוצאה
#         return "***" + result + "***"   # 4. מוסיף כוכביות
#     return wrapper                  # 5. מחזיר את העטיפה (בלי סוגריים)

# def say_hi():
#     return "hi"

# say_hi = stars_decorator(say_hi)
# print(say_hi())                     # ***hi***




# def stars_decorator(func):
#     def wrapper():
#         result = func()           # מפעיל את המתנה המקורית
#         return "***" + result + "***"
#         print("wrapper is running")
#     return wrapper

# def say_hi():
#     return "hi"

# say_hi = stars_decorator(say_hi)
# print(say_hi())                   # ***hi***

