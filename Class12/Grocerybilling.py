print("GROCERY BILLING QUEUE")

low_priced_items=medium_priced_items=high_priced_items=0

customers_served=0
total_sales=0

billing= True
while billing:
        name=input("Enter your name:")
        item_count=int(input(f"Hello {name}! How many items are you buying?:"))

        if item_count <=0:
            print("Invalid amount, Please enter a postive amount./n ")
            continue
            
            
        print(f"Billing item for {name}")
        customer_total=0
        item_number=1
        while item_number <= item_count:
            item_name=(input("Enter the name of item: "))
            price=int(input(f"Enter price of {item_name}: "))
            quantity=int(input(f"Enter quantity of {item_name}: "))
            if price <= 0 or quantity <=0:
                 print("Invalid input,Please try again")
                 continue
            item_total=price*quantity
            print(f"{item_name}:{price} x {quantity}={item_total}")
            item_total=customer_total

            if price < 50:
                low_priced_items+= quantity
            elif price <= 100:
                 medium_priced_items += quantity
            else:
                 high_priced_items += quantity


        print(f"transaction complete, {name}")
        serving=False