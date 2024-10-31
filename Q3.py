def basic_salary(hourly_rate, hours_worked_per_week):
    bs = hourly_rate*hours_worked_per_week*4
    gs = gross_salary(bs)
    return gs

def gross_salary(bs):
    tax = tax_amount(bs)
    allowances = 0.2*bs
    return bs + allowances - tax

def overtime_salary(hourly_rate, hours_worked):
    return hourly_rate*1.5*hours_worked*4

def total_salary(hourly_rate, hours_worked_per_week):
    if(hours_worked_per_week>40):
        extra_hour_per_week = hours_worked_per_week-40
        return basic_salary(hourly_rate,40)+overtime_salary(hourly_rate,extra_hour_per_week)
    else:
        return basic_salary(hourly_rate,hours_worked_per_week)

def tax_amount(basic_salary):
    if(basic_salary<60000):
        tax = 0.1*basic_salary
        print('Tax Deducted: $',tax)
        return tax
    elif(basic_salary >= 60000 and basic_salary <= 85000):
        tax=0.15*basic_salary
        print('Tax Deducted: $',tax)
        return tax
    else:
        tax=0.2*basic_salary
        print('Tax Deducted: $',tax)
        return tax


hourly_rate = float(input('Enter the hourly rate of the person: $'))
hours_worked_per_week = int(input('Enter the hours worked by the person per week: '))

ts = total_salary(hourly_rate, hours_worked_per_week)
print('Total Salary : $',ts)
