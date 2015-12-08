import csv
import plotly.plotly as py
from plotly.graph_objs import *
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

def male_population(lst):
    over_fifteen_m = list(map(int, lst[7]))
    total_labor_force_m = list(map(int, lst[8]))
    employed_m = list(map(int, lst[9]))
    unemployed_m = list(map(int, lst[10]))
    seasonally_inactive_labor_force_m = list(map(int, lst[11]))
    person_not_in_labor_force_m = list(map(int, lst[12]))


def female_population(lst):
    over_fifteen_f = list(map(int, lst[14]))
    total_labor_force_f = list(map(int, lst[15]))
    employed_f = list(map(int, lst[16]))
    unemployed_f = list(map(int, lst[17]))
    seasonally_inactive_labor_force_f = list(map(int, lst[18]))
    person_not_in_labor_force_f = list(map(int, lst[19]))


def create_multiple_chart(lst):
    count = 0
    for year in range(10):
        py.sign_in('bankok_bank', 'biay9nqniq')
        trace1 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[lst[0][count], lst[7][count], lst[14][count]],
            marker=Marker(
                color='#86a2d7'
            ),
            name='over_fifteen'
        )
        trace2 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[lst[1][count], lst[8][count], lst[15][count]],
            marker=Marker(
                color='#3aa0ad'
            ),
            name='total_labor_force'
        )
        trace3 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[lst[2][count], lst[9][count], lst[16][count]],
            marker=Marker(
                color='#6b80ce'
            ),
            name='employed'
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
            name='seasonally_inactive_labor_force'
        )
        trace6 = Bar(
            x=['All_population', 'Male_population', 'Female_population'],
            y=[lst[5][count], lst[12][count], lst[19][count]],
            marker=Marker(
                color='#1b3c50'
            ),
            name='person_not_in_labor_force'
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
        
create_multiple_chart(lst)
