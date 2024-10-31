def basic_salary(hourly_rate, hours_worked_per_week):
    bs = hourly_rate * hours_worked_per_week * 4
    print('Basic Salary : $', format(bs, '.2f'))
    gross_salary(bs)
    return bs

def gross_salary(bs):
    tax = tax_amount(bs)
    allowances = 0.2 * bs
    gs = bs + allowances - tax
    print('Gross Salary : $', format(gs, '.2f'))
    salary_bracket(gs)

def overtime_salary(hourly_rate, hours_worked):
    return hourly_rate * 1.5 * hours_worked * 4

def total_salary(hourly_rate, hours_worked_per_week):
    if hours_worked_per_week > 40:
        extra_hour_per_week = hours_worked_per_week - 40
        ts = basic_salary(hourly_rate, 40) + overtime_salary(hourly_rate, extra_hour_per_week)
    else:
        ts = basic_salary(hourly_rate, hours_worked_per_week)
    print('Total Salary : $', format(ts, '.2f'))

def tax_amount(basic_salary):
    if basic_salary < 60000:
        tax = 0.1 * basic_salary
        print('Tax Deducted : $', format(tax, '.2f'))
        return tax
    elif basic_salary >= 60000 and basic_salary <= 85000:
        tax = 0.15 * basic_salary
        print('Tax Deducted : $', format(tax, '.2f'))
        return tax
    else:
        tax = 0.2 * basic_salary
        print('Tax Deducted : $', format(tax, '.2f'))
        return tax

def salary_bracket(gross_salary):
    if gross_salary < 50000:
        print('Low Income')
    elif gross_salary >= 50000 and gross_salary <= 80000:
        print('Middle Income')
    else:
        print('High Income')

def employee_report(name, hr, hrw):
    print('Employee Name:', name)
    total_salary(hr, hrw)

names = []
hrs = []
hrws = []

print('Employee Database')
print('==================================')
num_employees = int(input('Enter the input of the number of Employees: '))

for i in range(num_employees):
    emp_name = input('Enter Employee ' + str(i+1) + ' name: ')
    names.append(emp_name)
    hourly_rate = float(input('Enter the hourly rate of Employee ' + str(i+1) + ': $'))
    hrs.append(hourly_rate)
    hours_worked_per_week = int(input('Enter the hours worked by Employee ' + str(i+1) + ' per week: '))
    hrws.append(hours_worked_per_week)
print('----------------------------------')
for i in range(num_employees):
    employee_report(names[i], hrs[i], hrws[i])
    print('----------------------------------')
