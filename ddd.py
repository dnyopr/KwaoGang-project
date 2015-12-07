import csv
with open('test1.csv',newline='') as csvfile:
    a = csv.reader(csvfile)
    lst = []
    for row in a:
        lst.append((','.join(row)).split('\t'))
    #All
    over_fifteen = lst[0]
    total_labor_force = lst[1]
    employed = lst[2]
    unemployed = lst[3]
    seasonally_inactive_labor_force = lst[4]
    person_not_in_labor_force = lst[5]
    over_fifteen = list(map(int, over_fifteen))
    total_labor_force = list(map(int, total_labor_force))
    employed = list(map(int, employed))
    unemployed = list(map(int, unemployed))
    seasonally_inactive_labor_force = list(map(int, seasonally_inactive_labor_force))
    person_not_in_labor_force = list(map(int, person_not_in_labor_force))
    print(over_fifteen)
    print(total_labor_force)
    print(employed)
    print(unemployed)
    print(seasonally_inactive_labor_force)
    print(person_not_in_labor_force)

    #Male
    over_fifteen_m = lst[7]
    total_labor_force_m = lst[8]
    employed_m = lst[9]
    unemployed_m = lst[10]
    seasonally_inactive_labor_force_m = lst[11]
    person_not_in_labor_force_m = lst[12]
    over_fifteen_m = list(map(int, over_fifteen_m))
    total_labor_force_m = list(map(int, total_labor_force_m))
    employed_m = list(map(int, employed_m))
    unemployed_m = list(map(int, unemployed_m))
    seasonally_inactive_labor_force_m = list(map(int, seasonally_inactive_labor_force_m))
    person_not_in_labor_force_m = list(map(int, person_not_in_labor_force_m))
    print(over_fifteen_m)
    print(total_labor_force_m)
    print(employed_m)
    print(unemployed_m)
    print(seasonally_inactive_labor_force_m)
    print(person_not_in_labor_force_m)

    #Female
    over_fifteen_f = lst[14]
    total_labor_force_f = lst[15]
    employed_f = lst[16]
    unemployed_f = lst[17]
    seasonally_inactive_labor_force_f = lst[18]
    person_not_in_labor_force_f = lst[19]
    over_fifteen_f = list(map(int, over_fifteen_f))
    total_labor_force_f = list(map(int, total_labor_force_f))
    employed_f = list(map(int, employed_f))
    unemployed_f = list(map(int, unemployed_f))
    seasonally_inactive_labor_force_f = list(map(int, seasonally_inactive_labor_force_f))
    person_not_in_labor_force_f = list(map(int, person_not_in_labor_force_f))
    print(over_fifteen_f)
    print(total_labor_force_f)
    print(employed_f)
    print(unemployed_f)
    print(seasonally_inactive_labor_force_f)
    print(person_not_in_labor_force_f)


