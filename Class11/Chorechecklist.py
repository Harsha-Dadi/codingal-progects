total_chores=4
completed_chores=0
chores_num=1
print("The total chores today is",total_chores)
while total_chores >= chores_num:
    if chores_num == 1:current_chore="Make your bed"
    elif chores_num == 2:current_chore="Wash dishes"
    elif chores_num == 3:current_chore="Feed the pet"
    elif chores_num == 4:current_chore="Clean the house"

    ans=input(f"Have you completed {current_chore} (yes/no)")
    if ans == "yes":
        print("Good job")
        completed_chores+=1
        chores_num+=1
    else:
        print("ok, but hurry up")

    print("num of chore remaining:",total_chores-completed_chores)
print("All Chores Completed")
print("now we are going to safely break our inf loop")

safety_counter=0
test_value=0
while test_value >= 0:
    print("Hello world")
    safety_counter+=1
    if safety_counter == 3:
        print("safely breaking an inf loop will not stop")
        break

print("Total chores:",total_chores)
print("Remaining chores:",total_chores-completed_chores)
print("Completed chores :",completed_chores)