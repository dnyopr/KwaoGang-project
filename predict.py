<<<<<<< HEAD
import csv
with open('test1.csv', newline='') as csvfile:
    a = csv.reader(csvfile)
    lst = []
    for row in a:
        lst.append((','.join(row)).split('\t'))
    over_fifteen = list(map(int, lst[0]))
    total_labor_force = list(map(int, lst[1]))
    employed = list(map(int, lst[2]))
    unemployed = list(map(int, lst[3]))
    seasonally_inactive_labor_force = list(map(int, lst[4]))
    person_not_in_labor_force = list(map(int, lst[5]))
    over_fifteen_m = list(map(int, lst[7]))
    total_labor_force_m = list(map(int, lst[8]))
    employed_m = list(map(int, lst[9]))
    unemployed_m = list(map(int, lst[10]))
    seasonally_inactive_labor_force_m = list(map(int, lst[11]))
    person_not_in_labor_force_m = list(map(int, lst[12]))
    over_fifteen_f = list(map(int, lst[14]))
    total_labor_force_f = list(map(int, lst[15]))
    employed_f = list(map(int, lst[16]))
    unemployed_f = list(map(int, lst[17]))
    seasonally_inactive_labor_force_f = list(map(int, lst[18]))
    person_not_in_labor_force_f = list(map(int, lst[19]))

def predict_5year(over_fifteen, total_labor_force, employed, unemployed,\
    seasonally_inactive_labor_force, person_not_in_labor_force,\
    over_fifteen_m, total_labor_force_m, employed_m, unemployed_m,\
    seasonally_inactive_labor_force_m, person_not_in_labor_force_m,\
    over_fifteen_f, total_labor_force_f, employed_f, unemployed_f,\
    seasonally_inactive_labor_force_f, person_not_in_labor_force_f):
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

