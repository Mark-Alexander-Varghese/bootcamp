#task1


total_money = float(input("Enter the total amount of money you have: "))


percent_to_spend = float(input("Enter the percentage of money you want to spend: "))


spending_limit = (percent_to_spend / 100) * total_money


print("Enter the cost of three items you want to buy:")
item1 = float(input("Cost of item 1: "))
item2 = float(input("Cost of item 2: "))
item3 = float(input("Cost of item 3: "))


total_cost = item1 + item2 + item3


if total_cost <= spending_limit:
    print("You can buy these items Your total cost is ",  total_cost)
else:
    print("You cannot buy these items. The amount of money u can spend is ", spending_limit)

#check the status