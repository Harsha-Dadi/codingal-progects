total_homework=4
orginal_count=total_homework
print(f"you have {orginal_count}homework to finish today")

completed_count=0
task_num=1
while task_num <= total_homework:

    if task_num == 1:
        current_task="Math Worksheet"
    elif task_num == 2:
            current_task="Science Reading"
    elif task_num == 3:
            current_task="English Writing"
    else:
            current_task="Coding Practice"
    ans=input(f"Have you finished:{current_task} (yes/no)")

    if ans == "yes":
          completed_count+=1
          task_num+=1
          print("Good job!")
    else:
          print("Ok,Hurry up")

    print("Homeworks remaining:",total_homework-completed_count)
    print()

print("ALL HOMEWORK COMPLETED")
print("great work finishing homework")

print("lets safely peek at an inf loop")

test_value=0
safety_count=0
while test_value >= 0:
    print("This condition never changes so it will run forever")
    safety_count +=1


    if safety_count == 3:
        print("stopping here on purpose- an real inf loop will not stop")
        break

print("Homework completion summary")
print("Homework assigned:",orginal_count)
print("Homework Completed",completed_count)
print("Homerwork remaining",total_homework-completed_count)