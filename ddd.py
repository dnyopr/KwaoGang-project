import csv
import plotly.plotly as py
from plotly.graph_objs import *
with open('test1.csv',newline='') as csvfile:
    a = csv.reader(csvfile)
    lst = []
    for row in a:
        lst.append((','.join(row)).split('\t'))
def main(lst):
    all_population(lst, input())
    male_population(lst)
    female_population(lst)

def all_population(lst, label):
    if label == 'over_fifteen':
        return list(map(str, lst[0]))
    elif label == 'total_labor_force':
        return list(map(str, lst[1]))
    elif label == 'employed':
        return list(map(str, lst[2]))
    elif label == 'unemployed':
        return list(map(str, lst[3]))
    elif label == 'seasonally_inactive_labor_force':
        return list(map(str, lst[4]))
    else:
        return list(map(str, lst[5]))
    
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


def graph():
    py.sign_in('thege3236', '5aniav9wlf')
trace1 = Scatter(
    x=['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016'],
    y=all_population(lst, 'over_fifteen'),
    line=Line(
        color='rgb(156, 124, 156)',
        shape='spline',
        width=3
    ),
    mode='lines',
    name='over_fifteen',
    uid='4163d0'
)
trace2 = Scatter(
    x=['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016'],
    y=['36131982', '36429004', '36941980', '37700387', '38426756', '38643482', '38921507', '39407838', '39383790', '38576232'],
    line=Line(
        color='rgb(211, 127, 100)',
        shape='spline',
        width=3
    ),
    mode='lines',
    name='total_labor_force',
    uid='b4950f'
)
trace3 = Scatter(
    x=['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016'],
    y=['35257173', '35685529', '36249454', '37016612', '37706321', '38037342', '38464667', '38939130', '38906889', '38077429'],
    line=Line(
        color='rgb(139, 202, 177)',
        shape='spline',
        width=3
    ),
    mode='lines',
    name='employed',
    uid='a38cdc'
)
data = Data([trace1, trace2, trace3])
layout = Layout(
    annotations=Annotations([
        Annotation(
            x=0.09999999999999802,
            y=0.29999999999999993,
            align='center',
            arrowcolor='rgba(68, 68, 68, 0)',
            arrowhead=1,
            arrowsize=1,
            arrowwidth=0,
            ax=-46,
            ay=186.48332977294922,
            bgcolor='rgba(0,0,0,0)',
            bordercolor='',
            borderpad=1,
            borderwidth=1,
            font=Font(
                color='',
                family='',
                size=0
            ),
            opacity=1,
            showarrow=True,
            text='Source: <a href="http://www.vox.com/2014/6/13/5804950/teens-are-ditching-booze-and-getting-high-marijuana-alcohol">Vox</a><br>Data: <a href="http://www.cdc.gov/healthyyouth/yrbs/pdf/trends/us_alcohol_trend_yrbs.pdf">CDC</a> (1), <a href="http://www.cdc.gov/healthyyouth/yrbs/pdf/trends/us_tobacco_trend_yrbs.pdf">CDC</a> (2), <a href="http://www.cdc.gov/healthyyouth/yrbs/pdf/trends/us_drug_trend_yrbs.pdf">CDC</a> (3)',
            textangle=0,
            xanchor='auto',
            xref='paper',
            yanchor='auto',
            yref='paper'
        )
    ]),
    autosize=False,
    bargap=0.2,
    bargroupgap=0,
    barmode='group',
    boxgap=0.3,
    boxgroupgap=0.3,
    boxmode='overlay',
    dragmode='zoom',
    font=Font(
        color='#444',
        family='Balto, sans-serif',
        size=12
    ),
    height=600,
    hidesources=False,
    hovermode='x',
    legend=Legend(
        x=0.796875,
        y=0.9285714285714286,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='#444',
        borderwidth=0,
        font=Font(
            color='',
            family='',
            size=0
        ),
        traceorder='normal',
        xanchor='left',
        yanchor='top'
    ),
    margin=Margin(
        r=80,
        t=100,
        autoexpand=True,
        b=80,
        l=80,
        pad=0
    ),
    paper_bgcolor='#fff',
    plot_bgcolor='#fff',
    separators='.,',
    showlegend=True,
    smith=False,
    title='<br>Marijuana Use Fluctuates, Tobacco and Alcohol Use Trending Down<br>Among High School Students',
    titlefont=dict(
        color='',
        family='',
        size=0
    ),
    width=800,
    xaxis=XAxis(
        anchor='y',
        autorange=False,
        autotick=False,
        domain=[0, 1],
        dtick=2,
        exponentformat='B',
        gridcolor='#eee',
        gridwidth=1,
        linecolor='#444',
        linewidth=1,
        mirror=False,
        nticks=15,
        overlaying=False,
        position=0,
        range=[1990.5, 2013.5],
        rangemode='normal',
        showexponent='all',
        showgrid=False,
        showline=False,
        showticklabels=True,
        tick0=1991,
        tickangle='auto',
        tickcolor='#444',
        tickfont=dict(
            color='',
            family='',
            size=0
        ),
        ticklen=5,
        ticks='',
        tickwidth=1,
        title='',
        titlefont=dict(
            color='',
            family='',
            size=0
        ),
        type='linear',
        zeroline=False,
        zerolinecolor='#444',
        zerolinewidth=1
    ),
    yaxis=YAxis(
        anchor='x',
        autorange=True,
        autotick=True,
        domain=[0, 1],
        dtick=10,
        exponentformat='B',
        gridcolor='#eee',
        gridwidth=1,
        linecolor='#444',
        linewidth=1,
        mirror=False,
        nticks=0,
        overlaying=False,
        position=0,
        range=[0, 54.31578947368421],
        rangemode='tozero',
        showexponent='all',
        showgrid=True,
        showline=False,
        showticklabels=True,
        tick0=0,
        tickangle='auto',
        tickcolor='#444',
        tickfont=dict(
            color='',
            family='',
            size=0
        ),
        ticklen=5,
        ticks='',
        tickwidth=1,
        title='Percent Using, Past 30 Days',
        titlefont=dict(
            color='',
            family='',
            size=0
        ),
        type='linear',
        zeroline=True,
        zerolinecolor='#444',
        zerolinewidth=1
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(data, filename='date-axes')
graph()
