# # # Homework numbers
# # #שאלה 3 : קבל שני מספרים מהמשתמש והצג את ההפרש ביניהם ואת המכפלה שלהם.
# # num1 = input('enter the first number')
# # num2 = input('enter the second number')
# # subtraction= int(num1) - int(num2)
# # multiplication = int(num1) * int(num2)
# # print(f"the subtraction sum is: {subtraction}\nthe multiplication sum is: {multiplication}")

# # # שאלה 1 : קבל שם פרטי מהמשתמש והצג אותו באותיות גדולות.
# # name = input ('enter your first name')
# # print (name.capitalize())

# # # שאלה 2 : קבל משפט מהמשתמש והצג כמה תווים יש בו.
# # sentence = input('enter your sentence:')
# # print (len(sentence))

# # # שאלה 3 : קבל מהמחשב מילה והדפס את האות הראשונה והאחרונה.
# # word = input('enter a single word:')
# # print (word[0],word[-1])


# # שאלה 4 (מתודות) : קבל מחרוזת מהמשתמש והצג: האם כל התווים הם אותיות?
# # • האם המחרוזת מתחילה באות גדולה?
# # • את הגרסה של המחרוזת באותיות קטנות בלבד.
# # sentence = input('enter your string here:')
# # print(sentence.isalpha(),"\n",sentence.istitle(),"\n",sentence.lower())

# # # # שאלה 1 : קבל שלושה שמות של פירות ושמור ברשימה. הדפס את הרשימה.
# # my_list = [input('enter first'),input('enter second'),input('enter third')]
# # print(my_list)
# # # # ==================================================
# # fruit1 = input('enter first fruit')
# # fruit2 = input('enter second fruit')
# # fruit3 = input('enter third fruit')
# # secondlist = [fruit1,fruit2,fruit3]
# # print(secondlist)


# # שאלה 2 : צור רשימה של מספרים ] ,2 ,4 ,6 8[, הוסף את המספר 10 לרשימה והצג אותה.

# # my_list=[2,4,6,8]
# # my_list.append(10)
# # print(my_list)

# # # שאלה 3 : צור רשימה עם שלושה צבעים ובצע החלפה של הצבע השני לצבע אחר לבחירתך.
# # color = ['red','green','blue']
# # color[1] = 'brown'
# # print(color)

# # # שאלה 4 (מתודות) : צור רשימת מספרים ]7 1, 9, 2, 5,[ = numbers ובצע את הפעולות הבאות:
# # numbers = [5,2,9,7,1]
# # print(max(numbers),min(numbers))# הדפס את המספר הגדול ביותר והקטן ביותר.

# # print(len(numbers))  #הדפס את מספר האיברים ברשימה.

# # numbers.reverse()# הפוך את הסדר של השימה והדפס שוב.
# # print(numbers)# 

# # numbers.sort()# מיין את הרשימה בסדר עולה והדפס אותה.
# # print(numbers)
# # =====================================
# # שאלה 1 : צור טפל של מיקום גיאוגרפי (קו רוחב, קו אורך) והדפס אותו.
# #location = (32.08, 34.78)
# # #print(location)

# # שאלה 2 : קבל שלושה רכיבים של תאריך (יום , חודש, שנה ) ושמור אותם בטפל. הדפס את השנה.
# date = (input('day'),input('month'),input('year'))
# # # print (date[-1])

# # שאלה 3 : צור טפל עם שלושה מספרים ובצע חיבור בין המספר הראשון לאחרון.
# num = (20,15,35)
# num= num[0]+num[-1]
# print(num)

# שאלה 4 : צור טפל של מספרים (6 5, 4, 3, 2, 1, 0,) = numbers ובצע את הפעולות הבאות:

# print(numbers[1:4])# • הדפס את המספרים מאינדקס 1 עד 3 (כולל).
#print(numbers[0:3])# • הדפס את שלושת המספרים הראשונים 
# # print(numbers[::2])# • הדפס כל מספר שני.
# numbers = (0,1,2,3,4,5,6)
# print(numbers[4:])# • הדפס את המספרים החל מהמקום הרביעי ועד הסוף.

#שאלה :5 צור טפל בשם person שיכיל את הערכים : שם, גיל , עיר . לאחר מכן, הכנס אותם לשלוש
# משתנים city ,age ,name והדפס כל אחד מהם בנפרד.

# person = ('shoval','23','tel_aviv')
# name = person[0]
# age = person[1]
# city = person [-1]
# print(name, "\n", age, "\n", city)

# # # =====================================
# שאלה 1 :צור מילון של פרטי ספר: כותרת, מחבר, שנה. הדפס את שם המחבר.
#book = {'name':'sonic','author':'fransis','year':'2003'}
#print (book['author'])

# שאלה 2 :קבל שם משתמש וכתובת אימייל, שמור במילון והצג את כל המפתחות.
# email = input('enter your email here')
# username = input('enter your username here')
# info = {email:username}
# print(info)

# שאלה 3 :צור מילון של מוצר ( שם, מחיר ), עדכן את המחיר והדפס את הערכים.

# book = {'name':'price'}
# book['name'] = 'ball'
# book['price'] = '50'
# print(book.values())
#  =====================================
# # שאלה 1 : קבל שלוש מילים מהמשתמש ושמור אותן בקבוצה. הדפס את גודל הקבוצה.
# word1 = input('enter the first word')
# word2 = input('enter the second word')
# word3 = input('enter the third word')
# words_set = {word1, word2, word3}
# print(len(words_set))

# # שאלה 2 : צור רשימה עם הערכים 1,2,3,3,3 ואז הפוך אותה לקבוצה.
# numbers = [1,2,3,3,3]
# my_set = set[int](numbers)
# print(numbers,'\n',my_set)
