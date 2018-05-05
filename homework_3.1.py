
def get_cube_list(mass):
    return [x**3 for x in mass if not (x % 3 or x % 4)]