import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Inicjalizacja 
app = dash.Dash(__name__)

# Przykładowy Dataframe
today = datetime.date.today()
date_list = [today - datetime.timedelta(days=x) for x in range(7)]
my_duration_time = [60, 120, 90, 45, 30, 75, 100]
data = {
    'Data': date_list,
    'Czas_trwania': my_duration_time,
    'Kolor': ['green'] * len(date_list)
}
df = pd.DataFrame(data)

# Układ wykresu
app.layout = html.Div(children=[
    html.H1('Wykres Dash z ostatnich 7 dni'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['Data'], 'y': df['Czas_trwania'], 'type': 'bar', 'name': 'Czas trwania',
                 'marker': {'color': 'green'}} 
            ],
            'layout': {
                'title': 'Czasy trwania zadań z ostatnich 7 dni',
                'xaxis': {'title': 'Data'},
                'yaxis': {'title': 'Czas trwania (min)'},
                }
            }
    )
])

# Uruchamiam apkę
if __name__ == '__main__':
    app.run_server(debug=True)
