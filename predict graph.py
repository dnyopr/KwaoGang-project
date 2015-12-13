'''
Show predict graphs by using data from lists.

    Lines below are kind of lists.
1. All population
    over fifteen = lst[0]
    total labor force = lst[1]
    employed = lst[2]
    unemployed = lst[3]
    seasonally inactive labor force = lst[4]
    person not in labor force = lst[5]
2. Male population
    over fifteen = lst[7]
    total labor force = lst[8]
    employed = lst[9]
    unemployed = lst[10]
    seasonally inactive labor force = lst[11]
    person not in labor force = lst[12]
3. Female population
    over fifteen = lst[14]
    total labor force = lst[15]
    employed = lst[16]
    unemployed = lst[17]
    seasonally inactive labor force = lst[18]
    person not in labor force = lst[19]
'''

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

import csv
import plotly.plotly as py
from plotly.graph_objs import *
with open('test1.csv',newline='') as csvfile:
    a = csv.reader(csvfile)
    lst = [(','.join(row)).split('\t') for row in a]

def create_all_chart(lst):
    count = 0
    for year in range(4):
        py.sign_in('phunpp', '9cjduh3bzn')
        trace1 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[pre_overfif(lst[0][count]), pre_overfif_m(lst[7][count]), pre_overfif_f(lst[14][count])],
            marker=Marker(
                color='#86a2d7'
            ),
            name='Over fifteen'
        )
        trace2 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[pre_totallabor(lst[1][count]), pre_totallabor_m(lst[8][count]), pre_totallabor_f(lst[15][count])],
            marker=Marker(
                color='#3aa0ad'
            ),
            name='Total labor force'
        )
        trace3 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[pre_employed(lst[2][count]), pre_employed_m(lst[9][count]), pre_employed_f(lst[16][count])],
            marker=Marker(
                color='#6b80ce'
            ),
            name='Employed'
        )
        trace4 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[pre_unemployed(lst[3][count]), pre_unemployed_m(lst[10][count]), pre_unemployed_f(lst[17][count])],
            marker=Marker(
                color='#3b86b2'
            ),
            name='Unemployed'
        )
        trace5 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[pre_seasonally(lst[4][count]), pre_seasonally_m(lst[11][count]), pre_seasonally_f(lst[18][count])],
            marker=Marker(
                color='#2d4686'
            ),
            name='Seasonally inactive labor force'
        )
        trace6 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[pre_notinlabor(lst[5][count]), pre_notinlabor_m(lst[12][count]), pre_notinlabor_f(lst[19][count])],
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

        py.sign_in('phunpp', '9cjduh3bzn')
