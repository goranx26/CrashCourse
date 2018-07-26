import json


def get_stored_drug():
    """Looks for and gets a saved favorite"""
    filename = 'drug.json'
    try:
        with open(filename, encoding='UTF-8') as f_obj:
            fave = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fave


def new_drug():
    """Reads and saves a favorite"""
    fave = input("What is the best drug in the world? ")
    filename = 'drug.json'
    with open(filename, 'w', encoding='UTF-8') as f_obj:
        json.dump(fave, f_obj)
    return fave


def show_drug():
    """Looks for the stored favorite and prints it on screen"""
    fave = get_stored_drug()
    if fave:
        print('Aight! I remember you, we both like ' + fave + "!")
    else:
        fave = new_drug()
        print("Mmmmmmm.... " + fave + " is sweet." )


show_drug()







