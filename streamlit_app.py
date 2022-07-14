import streamlit
import pandas


streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie') 
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# Set the Index Column
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets put a pick list so the customers can pick what they want to include
fruits_selected = streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Strawberries','Cantaloupe'])
# Filter wha users wants to see 
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the data on the page
streamlit.dataframe(fruits_to_show)
# new section to display fruitvice api responce 
import requests
streamlit.header('🍌🥭🥝 Fruityvice Fruit Advice !🍌🥭🥝')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# normalize the json data 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output the data onto a table 
streamlit.dataframe(fruityvice_normalized)
