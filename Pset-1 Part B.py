#input
annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save,  as a  decimal:"))
total_cost=float(input("Enter the cost of your dream home:")) 

#variables
month=1
current_savings=(annual_salary*portion_saved)/12
money=(annual_salary*portion_saved)/12 

#formula but there are another formula that is derived from geometric series but for now let's forget that ;_;
while (money<=total_cost*0.25):
  month=month+1
  money=money*(0.04/12)+money+current_savings 

#result
print("Number of months:",month)
