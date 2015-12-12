"""PREDICT"""
def predict(over_fifteen, total_labor_force, employed, unemployed,\
    seasonally_inactive_labor_force, person_not_in_labor_force,\
    over_fifteen_m, total_labor_force_m, employed_m, unemployed_m,\
    seasonally_inactive_labor_force_m, person_not_in_labor_force_m,\
    over_fifteen_f, total_labor_force_f, employed_f, unemployed_f,\
    seasonally_inactive_labor_force_f, person_not_in_labor_force_f):
    years = []
    for count in range(len(total_labor_force)):
        years.append(count)
    pre_overfif(over_fifteen)                           #pre_over
    pre_totallabor(total_labor_force)                   #pre_total
    pre_employed(employed)                              #pre_emp
    pre_unemployed(unemployed)                          #pre_unemp
    pre_seasonally(seasonally_inactive_labor_force)     #pre_season
    pre_notinlabor(person_not_in_labor_force)           #pre_not_in
    pre_overfif_m(over_fifteen_m)                       #pre_over_m
    pre_totallabor_m(total_labor_force_m)               #pre_total_m
    pre_employed_m(employed_m)                          #pre_emp_m
    pre_unemployed_m(unemployed_m)                      #pre_unemp_m
    pre_seasonally_m(seasonally_inactive_labor_force_m) #pre_season_m
    pre_notinlabor_m(person_not_in_labor_force_m)       #pre_not_in_m
    pre_overfif_f(over_fifteen_f)                       #pre_over_f
    pre_totallabor_f(total_labor_force_f)               #pre_total_f
    pre_employed_f(employed_f)                          #pre_emp_f
    pre_unemployed_f(unemployed_f)                      #pre_unemp_f
    pre_seasonally_f(seasonally_inactive_labor_force_f) #pre_season_f
    pre_notinlabor_f(person_not_in_labor_force_f)       #pre_not_in_f


###all

def pre_overfif(over_fifteen):
    over = over_fifteen
    xy_over = [over[i]*(i+1) for i in range(over)]
    xsquare_over = [j**2 for j in over]
    sumxy_over = sum(xy_over)
    sumxsquare_over = sum(xsquare_over)
    b_over = sumxy_over/sumxsquare_over
    ybar_over = sum(over)/len(over)
    bxbar_over = (sum(years)/len(years))*b_over
    a_over = ybar_over-bxbar_over
    pre_over = a_over+(b_over*len(over))
    over_fifteen.append(pre_over)
    return pre_over

def pre_totallabor(total_labor_force):
    total = total_labor_force
    xy_total = [total[i]*(i+1) for i in range(total)]
    xsquare_total = [j**2 for j in total]
    sumxy_total = sum(xy_totallab)
    sumxsquare_total = sum(xsquare_total)
    b_total = sumxy_total/sumxsquare_total
    ybar_total = sum(total)/len(total)
    bxbar_total = (sum(years)/len(years))*b_total
    a_total = ybar_total-bxbar_total
    pre_total = a_total+(b_total*len(total))
    total_labor_force.append(pre_total)
    return pre_total

def pre_employed(employed):
    xy_employed = [employed[i]*(i+1) for i in range(employed)]
    xsquare_employed = [j**2 for j in employed]
    sumxy_employed = sum(xy_employed)
    sumxsquare_employed = sum(xsquare_employed)
    b_employed = sumxy_employed/sumxsquare_employed
    ybar_employed = sum(employed)/len(employed)
    bxbar_employed = (sum(years)/len(years))*b_employed
    a_employed = ybar_employed-bxbar_employed
    pre_emp = a_employed+(b_employed*len(employed))
    employed.append(pre_emp)
    return pre_emp

def pre_unemployed(unemployed):
    xy_unemployed = [unemployed[i]*(i+1) for i in range(unemployed)]
    xsquare_unemployed = [j**2 for j in unemployed]
    sumxy_unemployed = sum(xy_unemployed)
    sumxsquare_unemployed = sum(xsquare_unemployed)
    b_unemployed = sumxy_unemployed/sumxsquare_unemployed
    ybar_unemployed = sum(unemployed)/len(unemployed)
    bxbar_unemployed = (sum(years)/len(years))*b_unemployed
    a_unemployed = ybar_unemployed-bxbar_unemployed
    pre_unemp = a_unemployed+(b_unemployed*len(unemployed))
    unemployed.append(pre_unemp)
    return pre_unemp

def pre_seasonally(seasonally_inactive_labor_force):
    seasonally = seasonally_inactive_labor_force
    xy_seasonally = [seasonally[i]*(i+1) for i in range(seasonally)]
    xsquare_seasonally = [j**2 for j in seasonally]
    sumxy_seasonally = sum(xy_seasonally)
    sumxsquare_seasonally = sum(xsquare_seasonally)
    b_seasonally = sumxy_seasonally/sumxsquare_seasonally
    ybar_seasonally = sum(seasonally)/len(seasonally)
    bxbar_seasonally = (sum(years)/len(years))*b_seasonally
    a_seasonally = ybar_seasonally-bxbar_seasonally
    pre_season = a_seasonally+(b_seasonally*len(seasonally))
    seasonally_inactive_labor_force.append(pre_season)
    return pre_season

