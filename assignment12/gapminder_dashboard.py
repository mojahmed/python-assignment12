from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# Load dataset
df = pldata.gapminder(return_type='pandas')

# Get unique countries for the dropdown
countries = df['country'].drop_duplicates()

# Initialize Dash app
app = Dash(__name__)

# Layout of the app
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in countries],
        value='Canada'  # default selected country
    ),
    dcc.Graph(id='gdp-growth')
])

# Callback to update graph when dropdown changes
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    # Filter dataset for the selected country
    filtered = df[df['country'] == selected_country]
    
    # Create line plot for GDP per capita over years
    fig = px.line(
        filtered,
        x='year',
        y='gdpPercap',
        title=f'GDP per Capita Growth for {selected_country}'
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
