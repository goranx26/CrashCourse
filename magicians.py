def show_magicians(mag_list):
    for magician in mag_list:
        print(magician)

def greatify(mag_list):
    i=0
    for mag in mag_list:
        mag_list[i]="The great "+mag.title()
        i=i+1
    return mag_list

magician_list=['joe labero','merlin','trollfar','dracula']

great_list=greatify(magician_list[:])
show_magicians(magician_list)
show_magicians(great_list)
