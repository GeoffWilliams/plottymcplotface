import plotly.express as px
import pandas as pd

import plotly.offline as offline


def save(filename):
    # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    #
    # fig = px.line(df, x='Date', y='AAPL.High')
    # fig.show()
    # offline.init_notebook_mode()
    # offline.plot({'data': [{'y': [4, 2, 3, 4]}],
    #               'layout': {'title': 'Test Plot',
    #                          'font': dict(family='Comic Sans MS', size=16)}},
    #              auto_open=True, image='png', image_filename='plot_image',
    #              output_type='file', image_width=800, image_height=600,
    #              filename=filename, validate=False)

    import plotly.graph_objects as go
    fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
    fig.write_html(filename, auto_open=True)
