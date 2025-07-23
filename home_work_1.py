def total_salary(path):
    total = 0
    count = 0

    with open(path, 'r') as file:
        for line in file:
            name, salary = line.strip().split(',')
            
            total += int(salary)
            count += 1

    if count == 0:
        return (0, 0)

    average_salary = round(total / count, 2)
    return (total, average_salary)

path = 'employees.txt'

result = total_salary(path)

if result:
    print(f"Загальна зарплата: {result[0]}")
    print(f"Середня зарплата сеньйорів: {result[1]}")
