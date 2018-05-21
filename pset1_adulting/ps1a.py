#Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats. 

# Your program should ask the user to enter the following variables: 
# 1. The starting annual salary (annual_salary) 
# 2. The portion of salary to be saved (portion_saved) 
# 3. The cost of your dream home (total_cost)

# annual_salary = input("What is your starting annual salary? ")
# portion_saved = input("How much of your monthly income will you save each month? (use dec) ")
# total_cost = input("What is the cost of your dream home? ")

annual_salary = 50000
portion_saved = .1
total_cost = 250000

print("annual salary",annual_salary, "portion saved", portion_saved, "total cost", total_cost)
portion_down_payment = 0.25
current_savings = 0
r = 0.04
#savings put into  is current_savings*r/12

portion_down_payment = 0.25
current_savings = 0
r = 0.04
goal = portion_down_payment * float(total_cost)
amt_to_savings = float(portion_saved) * float(annual_salary)/12
print("goal",goal)
print("savings", amt_to_savings)

def calc_savings(cs):
  cs = cs + amt_to_savings + current_savings*r/12
  return cs
def amount_to_go(current_savings, goal):
  return goal - current_savings
#testing and playing:
current_savings = calc_savings(current_savings)
print("1", current_savings)
print("left to go: ",amount_to_go(current_savings, goal))
current_savings = calc_savings(current_savings)
print("2", current_savings)
print("left to go: ",amount_to_go(current_savings, goal))
current_savings = calc_savings(current_savings)
print("3", current_savings)
print("left to go: ",amount_to_go(current_savings, goal))

