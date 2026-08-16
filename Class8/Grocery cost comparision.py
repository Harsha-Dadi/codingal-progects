rice_price=12
milk_price=4
fruit_price=8
number_of_baskets=2
family_members=4

basket_costs_per_person=((rice_price+milk_price+fruit_price)*number_of_baskets/family_members)

print("Grocery basket for 1 person is ",basket_costs_per_person)

total_items=int(input("Enter your total amount of grocery: "))
total_people=int(input("Enter the total amount of family memebers: "))

if total_items%total_people== 0:
    print(f"{total_items} items can be divided equally amoung {total_people} people")
else:
    print(f"{total_items} items can not be divided equally amoung {total_people} people")

recorded_average=65
incorrect_week_cost=50
correct_week_cost=80
total_weeks=4

recorded_total=recorded_average*total_weeks
print("Recorded total is ",recorded_total)

Corrected_total=(recorded_total-incorrect_week_cost+correct_week_cost)
print("Corrected grocery total is ",Corrected_total)
Corrected_average=Corrected_total/total_weeks
print("Corrected weekly average is ",Corrected_average)

store_a_avrg=70
store_b_avrg=75
store_c_avrg=80

print("store a average is ",store_a_avrg)
print("store b average is ",store_b_avrg)
print("store c average is ",store_c_avrg)

if store_a_avrg > Corrected_average and store_b_avrg > Corrected_average and store_c_avrg > Corrected_average:
    print("Your corrected grocery averages is lower than all 3 store averages")

elif store_a_avrg < Corrected_average and store_b_avrg < Corrected_average and store_c_avrg < Corrected_average:
    print("Your corrected grocery averages is higher than all 3 store averages")

else:
    print("Your corrected grocery average is between all 3 store averages")