trace1 = Scatter(
    x=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
    y=list(map(str, lst[0])),
    marker=Marker(
        size=12
    ),
    mode='lines+markers',
    name='Over fifteen',
    uid='ebe0393b947e2424868405e02d0fa8c2',
    xsrc='RhettAllain:45:7515eedb1e574665588442b0ced1549b',
    ysrc='RhettAllain:45:4e00758aa75a9cc2afa876ddead953cd'
)
trace2 = Scatter(
    x=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
    y=list(map(str, lst[1])),
        marker=Marker(
        size=12
    ),
    mode='lines+markers',
    name='Total labor force',
    uid='ceb83af3b01ca5c2c296f4e1c2a6a47e',
    xsrc='RhettAllain:45:2170f9fb9db6d6acf13c9cbcef844ced',
    ysrc='RhettAllain:45:641326b589d4672d747c36c1db112711'
)
trace3 = Scatter(
    x=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
    y=list(map(str, lst[2])),
        marker=Marker(
        size=12
    ),
    mode='lines+markers',
    name='Employed',
    uid='ceb83af3b01ca5c2c296f4e1c2a6a47e',
    xsrc='RhettAllain:45:2170f9fb9db6d6acf13c9cbcef844ced',
    ysrc='RhettAllain:45:641326b589d4672d747c36c1db112711'
)
trace4 = Scatter(
    x=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
    y=list(map(str, lst[3])),
        marker=Marker(
        size=12
    ),
    mode='lines+markers',
    name='Unemployed',
    uid='ceb83af3b01ca5c2c296f4e1c2a6a47e',
    xsrc='RhettAllain:45:2170f9fb9db6d6acf13c9cbcef844ced',
    ysrc='RhettAllain:45:641326b589d4672d747c36c1db112711'
)
trace5 = Scatter(
    x=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
    y=list(map(str, lst[4])),
        marker=Marker(
        size=12
    ),
    mode='lines+markers',
    name='Seasonally inactive labor force',
    uid='ceb83af3b01ca5c2c296f4e1c2a6a47e',
    xsrc='RhettAllain:45:2170f9fb9db6d6acf13c9cbcef844ced',
    ysrc='RhettAllain:45:641326b589d4672d747c36c1db112711'
)
trace6 = Scatter(
    x=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
    y=list(map(str, lst[5])),
        marker=Marker(
        size=12
    ),
    mode='lines+markers',
    name='Person not in labor force',
    uid='ceb83af3b01ca5c2c296f4e1c2a6a47e',
    xsrc='RhettAllain:45:2170f9fb9db6d6acf13c9cbcef844ced',
    ysrc='RhettAllain:45:641326b589d4672d747c36c1db112711'
)
data = Data([trace1, trace2, trace3, trace4, trace5, trace6])
layout = Layout(
    autosize=True,
    bargap=0.2,
    bargroupgap=0,
    barmode='stack',
    boxgap=0.3,
    boxgroupgap=0.3,
    boxmode='overlay',
    dragmode='zoom',
    font=Font(
        color='#000',
        family="'Open sans', verdana, arial, sans-serif",
        size=12
    ),
    height=726,
    hovermode='x',
    legend=Legend(
        x=0.013333333333333334,
        y=0.9798534798534798,
        bgcolor='#fff',
        bordercolor='#000',
        borderwidth=1,
        font=Font(
            color='',
            family='',
            size=0
        ),
        traceorder='normal'
    ),
    margin=Margin(
        r=80,
        t=100,
        b=80,
        l=80,
        pad=2
    ),
    paper_bgcolor='#fff',
    plot_bgcolor='#fff',
    separators='.,',
    showlegend=True,
    title='Olympic Medal Volume',
    titlefont=dict(
        color='',
        family='',
        size=0
    ),
    width=1285,
    xaxis=XAxis(
        anchor='y',
        autorange=True,
        autotick=True,
        domain=[0, 1],
        dtick=20,
        exponentformat='e',
        gridcolor='#ddd',
        gridwidth=1,
        linecolor='#000',
        linewidth=1,
        mirror='all',
        nticks=0,
        overlaying=False,
        position=0,
        range=[1888.4586466165413, 2021.5413533834587],
        rangemode='normal',
        showexponent='all',
        showgrid=True,
        showline=True,
        showticklabels=True,
        tick0=0,
        tickangle='auto',
        tickcolor='#000',
        tickfont=dict(
            color='',
            family='',
            size=0
        ),
        ticklen=5,
        ticks='outside',
        tickwidth=1,
        title='Year',
        titlefont=dict(
            color='',
            family='',
            size=0
        ),
        type='linear',
        zeroline=True,
        zerolinecolor='#000',
        zerolinewidth=1
    ),
    yaxis=YAxis(
        anchor='x',
        autorange=True,
        autotick=True,
        domain=[0, 1],
        dtick=20,
        exponentformat='e',
        gridcolor='#ddd',
        gridwidth=1,
        linecolor='#000',
        linewidth=1,
        mirror='all',
        nticks=0,
        overlaying=False,
        position=0,
        range=[-7.9089209286345445, 96.57996704902706],
        rangemode='normal',
        showexponent='all',
        showgrid=True,
        showline=True,
        showticklabels=True,
        tick0=0,
        tickangle='auto',
        tickcolor='#000',
        tickfont=dict(
            color='',
            family='',
            size=0
        ),
        ticklen=5,
        ticks='outside',
        tickwidth=1,
        title='Medal Volume [cm^3]',
        titlefont=dict(
            color='',
            family='',
            size=0
        ),
        type='linear',
        zeroline=True,
        zerolinecolor='#000',
        zerolinewidth=1
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(data, filename='date-axes')
        
create_all_chart(lst)
