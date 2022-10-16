salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
ftopoy = increase+1
pazniza = salary - spend
need_money = 0  # количество денег, чтобы прожить 10 месяцев
for money in range(1, months +1 ):
    money = spend - salary
    spend = spend * ftopoy
    need_money += money
print(round(need_money))
