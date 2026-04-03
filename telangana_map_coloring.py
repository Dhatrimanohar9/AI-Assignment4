districts = ['Adilabad', 'Nizamabad', 'Karimnagar', 'Warangal', 'Khammam']

neighbors = {
    'Adilabad': ['Nizamabad'],
    'Nizamabad': ['Adilabad', 'Karimnagar'],
    'Karimnagar': ['Nizamabad', 'Warangal'],
    'Warangal': ['Karimnagar', 'Khammam'],
    'Khammam': ['Warangal']
}

colors = ['Red', 'Green', 'Blue']

def is_valid(d, color, assignment):
    for n in neighbors[d]:
        if n in assignment and assignment[n] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    for d in districts:
        if d not in assignment:
            for color in colors:
                if is_valid(d, color, assignment):
                    assignment[d] = color
                    result = backtrack(assignment)
                    if result:
                        return result
                    del assignment[d]
            return None

print(backtrack({}))