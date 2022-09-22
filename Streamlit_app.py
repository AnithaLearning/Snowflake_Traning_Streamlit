
import streamlit

streamlit.title ( 'The Home Care Service')

streamlit.header ( ' 🍞 Connect to the home care service person')

streamlit.text ( ' 🐔 Home care services can be found for the following Services')

streamlit.text ( ' 🥣 Cooking , Cleaning , Washing , Helping Elders')

streamlit.header ( '🍌🥭 Find Your Own Home carer 🥝🍇' )

import pandas

my_fruit_list =pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")



# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
