def basic_salary(hourly_rate, hours_worked_per_week):
    return hourly_rate*hours_worked_per_week*4

def overtime_salary(hourly_rate, hours_worked):
    return hourly_rate*1.5*hours_worked*4

def total_salary(hourly_rate, hours_worked_per_week):
    if(hours_worked_per_week>40):
        extra_hour_per_week = hours_worked_per_week-40
        return basic_salary(hourly_rate,40)+overtime_salary(hourly_rate,extra_hour_per_week)
    else:
        return basic_salary(hourly_rate,hours_worked_per_week)


hourly_rate = float(input('Enter the hourly rate of the person: $'))
hours_worked_per_week = int(input('Enter the hours worked by the person per week: '))

print('Total Salary : $', total_salary(hourly_rate, hours_worked_per_week))
