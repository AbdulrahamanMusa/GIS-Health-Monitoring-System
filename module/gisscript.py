#===================GIS===============
from shiny import *
from htmltools import div, tags
from shiny.ui import output_text, tags
from shiny_semantic.elements import segment
import pandas as pd
import geopandas 
import matplotlib.pyplot as plt
import folium  # Or your preferred mapping library
from folium.plugins import Draw
from folium.plugins import TagFilterButton
from shapely.geometry import Point
from folium.plugins import Draw, Fullscreen, Geocoder, LocateControl

    

df1 = pd.read_csv("# replace the with your csv datafile.csv") 

df = df1.loc[:, ("hf_name", "hf_total_score","latitude","longitude","state_name","lga_name"	,"senatorial_district","globalid","hf_uuid")]

# Create point geometries
geometry = geopandas.points_from_xy(df.longitude, df.latitude)
geo_df = geopandas.GeoDataFrame(
    df, geometry=geometry
)

def style_function(feature):
    props = feature.get('properties')
    markup = f"""
        <a href="{props.get('url')}">
            <div style="font-size: 0.8em;">
            <div style="width: 10px;
                        height: 10px;
                        border: 1px solid black;
                        border-radius: 5px;
                        background-color: orange;">
            </div>
            {props.get('name')}
        </div>
        </a>
    """
    return {"html": markup}

@module.ui
def UIgis():
    return segment(ui.output_ui("map_output")),

@module.server
def server(input: Inputs, output: Outputs, session: Session):
  #==================GIS section========
    @output
    @render.ui
    def map_output():
         
        # Create a Folium map centered around Nigeria
        m = folium.Map(location=[9.0820, 8.6753], zoom_start=6, tiles="OpenStreetMap")  # Centered around Nigeria

        # Define marker colors (you can customize these)
        marker_colors = ["red", "orange", "green", "blue", "purple", "pink", 
                        "brown", "gray", "black", "darkred", "lightblue", "beige"]
    
        # Add GeoJSON layer for each state with markers for LGAs
        for state in geo_df["state_name"].unique():
            state_data = geo_df[geo_df["state_name"] == state]
            
            # Create a FeatureGroup for the state
            fg = folium.FeatureGroup(name=state)
            
            # Add markers for each LGA within the state
            for index, row in state_data.iterrows():
                # Cycle through marker colors
                color_index = index % len(marker_colors) 
                
                 # Create the marker label combining hf_name and hf_total_score
                label_text = f"{row['hf_name']}: {row['hf_total_score']}"
                
                folium.Marker(
                    location=[row["latitude"], row["longitude"]],
                    popup=folium.Popup(
                        f"<strong>State:</strong> {row['state_name']}<br>"
                        f"<strong>LGA:</strong> {row['lga_name']}<br>"
                        f"<strong>Health Facility:</strong> {row['hf_name']}<br>"
                        f"<strong>Health Facility Total Score:</strong> {row['hf_total_score']}<br>"
                        f"<strong>Age Range:</strong> {row['senatorial_district']}<br>"
                        f"<strong>globalid:</strong> {row['globalid']}"
                    ),
                    icon=folium.Icon(color=marker_colors[color_index], icon="info-sign"), tooltip=label_text
                ).add_to(fg)
            # Add the FeatureGroup to the map
                fg.add_to(m)
        # Add map controls
        # folium.plugins.Draw(export=True).add_to(m)
        folium.LayerControl().add_to(m)
        folium.LatLngPopup().add_to(m)
        folium.plugins.Fullscreen(
            position="topright",
            title="Expand me",
            title_cancel="Exit me",
            force_separate_button=True,
        ).add_to(m)

        # Correct TagFilterButton usage (assuming 'State' is the property to filter by)
        # TagFilterButton('state_name').add_to(m)  

        folium.plugins.Geocoder().add_to(m)
        folium.plugins.LocateControl(auto_start=False).add_to(m)     
        return ui.TagList(
            ui.HTML(m._repr_html_())
        )
    