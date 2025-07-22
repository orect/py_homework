def senior_salary(path):
    total = 0
    count = 0

    with open(path, 'r') as file:
        for line in file:
            name, role, salary = line.strip().split(',')
            if role.lower() == 'senior':
                total += int(salary)
                count += 1

    if count == 0:
        return (0, 0)

    average_senior = round(total / count, 2)
    return (total, average_senior)

path = 'employees.txt'

result = senior_salary(path)

if result:
    print(f"Загальна зарплата сеньйорів: {result[0]}")
    print(f"Середня зарплата сеньйорів: {result[1]}")
