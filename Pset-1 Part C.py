#input
annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save,  as a  decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))
semi_annual_raise=float(input("Enter the semiannual raise, as  a  decimal:")) 

#vairable
month=1
n=0
money=(annual_salary*portion_saved)/12 

#boringformula
while (money<=total_cost*0.25):
  current_savings=(annual_salary*portion_saved)/12
  month=month+1
  if month%6==0:
    n=n+1
  if month==6*n+1:
    annual_salary=annual_salary+annual_salary*semi_annual_raise
    money=money*(0.04/12)+money+current_savings
  else:
    money=money*(0.04/12)+money+current_savings 
#boringresult
print("Number of months:",month)
