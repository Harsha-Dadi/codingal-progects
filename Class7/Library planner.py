print("-----Library planner-----")
print("answer 3 questions and ill plan your library visit")

day= input("what day is it(Monday to Sunday)?:").strip().capitalize()
weather=input("what weather is it?(sunny/rainy/cloudy):").strip().lower()
book_due=input("do you have a book due? (yes/no)").strip().lower()

print()
print(f"Your library plan for {day}")
