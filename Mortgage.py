k=float(input("Enter the starting salary:"))
z=0
annual_salary=k
total_cost=1000000
semi_annual_raise=0.07
guess=5000

month=1
n=0
money=(annual_salaryguess/10000)/12 

while (money<=total_cost0.25):
    current_savings=(annual_salaryguess/10000)/12
    month=month+1
    if month%6==0:
        n=n+1
    if month==6n+1:
        annual_salary=annual_salary+annual_salarysemi_annual_raise
        money=money(0.04/12)+money+current_savings
    else:
        money=money(0.04/12)+money+current_savings 
min=0
max=10000
guess=(min+max)/2
while(month!=37):
    z=z+1
    if month>37:min=guess
    if month<37:max=guess
    guess=(min+max)/2
    annual_salary=k
    total_cost=1000000
    semi_annual_raise=0.07
    month=1
    n=0
    money=(annual_salaryguess/10000)/12 
    while (money<=total_cost0.25):
        current_savings=(annual_salaryguess/10000)/12
        month=month+1
        if month%6==0:
            n=n+1
        if month==6n+1:
            annual_salary=annual_salary+annual_salarysemi_annual_raise
            money=money(0.04/12)+money+current_savings
        else:
            money=money(0.04/12)+money+current_savings
    if max==min:
        month=37
        guess="It is not possible to pay the down payment in three years. "
        z=-69
        
print("Best savings rate:"+str(guess))
if z!=-69:
    print("Steps in bisection search:"+str(z))
