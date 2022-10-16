money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0
post = 1.05
pazniza = (salary - spend)
while money_capital + pazniza >= spend:
    money_capital += pazniza
    spend = spend * post
    month+= 1
print(month)
