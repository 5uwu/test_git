magician_list = ['Alex','David','Bob','Tommy','Jessica']

def show_magicians(list):
    for magician in list:
        print(magician)

def make_great(list):
    i = 0
    while i < len(list):
        list[i] = "the Great " + list[i]
        i += 1
    return list

# show_magicians(magician_list)
great_magician_list = make_great(magician_list[:])
show_magicians(magician_list)
show_magicians(great_magician_list)