import csv
with open('test1.csv',newline='') as csvfile:
    a = csv.reader(csvfile)
    lst = []
    for row in a:
        lst.append((','.join(row)).split('\t'))
def main(lst):
    all_population(lst)
    male_population(lst)
    female_population(lst)

def all_population(lst):
    over_fifteen = list(map(int, lst[0]))
    total_labor_force = list(map(int, lst[1]))
    employed = list(map(int, lst[2]))
    unemployed = list(map(int, lst[3]))
    seasonally_inactive_labor_force = list(map(int, lst[4]))
    person_not_in_labor_force = list(map(int, lst[5]))
    print(over_fifteen)
    print(total_labor_force)
    print(employed)
    print(unemployed)
    print(seasonally_inactive_labor_force)
    print(person_not_in_labor_force)
    print()

def male_population(lst):
    over_fifteen_m = list(map(int, lst[7]))
    total_labor_force_m = list(map(int, lst[8]))
    employed_m = list(map(int, lst[9]))
    unemployed_m = list(map(int, lst[10]))
    seasonally_inactive_labor_force_m = list(map(int, lst[11]))
    person_not_in_labor_force_m = list(map(int, lst[12]))
    print(over_fifteen_m)
    print(total_labor_force_m)
    print(employed_m)
    print(unemployed_m)
    print(seasonally_inactive_labor_force_m)
    print(person_not_in_labor_force_m)
    print()

def female_population(lst):
    over_fifteen_f = list(map(int, lst[14]))
    total_labor_force_f = list(map(int, lst[15]))
    employed_f = list(map(int, lst[16]))
    unemployed_f = list(map(int, lst[17]))
    seasonally_inactive_labor_force_f = list(map(int, lst[18]))
    person_not_in_labor_force_f = list(map(int, lst[19]))
    print(over_fifteen_f)
    print(total_labor_force_f)
    print(employed_f)
    print(unemployed_f)
    print(seasonally_inactive_labor_force_f)
    print(person_not_in_labor_force_f)
    print()

main(lst)
