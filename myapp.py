from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# Load dataset
df = pldata.gapminder(return_type='pandas')

# Get unique countries for the dropdown
countries = df['country'].drop_duplicates()

# Initialize app
app = Dash(__name__)
server = app.server # for render 

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in countries],
        value='Saudi Arabia'  # default 
    ),
    dcc.Graph(id='gdp-growth')
])

# Callback
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered = df[df['country'] == selected_country]
    fig = px.line(
        filtered,
        x='year',
        y='gdpPercap',
        title=f'GDP per Capita Growth for {selected_country}'
    )
    return fig

# Run 
if __name__ == "__main__":
    app.run(debug=True)