def pre_notinlabor(person_not_in_labor_force):
    not_in = person_not_in_labor_force
    xy_not_in = [not_in[i]*(i+1) for i in range(not_in)]
    xsquare_not_in = [j**2 for j in not_in]
    sumxy_not_in = sum(xy_not_in)
    sumxsquare_not_in = sum(xsquare_not_in)
    b_not_in = sumxy_not_in/sumxsquare_not_in
    ybar_not_in = sum(not_in)/len(not_in)
    bxbar_not_in = (sum(years)/len(years))*b_not_in
    a_not_in = ybar_not_in-bxbar_not_in
    pre_not_in = a_not_in+(b_not_in*len(not_in))
    person_not_in_labor_force.append(pre_not_in)
    return pre_not_in


###male

def pre_overfif_m(over_fifteen_m):
    over = over_fifteen_m
    xy_over = [over[i]*(i+1) for i in range(over)]
    xsquare_over = [j**2 for j in over]
    sumxy_over = sum(xy_over)
    sumxsquare_over = sum(xsquare_over)
    b_over = sumxy_over/sumxsquare_over
    ybar_over = sum(over)/len(over)
    bxbar_over = (sum(years)/len(years))*b_over
    a_over = ybar_over-bxbar_over
    pre_over_m = a_over+(b_over*len(over))
    over_fifteen_m.append(pre_over_m)
    return pre_over_m

def pre_totallabor_m(total_labor_force_m):
    total = total_labor_force_m
    xy_total = [total[i]*(i+1) for i in range(total)]
    xsquare_total = [j**2 for j in total]
    sumxy_total = sum(xy_totallab)
    sumxsquare_total = sum(xsquare_total)
    b_total = sumxy_total/sumxsquare_total
    ybar_total = sum(total)/len(total)
    bxbar_total = (sum(years)/len(years))*b_total
    a_total = ybar_total-bxbar_total
    pre_total_m = a_total+(b_total*len(total))
    total_labor_force_m.append(pre_total_m)
    return pre_total_m

def pre_employed_m(employed_m):
    emp = employed_m
    xy_employed = [emp[i]*(i+1) for i in range(emp)]
    xsquare_employed = [j**2 for j in emp]
    sumxy_employed = sum(xy_employed)
    sumxsquare_employed = sum(xsquare_employed)
    b_employed = sumxy_employed/sumxsquare_employed
    ybar_employed = sum(emp)/len(emp)
    bxbar_employed = (sum(years)/len(years))*b_employed
    a_employed = ybar_employed-bxbar_employed
    pre_emp_m = a_employed+(b_employed*len(emp))
    employed_m.append(pre_emp_m)
    return pre_emp_m

def pre_unemployed_m(unemployed_m):
    unemp = unemployed_m
    xy_unemployed = [unemp[i]*(i+1) for i in range(unemp)]
    xsquare_unemployed = [j**2 for j in unemp]
    sumxy_unemployed = sum(xy_unemployed)
    sumxsquare_unemployed = sum(xsquare_unemployed)
    b_unemployed = sumxy_unemployed/sumxsquare_unemployed
    ybar_unemployed = sum(unemp)/len(unemp)
    bxbar_unemployed = (sum(years)/len(years))*b_unemployed
    a_unemployed = ybar_unemployed-bxbar_unemployed
    pre_unemp_m = a_unemployed+(b_unemployed*len(unemp))
    unemployed_m.append(pre_unemp_m)
    return pre_unemp_m

def pre_seasonally_m(seasonally_inactive_labor_force_m):
    seasonally = seasonally_inactive_labor_force_m
    xy_seasonally = [seasonally[i]*(i+1) for i in range(seasonally)]
    xsquare_seasonally = [j**2 for j in seasonally]
    sumxy_seasonally = sum(xy_seasonally)
    sumxsquare_seasonally = sum(xsquare_seasonally)
    b_seasonally = sumxy_seasonally/sumxsquare_seasonally
    ybar_seasonally = sum(seasonally)/len(seasonally)
    bxbar_seasonally = (sum(years)/len(years))*b_seasonally
    a_seasonally = ybar_seasonally-bxbar_seasonally
    pre_season_m = a_seasonally+(b_seasonally*len(seasonally))
    seasonally_inactive_labor_force_m.append(pre_season_m)
    return pre_season_m

def pre_notinlabor_m(person_not_in_labor_force_m):
    not_in = person_not_in_labor_force_m
    xy_not_in = [not_in[i]*(i+1) for i in range(not_in)]
    xsquare_not_in = [j**2 for j in not_in]
    sumxy_not_in = sum(xy_not_in)
    sumxsquare_not_in = sum(xsquare_not_in)
    b_not_in = sumxy_not_in/sumxsquare_not_in
    ybar_not_in = sum(not_in)/len(not_in)
    bxbar_not_in = (sum(years)/len(years))*b_not_in
    a_not_in = ybar_not_in-bxbar_not_in
    pre_not_in_m = a_not_in+(b_not_in*len(not_in))
    person_not_in_labor_force_m.append(pre_not_in_m)
    return pre_not_in_m


