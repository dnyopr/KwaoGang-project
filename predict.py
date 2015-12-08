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