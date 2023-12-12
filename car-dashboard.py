import streamlit as st
import pandas as pd
import plotly.express as px

MSRP = pd.read_csv('data.csv')

url = 'https://www.canstarblue.com.au/vehicles/car-country-of-origin/'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print("Failed to retrieve the page. Status code:", response.status_code)

table = soup.find('h2', text='Car Brands – Country of Origin').find_next('table')

data = []
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    row_data = [col.get_text(strip=True) for col in columns]
    data.append(row_data)

df = pd.DataFrame(data, columns=['Car Brand', 'Country of Origin'])

st.title('Car Data Analysis Dashboard')
st.write('Explore insights from car data analysis')

file_path = '/Users/marynydegger/Documents/FALL2023/STAT386/EDA Project/merged_df'
cars = pd.read_csv(file_path)

#Looking at MSRP with the different features.
st.header('Scatter plot: Engine HP vs Highway MPG colored by MSRP')
st.write('Recommendation: Look at the results in the scatterplot for only one specific MSRP amount, like 2000. Or take it to smaller price ranges.')

msrp_min = int(cars['MSRP'].min())
msrp_max = int(cars['MSRP'].max())
selected_msrp_range = st.slider('Select MSRP Range', msrp_min, msrp_max, (msrp_min, msrp_max))
filtered_data = cars[(cars['MSRP'] >= selected_msrp_range[0]) & (cars['MSRP'] <= selected_msrp_range[1])]

fig = px.scatter(filtered_data, x='Engine HP', y='highway MPG', color='MSRP',
                 title='Engine HP vs Highway MPG colored by MSRP',
                 labels={'Engine HP': 'Engine Horsepower', 'highway MPG': 'Highway MPG', 'MSRP': 'Manufacturer\'s Suggested Retail Price'},
                 hover_name='Make', hover_data=['Model'])

fig.update_layout(xaxis_title='Engine HP', yaxis_title='Highway MPG')
st.plotly_chart(fig)

#Look at the different amounts of models in each country
st.header('Car Distribution Map')
selected_countries = st.multiselect('Select Countries', cars['Country of Origin'].unique())
filtered_data_countries = cars[cars['Country of Origin'].isin(selected_countries)]
country_model_counts = filtered_data_countries['Country of Origin'].value_counts().reset_index()
country_model_counts.columns = ['Country', 'Model Count']
bar_fig = px.bar(country_model_counts, x='Country', y='Model Count', 
                 title='Number of Car Models per Country', 
                 labels={'Country': 'Country', 'Model Count': 'Number of Models'})
bar_fig.update_layout(xaxis_title='Country', yaxis_title='Number of Models')
st.plotly_chart(bar_fig)

#Look at the engine size and horsepower in for certain models.
st.header('Engine Size vs. Horsepower Scatterplot')
selected_models = st.multiselect('Select Car Models', cars['Model'].unique())
filtered_cars = cars[cars['Model'].isin(selected_models)]
scatterplot = px.scatter(filtered_cars, x = 'Engine Cylinders', y = 'Engine HP', color = 'Country of Origin', hover_data = ['Model'])
st.plotly_chart(scatterplot)

#Fuel efficiency across different car sizes
st.header('Fuel Efficiency Across Different Car Sizes by Country of Origin')
widget_key = 'select_countries'

selected_countries = st.multiselect('Select Countries', cars['Country of Origin'].unique(), key=widget_key)
filtered_data = cars[cars['Country of Origin'].isin(selected_countries)]

fig = px.bar(filtered_data, x='Vehicle Size', y=['highway MPG', 'city mpg'], color='Country of Origin',
             barmode='group',
             title='Fuel Efficiency Across Different Car Sizes by Country of Origin',
             labels={'value': 'MPG', 'Vehicle Size': 'Car Size', 'Country of Origin': 'Country'},
             hover_name='Make', hover_data=['Model'])

fig.update_layout(xaxis_title='Car Size', yaxis_title='MPG')
st.plotly_chart(fig)



