# type()  გვაჩვენებს რა ტიპის არის  ცვლადი
# int()  გარდაქმნის ცვლადს ინტეჯერად
# str()  გარდაქმნის ცვლადს სტრინგად
# float() გარდაქმნის ციფ ფლოუტად
# list.lower()   გამოიყენება რომ დააპატარაო ყველა ასო სთრ-ში
# list.upper()  გამოიყენება რომ გავადიდოდ ყველა ასო სთრ-ში
# list.capitalize() გამოიყენება რომ   პირველი ასო სტრინგში გადიდდეს
# list.reversed()  უკუზღმა აჩვენებს ლისტს
# list.pop()  შლის  ერთ ლისტის ცვლადსს
# list.insert()  ამატებს ლისტში ცვლადს
# list.index()  რომ დავამატოტ ინდეხის ადგილას
# list.split()  გამოიყენება რომ  გახლიჩოს ლისტი
# list.find()  გამოიყენება რომ ვნახოთ რამის ინდექსი

# def plus(a, b):
#     return a + b
# print(plus(10, 20))

# def greet():
#     print("Hello how are you?")
# print(greet())


def info():
    name =  input("Enter your name: ")
    age =  int(input("Enter your age"))
    last_name = input("Enter your last name")
    return f"my Name is {name}, my last name is {last_name}, and my age is {age}"
print(info())