print("Welcome to my program")

company_name = input("Please enter the company name:")

feet_of_cable = input("Please enter the number of feet of cable:")

feet_of_cable = float(feet_of_cable)

cost_of_cable = feet_of_cable  # * .87

if feet_of_cable > 100:
  cost_of_cable = feet_of_cable * .80
if feet_of_cable > 250:
  cost_of_cable = feet_of_cable * .75
if feet_of_cable > 500:
  cost_of_cable = feet_of_cable * .50

message = "The cost is: " + str(cost_of_cable) + " for " + str(company_name)

print(message)
