# The libraries you have to use
import pandas as pd
import matplotlib.pyplot as plt

# Some extra libraries to build the webapp
import streamlit as st


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.write("Interactive Project to load a dataset with information about Netflix Movies and Series, extract some insights usign Pandas and displaying them with Matplotlib.")
    st.write("Data extracted from: https://www.kaggle.com/datasets/shivamb/netflix-shows (with some cleaning and modifications)")


# ----- Title of the page -----
st.title("🎬 Netflix Data Analysis")
st.divider()


# ----- Loading the dataset -----

@st.cache_data
def load_data():
    data_path = "data/netflix_titles.csv"

    movies_df =pd.read_csv(data_path, index_col='show_id')  # TODO: Ex 2.1: Load the dataset using Pandas, use the data_path variable and set the index column to "show_id"

    return movies_df   # a Pandas DataFrame


movies_df = load_data()

# Displaying the dataset in a expandable table
with st.expander("Check the complete dataset:"):
    st.dataframe(movies_df)


# ----- Extracting some basic information from the dataset -----

# TODO: Ex 2.2: What is the min and max release years?
min_year = movies_df['release_year'].min()
max_year = movies_df['release_year'].max()

# TODO: Ex 2.3: How many director names are missing values (NaN)?
num_missing_directors = movies_df['director'].isna().sum()

# TODO: Ex 2.4: How many different countries are there in the data?
# Fill the NaN (missing) values with the string "Unknown" first.
movies_df['country'] = movies_df['country'].fillna('Unknown')

# Join with ", " all the elements of the list into a single string
all_countries_string = ", ".join(movies_df['country'])

# Split it by ", " to get a list of all the individual countries.
all_countries_list = all_countries_string.split(', ')

n_countries = len(all_countries_list)

# TODO: Ex 2.5: How many characters long are on average the title names?
# Create a new column with the titles length using apply
movies_df['title_length'] = movies_df['title'].apply(lambda x: len(x))

avg_title_length = movies_df['title_length'].mean()


# ----- Displaying the extracted information metrics -----

st.write("##")
st.header("Basic Information")

cols1 = st.columns(5)
cols1[0].metric("Min Release Year", min_year)
cols1[1].metric("Max Release Year", max_year)
cols1[2].metric("Missing Dir. Names", num_missing_directors)
cols1[3].metric("Countries", n_countries)
cols1[4].metric("Avg Title Length", str(round(avg_title_length, 2)) if avg_title_length is not None else None)


# ----- Pie Chart: Top year producer countries -----

st.write("##")
st.header("Top Year Producer Countries")

cols2 = st.columns(2)
year = cols2[0].number_input("Select a year:", min_year, max_year, 2005)

# TODO: Ex 2.6: For a given year, get the Pandas Series of how many movies and series 
# combined were made by every country, limit it to the top 10 countries.
top_10_countries = movies_df.loc[movies_df['release_year'] == year, 'country'].value_counts().head(10)
# Filter the data by year
# Use .loc to filter by the boolean condition for the year
# Then get the value_counts() of the 'country' column
# Finally take the top 10
top_10_countries = movies_df.loc[movies_df['release_year'] == year, 'country'].value_counts().head(10)

print(top_10_countries)

# Code to plot the pie chart from your data results
fig = plt.figure(figsize=(8, 8))
plt.pie(top_10_countries, labels=top_10_countries.index, autopct="%.2f%%")
plt.title(f"Top 10 Countries in {year}")

plt.savefig("top_10_countries_pie.png")
# print(top_10_countries)
if top_10_countries is not None:
    fig = plt.figure(figsize=(8, 8))
    plt.pie(top_10_countries, labels=top_10_countries.index, autopct="%.2f%%")
    plt.title(f"Top 10 Countries in {year}")

    st.pyplot(fig)

else:
    st.subheader("⚠️ You still need to develop the Ex 2.6.")


# ----- Line Chart: Avg duration of movies by year -----

import matplotlib.pyplot as plt

st.write("##")
st.header("Avg Duration of Movies by Year")

# Ex 2.7: Make a line chart of the average duration of movies (not TV shows) in minutes for every year.

# 1. Filter for Movies
movies_only_df = movies_df[movies_df['type'] == 'Movie'].copy()

# 2. Create the duration_minutes column
# We use .copy() above to avoid SettingWithCopyWarning
# We treat the duration string, split it by space, take the first part, and convert to int.
movies_only_df['duration_minutes'] = movies_only_df['duration'].apply(
    lambda x: int(str(x).split(' ')[0]) if isinstance(x, str) else 0
)

# 3. Group by release_year and calculate the mean
movies_avg_duration_per_year = movies_only_df.groupby('release_year')['duration_minutes'].mean()

# 4. Plotting
if movies_avg_duration_per_year is not None and not movies_avg_duration_per_year.empty:
    fig = plt.figure(figsize=(9, 6))
    
    # Generate the line plot
    plt.plot(movies_avg_duration_per_year.index, movies_avg_duration_per_year.values)
    
    # Set titles and labels
    plt.title("Average Duration of Movies Across Years")
    plt.xlabel("Year")
    plt.ylabel("Average Duration (minutes)")
    plt.grid(True)
    
    # Display in Streamlit
    st.pyplot(fig)

else:
    st.subheader("⚠️ You still need to develop the Ex 2.7.")

