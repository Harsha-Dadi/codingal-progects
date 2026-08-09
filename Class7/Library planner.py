print("-----Library planner-----")
print("answer 3 questions and ill plan your library visit")

day= input("what day is it(Monday to Sunday)?:").strip().capitalize()
weather=input("what weather is it?(sunny/rainy/cloudy):").strip().lower()
book_due=input("do you have a book due? (yes/no)").strip().lower()

print()
print(f"Your library plan for {day}")
print("-" * 35)

if day is ("Saturday" , "Sunday"):
    print("weekend: the day is a nice day to go to the library")
elif day == "Monday":
    print("Monday- start of the week check your reading list")
elif day == "Friday":
    print("Last school day before weekends rememeber to return your books ")
elif day == ("Tuesday","Wednesday","Thursday"):
    print("Your day is in a regular school day plan a short visit")
else: 
    print("not recognised day please try again")

print()
print("-----Weather and book due-----")
if weather == "sunny" and book_due == "yes":
    print("library tip- great weather! return your book and borrow a new one")

if weather == "rainy" and weather == "cloudy":
    print("library tip- bad weather! Carry an umbrella if you are going to the library")

if not(book_due == "yes"):
    print("Library tip- no books need to return today but you can browse for books")

if weather == "rainy" and book_due == "yes":
    print("library tip- be careful and grab an umbrella while returning book")

elif weather == "sunny" and book_due == "yes" and not (day in("Saturday, Sunday")):
    print("library tip- Stop at the library after school and return the book")

elif day in ("Saturday, Sunday") and weather == "sunny":
    print("library tip- perfect day to read longer at the library")
else:
    print(" library tip- try reshedule the plan again")