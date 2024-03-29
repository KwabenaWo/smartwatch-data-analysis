# Importing necessary libraries for data analysis and visualization
import pandas as pd        # Pandas: powerful data manipulation library
import numpy as np         # NumPy: fundamental package for scientific computing
import matplotlib.pyplot as plt    # Matplotlib: plotting library for creating static, interactive, and animated visualizations
import plotly.express as px        # Plotly Express: easy-to-use interface for creating interactive plots
import plotly.graph_objects as go  # Plotly Graph Objects: provides more control over plots with a lower-level interface

# Load the daily activity data from the CSV file into a Pandas DataFrame.
data = pd.read_csv("dailyActivity_merged.csv")

# Display the first few rows of the DataFrame to get a glimpse of the data.
print(data.head())

# Displaying concise summary information about the DataFrame 'data'
# including column data types, non-null counts, and memory usage.
print(data.info())

# Converting the datatype of 'ActivityDate' column to datetime format for better time handling.
data["ActivityDate"] = pd.to_datetime(data["ActivityDate"],
                                      format="%m/%d/%Y")

# Printing concise information about the DataFrame to verify the changes.
print(data.info())

# Calculating the total minutes spent across various activity levels.
data["TotalMinutes"] = (
    data["VeryActiveMinutes"] +
    data["FairlyActiveMinutes"] +
    data["LightlyActiveMinutes"] +
    data["SedentaryMinutes"]
)

# Sampling a random subset of total minutes data to analyze.
print(data["TotalMinutes"].sample(5))

#Relationship between Calories and Total Steps

import seaborn as sns

# Visualizing the relationship between Calories and Total Steps with Seaborn.
sns.scatterplot(data=data, x="Calories", y="TotalSteps", size="VeryActiveMinutes")

# Adding a trendline using Ordinary Least Squares regression.
sns.regplot(data=data, x="Calories", y="TotalSteps", scatter=False)

# Adding title to the plot.
plt.title("Relationship between Calories & Total Steps")

# Displaying the plot.
plt.show()

import matplotlib.pyplot as plt

# Calculating the mean of different activity minutes.
activity_counts = data[["VeryActiveMinutes", "FairlyActiveMinutes",
                       "LightlyActiveMinutes", "SedentaryMinutes"]].mean()

# Labels for the pie chart.
labels = ["Very Active Minutes", "Fairly Active Minutes",
          "Lightly Active Minutes", "Inactive Minutes"]

# Generating a gradient of colors.
colors = sns.color_palette("coolwarm", n_colors=len(labels))

# Creating a pie chart using Seaborn.
plt.figure(figsize=(8, 8))
plt.pie(activity_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Adding title to the plot.
plt.title('Total Active Minutes')

# Displaying the plot.
plt.show()

"""
## Observations:

- 81.3% of Total inactive minutes in a day
- 15.8% of Lightly active minutes in a day
- On an average, only 21 minutes (1.74%) were very active
- and 1.11% (13 minutes) of fairly active minutes in a day"""

# Extracting the day name from the 'ActivityDate' column
data["Day"] = data["ActivityDate"].dt.day_name()

# Printing the first few entries of the 'Day' column to display the extracted day names
print(data["Day"].head())

fig = go.Figure()

# Adding Very Active minutes data as a bar trace with customized color and name
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["VeryActiveMinutes"],
    name='Very Active',
    marker_color='#FF5733'  # Customizing the marker color
))

# Adding Fairly Active minutes data as a bar trace with customized color and name
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["FairlyActiveMinutes"],
    name='Fairly Active',
    marker_color='#33FF6E'  # Customizing the marker color
))

# Adding Lightly Active minutes data as a bar trace with customized color and name
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["LightlyActiveMinutes"],
    name='Lightly Active',
    marker_color='#3388FF'  # Customizing the marker color
))

# Updating the layout to set the group bar mode and adjust x-axis tick angles
fig.update_layout(
    barmode='group',  # Setting the bar mode to group
    xaxis_tickangle=-45,  # Rotating x-axis ticks for better readability
    title="Activity Minutes by Day",  # Adding a title to the plot
    xaxis_title="Day",  # Adding a label to the x-axis
    yaxis_title="Minutes",  # Adding a label to the y-axis
    legend_title="Activity Type",  # Adding a title to the legend
    legend=dict(x=0, y=1.0)  # Positioning the legend
)

# Displaying the plot
fig.show()
