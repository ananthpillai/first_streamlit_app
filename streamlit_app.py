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
my_fruit_list = my_fruit_list.set_index('Fruits')

# Lets put a pick list so the customers can pick what they want to include

streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))
# display the data on the page
streamlit.dataframe(my_fruit_list)
