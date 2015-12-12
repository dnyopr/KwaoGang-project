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


def graph(lst):
    py.sign_in('it58070041', 'bxhjqg6nps')
trace1 = Scatter(
    x=[2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
    y=list(map(str, lst[0])),
    marker=Marker(
        size=12
    ),
    mode='lines+markers',
    name='Over_fifteen',
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
    name='Total_labor_force',
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
    name='seasonally_inactive_labor_force',
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
    name='person_not_in_labor_force',
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
graph(lst)
