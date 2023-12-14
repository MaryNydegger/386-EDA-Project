import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Car Data Analysis Dashboard')
st.write('Explore insights from car data analysis')

cars = pd.read_csv('merged_df.csv')

#Looking at MSRP with the different features.
st.header('Scatter plot: Engine HP vs Highway MPG colored by MSRP')
st.write('Recommended ranges: 2000, 2000 - 10,000, 10,000 - 20,000, 20,000 - 50,000, 50,000 +.')

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

st.write('The lower MSRPs have much higher volume of observations, so I found those more interesting to look a and see how the MPG and horsepower vary between those. Check out my suggested ranges.')


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

st.write('This is a quick and easy way to visualize the amounts of models each country has and compare them against each other.')

#Look at the MSRP of certain makes and engine sizes.
st.header('Car Make vs. Engine Size vs. MPG Scatterplot')
selected_car_make = st.multiselect('Select Vehicle Make', cars['Make'].unique())
filtered_cars = cars[cars['Make'].isin(selected_car_make)]
selected_engine_size = st.multiselect('Select Vehicle Size', cars['Vehicle Size'].unique())
filtered_cars = filtered_cars[filtered_cars['Vehicle Size'].isin(selected_engine_size)]
scatterplot = px.scatter(filtered_cars, x='Make', y='city mpg', color='Vehicle Size', hover_data=['Country of Origin'])
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

st.write('I thought this was one of the most interesting visualizations because you can view multiple features at once. I would suggest looking at America and Germany together. These countries both are some of the top model producers, but the MPG for larger American cars is substantially higher than in Germany. The other vehicle sizes have closer results so I would have expected that too.')

st.markdown("[Car Pricing Data Compilation](https://marynydegger.github.io/my-blog/2023/11/17/Car-Pricing-Data-Compilation.html)")
st.markdown("[Car Features EDA](https://marynydegger.github.io/my-blog/2023/12/07/Car-Features-EDA.html)")
st.markdown("[Github Repository](https://github.com/MaryNydegger/386-EDA-Project)")




