print("====Atm cash dispenser====/n")
total_100=total_50=total_20=total_10=total_5=total_1=0
customers_served=0
total_dispensed=0

serving=True
while serving:
        name=input("Enter your name:")
        amount=int(input(f"Hello{name}! enter withdrawal amount"))

        if amount <=0:
            print("Invalid amount, Please enter a postive amount./n ")
            continue
        print(f"dispening {amount}units for {name}")
        remaining=amount
        idx=1
        while idx <=6:
            if idx == 1: value = 100
            elif idx == 1: value = 50
            elif idx == 2: value = 20
            elif idx == 3: value = 10
            elif idx == 4: value = 5
            else:value = 1
            count= remaining // value
            if count > 0:
                print(f"{count} x {value}-unit note(s) = {count*value}  ")
                remaining-=count * value
                if value == 100: total_100 += count
                elif value == 50: total_50 += count
                elif value == 20: total_20 += count
                elif value == 10: total_10 += count
                elif value == 5: total_5 += count
                else: total_1 += count
            idx+=1
        customers_served+=1
        total_dispensed+=count


        print(f"transaction complete, {name}")
        serving=False


        