import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
# create a function
def get_fruityvice_data(fruit_choice):
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        return fruityvice_normalized
         
streamlit.header('🍌🥭🥝 Fruityvice Fruit Advice !🍌🥭🥝')
try:
     # Let user select enter a fruit name
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get info.") 
    else:
        back_from_function = get_fruityvice_data(fruit_choice) 
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()
        
streamlit.write('The user entered ', fruit_choice)

 

streamlit.header("The Fruit load list contains:")
# snowflake related fucntions 
def get_fruit_load_list():
        with my_cnx.cursor() as my_cur:
                my_cur.execute("SELECT * from fruit_load_list")
                my_cur.fetchall()
# add a button to load the fruit 
if streamlit.button('Get fruit load list'):
        my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
        my_data_rows = get_fruit_load_list()
        streamlit.dataframe(my_data_rows)


######  dont run anything past here while we troubleshoot 
streamlit.stop()

fruit_add_by_user = streamlit.text_input('What fruit would you like to add?','')
streamlit.write('Thanks for adding ', fruit_add_by_user)

# test it out 
my_cur.execute("insert into  FRUIT_LOAD_LIST values ('from streamlit')")


