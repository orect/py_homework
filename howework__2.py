def get_cats_info(path):
    cats_info = []
    with open(path, 'r') as file:
        for line in file:
            aidi, name, age = line.strip().split(',') 
            cats_dict = {'id': id, 'name': name, 'age': age}
            cats_info.append(cats_dict)
    return cats_info
    

path = 'cats.txt' 
result = get_cats_info(path) 

print(result)


