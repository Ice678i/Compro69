heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']

def display_heroes(hero_list):
    print("Heroes List:", hero_list)

def add_hero(hero_list, hero_name):
    return hero_list + [hero_name]

def insert_hero(hero_list, index, hero_name):
    return hero_list[:index] + [hero_name] + hero_list[index:]

def remove_hero(hero_list, hero_name):
    return [h for h in hero_list if h != hero_name]

def get_sorted_heroes(hero_list, reverse=False):
    return sorted(hero_list, reverse=reverse)

display_heroes(heroes)

heroes = add_hero(heroes, "Captain America")
display_heroes(heroes)

heroes = insert_hero(heroes, 1, "Hawkeye")
display_heroes(heroes)

heroes = remove_hero(heroes, "Hulk")
display_heroes(heroes)

print("Ascending:", get_sorted_heroes(heroes))
print("Descending:", get_sorted_heroes(heroes, reverse=True))