###female

def pre_overfif_f(over_fifteen_f):
    over = over_fifteen_f
    xy_over = [over[i]*(i+1) for i in range(over)]
    xsquare_over = [j**2 for j in over]
    sumxy_over = sum(xy_over)
    sumxsquare_over = sum(xsquare_over)
    b_over = sumxy_over/sumxsquare_over
    ybar_over = sum(over)/len(over)
    bxbar_over = (sum(years)/len(years))*b_over
    a_over = ybar_over-bxbar_over
    pre_over_f = a_over+(b_over*len(over))
    over_fifteen_f.append(pre_over_f)
    return pre_over_f

def pre_totallabor_f(total_labor_force_f):
    total = total_labor_force_f
    xy_total = [total[i]*(i+1) for i in range(total)]
    xsquare_total = [j**2 for j in total]
    sumxy_total = sum(xy_totallab)
    sumxsquare_total = sum(xsquare_total)
    b_total = sumxy_total/sumxsquare_total
    ybar_total = sum(total)/len(total)
    bxbar_total = (sum(years)/len(years))*b_total
    a_total = ybar_total-bxbar_total
    pre_total_f = a_total+(b_total*len(total))
    total_labor_force_f.append(pre_total_f)
    return pre_total_f

def pre_employed_f(employed_f):
    emp = employed_f
    xy_employed = [emp[i]*(i+1) for i in range(emp)]
    xsquare_employed = [j**2 for j in emp]
    sumxy_employed = sum(xy_employed)
    sumxsquare_employed = sum(xsquare_employed)
    b_employed = sumxy_employed/sumxsquare_employed
    ybar_employed = sum(emp)/len(emp)
    bxbar_employed = (sum(years)/len(years))*b_employed
    a_employed = ybar_employed-bxbar_employed
    pre_emp_f = a_employed+(b_employed*len(emp))
    employed_f.append(pre_emp_f)
    return pre_emp_f

def pre_unemployed_f(unemployed_f):
    unemp = unemployed_f
    xy_unemployed = [unemp[i]*(i+1) for i in range(unemp)]
    xsquare_unemployed = [j**2 for j in unemp]
    sumxy_unemployed = sum(xy_unemployed)
    sumxsquare_unemployed = sum(xsquare_unemployed)
    b_unemployed = sumxy_unemployed/sumxsquare_unemployed
    ybar_unemployed = sum(unemp)/len(unemp)
    bxbar_unemployed = (sum(years)/len(years))*b_unemployed
    a_unemployed = ybar_unemployed-bxbar_unemployed
    pre_unemp_f = a_unemployed+(b_unemployed*len(unemp))
    unemployed_f.append(pre_unemp_f)
    return pre_unemp_f

def pre_seasonally_f(seasonally_inactive_labor_force_f):
    seasonally = seasonally_inactive_labor_force_f
    xy_seasonally = [seasonally[i]*(i+1) for i in range(seasonally)]
    xsquare_seasonally = [j**2 for j in seasonally]
    sumxy_seasonally = sum(xy_seasonally)
    sumxsquare_seasonally = sum(xsquare_seasonally)
    b_seasonally = sumxy_seasonally/sumxsquare_seasonally
    ybar_seasonally = sum(seasonally)/len(seasonally)
    bxbar_seasonally = (sum(years)/len(years))*b_seasonally
    a_seasonally = ybar_seasonally-bxbar_seasonally
    pre_season_f = a_seasonally+(b_seasonally*len(seasonally))
    seasonally_inactive_labor_force_f.append(pre_season_f)
    return pre_season_f

def pre_notinlabor_f(person_not_in_labor_force_f):
    not_in = person_not_in_labor_force_f
    xy_not_in = [not_in[i]*(i+1) for i in range(not_in)]
    xsquare_not_in = [j**2 for j in not_in]
    sumxy_not_in = sum(xy_not_in)
    sumxsquare_not_in = sum(xsquare_not_in)
    b_not_in = sumxy_not_in/sumxsquare_not_in
    ybar_not_in = sum(not_in)/len(not_in)
    bxbar_not_in = (sum(years)/len(years))*b_not_in
    a_not_in = ybar_not_in-bxbar_not_in
    pre_not_in_f = a_not_in+(b_not_in*len(not_in))
    person_not_in_labor_force_f.append(pre_not_in_f)
    return pre_not_in_f

predict()
'''For prediction of 2558'''
def predict_2558(years, popul):
    popul = eval(popul)
    years = eval(years)
    ayear = [ayear - 2547 for ayear in years]
    sum_popul = sum(popul)
    sum_yearpop = sum([ayear[index]*popul[index] for index in range(10)])
    sum_ayear_two = sum([year^2 for year in ayear])
    num_b = sum_yearpop/sum_ayear_two
    num_a = sum(popul) + (num_b*sum(ayear))
    num_predict = num_a + (num_b*11) # 11=2558-2547
    return num_predict