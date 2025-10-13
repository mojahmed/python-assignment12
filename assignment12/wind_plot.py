import plotly.express as px
import plotly.data as pldata

# Load the wind dataset
df = pldata.wind(return_type='pandas')

# Print first and last 10 rows
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

## Remove non-numbers and convert to float
df['strength'] = df['strength'].str.replace(r'\D', '', regex=True)  # keep only digits
df['strength'] = df['strength'].astype(float)  # tis will convert to float

# Create an interactive scatter plot: strength vs. frequency
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs. Frequency by Direction',
    hover_data=['direction']
)

# save the plot as HTML
fig.write_html("wind.html", auto_open=True)
