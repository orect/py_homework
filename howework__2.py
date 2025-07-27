def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    continue 
                cat_id, name, age = parts
                cat = {"id": cat_id, "name": name, "age": age}
                cats.append(cat)
    except FileNotFoundError:
        print(f"File not found: {path}")
    except IOError:
        print(f"Error reading file: {path}")
    return cats

