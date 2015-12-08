"""PREDICT"""
def predict():
    years = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#all
def pre_overfif(over_fifteen):
    over = over_fifteen
    xy_over = [over[i]*(i+1) for i in range(over)]
    xsquare_over = [j**2 for j in over]
    sumxy_over = sum(xy_over)
    sumxsquare_over = sum(xsquare_over)
    b_over = sumxy_over/sumxsquare_over
    ybar_over = sum(over)/len(over)
    bxbar_over = (sum(years)/len(over))*b_over
    a_over = ybar_over-bxbar_over
    pre_over = a_over+(b_over*len(over))
    return(pre_over)


def pre_totallabor(total_labor_force):
    total = total_labor_force
    xy_total = [total[i]*(i+1) for i in range(total)]
    xsquare_total = [j**2 for j in total]
    sumxy_total = sum(xy_totallab)
    sumxsquare_total = sum(xsquare_total)
    b_total = sumxy_total/sumxsquare_total
    ybar_total = sum(total)/len(total)
    bxbar_total = (sum(years)/len(total))*b_total
    a_total = ybar_total-bxbar_total
    pre_total = a_total+(b_total*len(total))
    return(pre_total)

def pre_employed(employed):
    xy_employed = [employed[i]*(i+1) for i in range(employed)]
    xsquare_employed = [j**2 for j in employed]
    sumxy_employed = sum(xy_employed)
    sumxsquare_employed = sum(xsquare_employed)
    b_employed = sumxy_employed/sumxsquare_employed
    ybar_employed = sum(employed)/len(employed)
    bxbar_employed = (sum(years)/len(employed))*b_employed
    a_employed = ybar_employed-bxbar_employed
    pre_employed = a_employed+(b_employed*len(employed))
    return(pre_employed)

def pre_unemployed():


def pre_seasonally():


def pre_notinlabor():
predict()