def pre_overfif(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_totallabor(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_employed(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_unemployed(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_seasonally(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_notinlabor(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

###male

def pre_overfif_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_totallabor_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_employed_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_unemployed_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_seasonally_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_notinlabor_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

###female

def pre_overfif_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_totallabor_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_employed_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_unemployed_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_seasonally_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_notinlabor_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

predict_5year(over_fifteen, total_labor_force, employed, unemployed,\
    seasonally_inactive_labor_force, person_not_in_labor_force,\
    over_fifteen_m, total_labor_force_m, employed_m, unemployed_m,\
    seasonally_inactive_labor_force_m, person_not_in_labor_force_m,\
    over_fifteen_f, total_labor_force_f, employed_f, unemployed_f,\
    seasonally_inactive_labor_force_f, person_not_in_labor_force_f)
=======
import csv
with open('test1.csv', newline='') as csvfile:
    a = csv.reader(csvfile)
    lst = []
    for row in a:
        lst.append((','.join(row)).split('\t'))
    over_fifteen = list(map(int, lst[0]))
    total_labor_force = list(map(int, lst[1]))
    employed = list(map(int, lst[2]))
    unemployed = list(map(int, lst[3]))
    seasonally_inactive_labor_force = list(map(int, lst[4]))
    person_not_in_labor_force = list(map(int, lst[5]))
    over_fifteen_m = list(map(int, lst[7]))
    total_labor_force_m = list(map(int, lst[8]))
    employed_m = list(map(int, lst[9]))
    unemployed_m = list(map(int, lst[10]))
    seasonally_inactive_labor_force_m = list(map(int, lst[11]))
    person_not_in_labor_force_m = list(map(int, lst[12]))
    over_fifteen_f = list(map(int, lst[14]))
    total_labor_force_f = list(map(int, lst[15]))
    employed_f = list(map(int, lst[16]))
    unemployed_f = list(map(int, lst[17]))
    seasonally_inactive_labor_force_f = list(map(int, lst[18]))
    person_not_in_labor_force_f = list(map(int, lst[19]))

# def predict_5year(over_fifteen, total_labor_force, employed, unemployed,\
#     seasonally_inactive_labor_force, person_not_in_labor_force,\
#     over_fifteen_m, total_labor_force_m, employed_m, unemployed_m,\
#     seasonally_inactive_labor_force_m, person_not_in_labor_force_m,\
#     over_fifteen_f, total_labor_force_f, employed_f, unemployed_f,\
#     seasonally_inactive_labor_force_f, person_not_in_labor_force_f):
    
#     pre_overfif(over_fifteen)                           #pre_over
#     pre_totallabor(total_labor_force)                   #pre_total
#     pre_employed(employed)                              #pre_emp
#     pre_unemployed(unemployed)                          #pre_unemp
#     pre_seasonally(seasonally_inactive_labor_force)     #pre_season
#     pre_notinlabor(person_not_in_labor_force)           #pre_not_in
    
#     pre_overfif_m(over_fifteen_m)                       #pre_over_m
#     pre_totallabor_m(total_labor_force_m)               #pre_total_m
#     pre_employed_m(employed_m)                          #pre_emp_m
#     pre_unemployed_m(unemployed_m)                      #pre_unemp_m
#     pre_seasonally_m(seasonally_inactive_labor_force_m) #pre_season_m
#     pre_notinlabor_m(person_not_in_labor_force_m)       #pre_not_in_m
    
#     pre_overfif_f(over_fifteen_f)                       #pre_over_f
#     pre_totallabor_f(total_labor_force_f)               #pre_total_f
#     pre_employed_f(employed_f)                          #pre_emp_f
#     pre_unemployed_f(unemployed_f)                      #pre_unemp_f
#     pre_seasonally_f(seasonally_inactive_labor_force_f) #pre_season_f
#     pre_notinlabor_f(person_not_in_labor_force_f)       #pre_not_in_f

###all

def pre_overfif(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_totallabor(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_employed(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_unemployed(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_seasonally(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_notinlabor(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

###male

def pre_overfif_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_totallabor_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_employed_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_unemployed_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_seasonally_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_notinlabor_m(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

###female

def pre_overfif_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_totallabor_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_employed_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_unemployed_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_seasonally_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def pre_notinlabor_f(predict):
    year = []
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-9) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-9)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((11*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)
    
    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-5) for i in range(len(predict))])
    xsquare_predict = sum([(j-5)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((6*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-11) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-11)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((13*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i-6) for i in range(len(predict))])
    xsquare_predict = sum([(j-6)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((7*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    y_mean = sum(predict) / len(predict)
    xy_predict = sum([predict[i]*(i*2-13) for i in range(len(predict))])
    xsquare_predict = sum([(j*2-13)**2 for j in range(len(predict))])
    num_b = xy_predict / xsquare_predict
    year_pre = int((15*num_b) + y_mean)
    predict.append(year_pre)
    year.append(year_pre)

    return year

def create_chart(lst):
    count = 0
    for year in range(10):
        py.sign_in('it58070041', 'bxhjqg6nps')
        trace1 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[pre_overfif(list(map(int, lst[0])))[count], lst[7][count], lst[14][count]],
            marker=Marker(
                color='#86a2d7'
            ),
            name='Over fifteen'
        )
        trace2 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[lst[1][count], lst[8][count], lst[15][count]],
            marker=Marker(
                color='#3aa0ad'
            ),
            name='Total labor force'
        )
        trace3 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[lst[2][count], lst[9][count], lst[16][count]],
            marker=Marker(
                color='#6b80ce'
            ),
            name='Employed'
        )
        trace4 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[lst[3][count], lst[10][count], lst[17][count]],
            marker=Marker(
                color='#3b86b2'
            ),
            name='Unemployed'
        )
        trace5 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[lst[4][count], lst[11][count], lst[18][count]],
            marker=Marker(
                color='#2d4686'
            ),
            name='Seasonally inactive labor force'
        )
        trace6 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[lst[5][count], lst[12][count], lst[19][count]],
            marker=Marker(
                color='#1b3c50'
            ),
            name='Person not in labor force'
        )

        data = Data([trace1, trace2, trace3, trace4, trace5, trace6])
        layout = Layout(
            barmode='group',
            paper_bgcolor='#FFF',
            plot_bgcolor='#FFF',
            title='Lines, words and character average in blogposts on noqqe.de',
            xaxis=XAxis(
                exponentformat='none',
                showexponent='none',
                title='',
                type='category'
            ),
            yaxis=YAxis(
                exponentformat='none',
                showexponent='none',
                title=''
            )
        )
        fig = Figure(data=data, layout=layout)
        plot_url = py.plot(data, filename=str(year))

        count += 1
>>>>>>> origin/master
