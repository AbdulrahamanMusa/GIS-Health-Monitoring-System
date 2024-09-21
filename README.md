## GIS-Health-System:
 Visualizing and Analyzing Healthcare Data. This application provides a comprehensive platform for visualising and analyzing healthcare data, specifically focusing on health facility scores and survey responses. It leverages the power of GIS mapping, interactive dashboards, and data analysis tools to provide actionable insights for stakeholders in the healthcare sector.
 


## Features:
Interactive Mapping: Visualize the geographical distribution of healthcare facilities across different states in Nigeria. Each facility is marked with a health score, providing a clear overview of areas with high and low performance.
## Data Integration and Analysis: 
Seamlessly integrate survey data collected through KoboToolbox, a powerful data collection platform. The app cleans, processes, and stores this data in a SQL database for further analysis.
 

##  Data Exploration and Visualization: 
Explore key variables from the survey data using interactive plots and frequency distributions. Gain insights into demographics, health indicators, and other relevant factors.
 


## User-Friendly Interface: 
Navigate effortlessly through the app using a user-friendly sidebar menu. The landing page provides a clear overview of the app's capabilities, while the interactive map and data analysis sections offer in-depth exploration tools.
## Technologies Used:
Python: The core application is built using Python, a versatile programming language widely used for data analysis and visualisation.
## Shiny for Python: A framework for building interactive web applications in Python, enabling users to explore data and interact with the app in real time.
## Shiny Semantic: A library that provides a collection of UI elements based on the Semantic UI framework, enhancing the visual appeal and user experience of the app.
##  Folium: A Python library built on top of Leaflet.js, used for creating interactive maps.
## SQLite: A lightweight database engine used to store and manage the survey data.
KoboToolbox API: Integrates with the KoboToolbox API to retrieve survey data directly into the application.
## How it Works:
Data Collection: Survey data is collected using KoboToolbox and stored securely on their servers.
## Data Retrieval: The app uses the KoboToolbox API to retrieve the collected data and store it in a local SQLite database.
## Data Processing and Analysis: The retrieved data is cleaned, processed, and analyzed to generate relevant insights.
## Interactive Visualization: The processed data is visualized using interactive maps, plots, and tables, providing users with a comprehensive view of the healthcare landscape.
## Getting Started:
Installation: Clone the repository and install the necessary dependencies.
Configuration: Configure the app to connect to your KoboToolbox account and database.
Running the App: Run the main Python script to launch the application.

## Acknowledgements:
Posit for developing Shiny for Python.
Appsilon for shiny_semantic.
eHealth Africa for providing insightful learning materials and data.


[App Link](https://am-datasolution.shinyapps.io/gis-health-system/)


[Full Article for this App](https://am-datasolution.com/posts/giskobo/)