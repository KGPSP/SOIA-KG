import streamlit as st
import pandas as pd

# Load the data
data_path = '6-dane.csv'
data = pd.read_csv(data_path)

# Sidebar menu
menu = st.sidebar.radio(
    "Menu",
    ("Informacje podstawowe", "Analiza obiektów", "Mapy", "Kontakt")
)

# Basic Information Page
if menu == "Informacje podstawowe":
    st.title("Informacje podstawowe")
    st.write("Tutaj znajdują się podstawowe informacje o danych.")
    st.write(data.head())  # Display the first few rows of the dataset

# Object Analysis Page
elif menu == "Analiza obiektów":
    st.title("Analiza obiektów")
    st.write("Tutaj możesz przeprowadzić analizę obiektów.")
    st.write(data.describe())  # Display basic statistical analysis

# Maps Page
elif menu == "Mapy":
    st.title("Mapy")
    st.write("Tutaj możesz wyświetlić mapy.")
    # Check if latitude and longitude columns are present
    if 'latitude' in data.columns and 'longitude' in data.columns:
        st.map(data[['latitude', 'longitude']])
    else:
        st.write("Dane nie zawierają informacji o lokalizacji (szerokości i długości geograficznej).")

# Contact Page
elif menu == "Kontakt":
    st.title("Kontakt")
    st.write("Dziękujemy za odwiedzenie naszej aplikacji. W przypadku pytań, prosimy o kontakt pod adresem email@example.com.")

