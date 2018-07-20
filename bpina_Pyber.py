# # Option 1: Pyber

# ![Ride](Images/Ride.png)

# The ride sharing bonanza continues! Seeing the success of notable players like Uber and Lyft, you've decided to join a fledgling ride sharing company of your own. In your latest capacity, you'll be acting as Chief Data Strategist for the company. In this role, you'll be expected to offer data-backed guidance on new opportunities for market differentiation.

# You've since been given access to the company's complete recordset of rides. This contains information about every active driver and historic ride, including details like city, driver count, individual fares, and city type.

# Your objective is to build a [Bubble Plot](https://en.wikipedia.org/wiki/Bubble_chart) that showcases the relationship between four key variables:

# * Average Fare ($) Per City
# * Total Number of Rides Per City
# * Total Number of Drivers Per City
# * City Type (Urban, Suburban, Rural)

# In addition, you will be expected to produce the following three pie charts:

# * % of Total Fares by City Type
# * % of Total Rides by City Type
# * % of Total Drivers by City Type

# As final considerations:

# * You must use the Pandas Library and the Jupyter Notebook.
# * You must use the Matplotlib library.
# * You must include a written description of three observable trends based on the data.
# * You must use proper labeling of your plots, including aspects like: Plot Titles, Axes Labels, Legend Labels, Wedge Percentages, and Wedge Labels.
# * Remember when making your plots to consider aesthetics!
#   * You must stick to the Pyber color scheme (Gold, Light Sky Blue, and Light Coral) in producing your plot and pie charts.
#   * When making your Bubble Plot, experiment with effects like `alpha`, `edgecolor`, and `linewidths`.
#   * When making your Pie Chart, experiment with effects like `shadow`, `startangle`, and `explosion`.
# * See [Starter Workbook](Pyber/pyber_starter.ipynb) for a reference on expected format.


# Include this line to make plots interactive
# %matplotlib notebook

# Import our dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# File Paths
CityFilePath = "data/city_data.csv"
RideFilePath = "data/ride_data.csv"

# Read data into Data Frames
DF_City = pd.read_csv(CityFilePath)
DF_Ride = pd.read_csv(RideFilePath)

# Combine data sets into one data set
DF_Combined = pd.merge(DF_City , DF_Ride , on = "city") 
print(DF_Combined.head())
print(DF_Combined.dtypes)
DF_Combined["fare"] = pd.to_numeric(DF_Combined["fare"] )

###################
# Bubble Plot
###################

# Obtain the x and y coordinates for each of the three city types
UrbanDF = DF_Combined[DF_Combined["type"]=="Urban"]
SuburbanDF = DF_Combined[DF_Combined["type"]=="Suburban"]
RuralDF = DF_Combined[DF_Combined["type"]=="Rural"]

# Circle size correlates to driver count per city (each circle is one city)
# Get count of rides per ride id
UrbanRides = UrbanDF.groupby(["city"]).count()["ride_id"] #giving us the count of rides based on the ride id
SuburbanRides = SuburbanDF.groupby(["city"]).count()["ride_id"]
RuralRides = RuralDF.groupby(["city"]).count()["ride_id"]

# Get the average fare
RuralAvgFare = RuralDF.groupby(["city"]).mean()["fare"]
SuburbanAvgFare = SuburbanDF.groupby(["city"]).mean()["fare"]
UrbanAvgFare = UrbanDF.groupby(["city"]).mean()["fare"]

# Get Driver Count
RuralDriverCount = RuralDF.groupby(["city"]).mean()["driver_count"] #we still use mean function because we want to use the driver count number(38) not add them
SuburbanDriverCount = SuburbanDF.groupby(["city"]).mean()["driver_count"]
UrbanDriverCount = UrbanDF.groupby(["city"]).mean()["driver_count"]

# Build the scatter plots for each city types
plt.scatter(UrbanRides,UrbanAvgFare , s = 8*UrbanDriverCount , c = "gold" , marker = "o" , label = "Urban" , edgecolors = "black" )
plt.scatter(SuburbanRides,SuburbanAvgFare , s = 8*SuburbanDriverCount , c = "lightskyblue" , marker = "o", label = "Suburban", edgecolors = "black")
plt.scatter(RuralRides,RuralAvgFare , s = 8*RuralDriverCount , c = "lightcoral" , marker = "o" , label = "Rural" , edgecolors = "black" )

# Label Axes and Title
plt.xlabel("Ride Sharing Bubble (Scatter) Plot")
plt.ylabel("Average Fare")
plt.title("Pyber: City Type Average Fare")

# Add grid
plt.grid(True)

# Create Legend
plt.legend(loc = "best" , title = "City Type")

# SAave and Show PLot
plt.savefig("Output/bpina_Output_BubblePlot")
plt.show()


#############################
# TOTAL FARES PER CITY TYPE (62 urban, 30 sub) WRONG
#############################

CombinedTotalFaresPerType = DF_Combined.groupby("type").count()["fare"]
print(CombinedTotalFaresPerType)

# Generate List with Keys (Labels)
CityTypeKeys = CombinedTotalFaresPerType.keys()
print(CityTypeKeys)

# Create a Pie Chart
plt.pie(CombinedTotalFaresPerType , labels = CityTypeKeys , autopct = "%1.1f%%" , shadow = True , startangle = 90)

# Set Title
plt.title("Percent of Total Fares by City Type")

# Save and show plot
plt.savefig("Output/bp_output_PieChart_TotalFARESByCityType.png")
plt.show()
plt.axis("equal")


#############################
# TOTAL RIDES PER CITY TYPE (68 URban, 26 sub) RIGHT
#############################

CombinedTotalRidesPerType = DF_Combined.groupby("type").count()["ride_id"]
print(CombinedTotalRidesPerType)

# Create a Pie Chart
plt.pie(CombinedTotalRidesPerType , labels = CityTypeKeys , autopct = "%1.1f%%" , shadow = True , startangle = 90)

# Set Title
plt.title("Percent of Total Rides by City Type")

# Save and show plot
plt.savefig("Output/bp_output_PieChart_TotalRIDESByCityType.png")
plt.show()
plt.axis("equal")

#############################
# TOTAL DRIVERS PER CITY TYPE (80 urban, 16 sub, 2.6 rural) WRONG
#############################

CombinedTotalDriversPerType = DF_Combined.groupby("type").count()["driver_count"]
print(CombinedTotalDriversPerType)

# Create a Pie Chart
plt.pie(CombinedTotalDriversPerType , labels = CityTypeKeys , autopct = "%1.1f%%" , shadow = True , startangle = 90)

# Set Title
plt.title("Percent of Total Drivers by City Type")

# Save and show plot
plt.savefig("Output/bp_output_PieChart_TotalDRIVERSByCityType.png")
plt.show()
plt.axis("equal")