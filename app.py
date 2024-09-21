from shiny import* 
from utility import onclick_callback,sidebar,predic_sidebar_ui
from shiny.types import FileInfo
import pandas as pd
from datetime import date
import sqlite3

from itables.shiny import DT
from itables import show
from htmltools import TagList, div, tags
from shiny import render
import matplotlib.pyplot as plt
from shiny_semantic import page_semantic

from shiny_semantic.elements import (
    button,
    header,
    icon,
    segment,
    semantic_input,
    subheader,
    container,
)
import module
from module.about import AppInfo,WorkInfo,model_infor_pop
import re
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt


# Create SQLite database connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

#================Get data from SQL and Select columns 
query = "SELECT * FROM kobdata"
kdf = pd.read_sql_query(query, conn)

def clean_data(kdf):
    kdf.insert(1, "date", kdf.apply(lambda row : row["start"][:row["start"].find(":") - 3], axis=1))
    # Change column type to float16 for column: 'Monthly_Income'
    kdf = kdf.astype({'Monthly_Income': 'float16'})
    # Split text using string '|' in column: '_17_In_your_opinion_of_a_pregnant_woman'
    loc_0 = kdf.columns.get_loc('_17_In_your_opinion_of_a_pregnant_woman')
    df_split = kdf['_17_In_your_opinion_of_a_pregnant_woman'].str.split(pat='|', expand=True).add_prefix('_17_In_your_opinion_of_a_pregnant_woman_')
    kdf = pd.concat([kdf.iloc[:, :loc_0], df_split, kdf.iloc[:, loc_0:]], axis=1)
    kdf = kdf.drop(columns=['_17_In_your_opinion_of_a_pregnant_woman'])
    # Select columns: 'date', 'Age' and 26 other columns
    kdf = kdf.loc[:, ['date', 'Age', 'Ethnicity', 'Religion', 'Marital_status', 'Occupation', 'Education_attainment', 'Monthly_Income', 'Age_of_first_pregnancy', 'Is_this_your_first_pregnancy', 'Born_Alive', 'Howmany_born_alive', 'Parity', 'Gravidity', 'Place_of_Delivery', 'How_Many_ANC', 'Unforseen_problem', '_17_In_your_opinion_of_a_pregnant_woman_1', '_17_In_your_opinion_of_a_pregnant_woman_2', '_17_In_your_opinion_of_a_pregnant_woman_3', '_17_In_your_opinion_of_a_pregnant_woman_4', '_17_In_your_opinion_of_a_pregnant_woman_5', '_17_In_your_opinion_of_a_pregnant_woman_6', '_17_In_your_opinion_of_a_pregnant_woman_7', '_17_In_your_opinion_of_a_pregnant_woman_8', '_17_In_your_opinion_of_a_pregnant_woman_9', '_17_In_your_opinion_of_a_pregnant_woman_10', 'In_your_opinion_cou_these_problems_above']]
    return kdf

df_clean = clean_data(kdf.copy())

#======Kdf-List
my_kdf =['date', 'Age', 'Ethnicity', 'Religion', 'Marital_status', 'Occupation', 'Education_attainment', 'Monthly_Income', 'Age_of_first_pregnancy', 'Is_this_your_first_pregnancy', 'Born_Alive', 'Howmany_born_alive', 'Parity', 'Gravidity', 'Place_of_Delivery', 'How_Many_ANC', 'Unforseen_problem', '_17_In_your_opinion_of_a_pregnant_woman_1', '_17_In_your_opinion_of_a_pregnant_woman_2', '_17_In_your_opinion_of_a_pregnant_woman_3', '_17_In_your_opinion_of_a_pregnant_woman_4', '_17_In_your_opinion_of_a_pregnant_woman_5', '_17_In_your_opinion_of_a_pregnant_woman_6', '_17_In_your_opinion_of_a_pregnant_woman_7', '_17_In_your_opinion_of_a_pregnant_woman_8', '_17_In_your_opinion_of_a_pregnant_woman_9', '_17_In_your_opinion_of_a_pregnant_woman_10', 'In_your_opinion_cou_these_problems_above']


#=======================UI-Part==================
app_ui = page_semantic(
    
    
    sidebar(),
    ui.page_navbar(
        
        ui.nav_panel(
               tags.div(
                tags.i(class_="hamburger icon"),
                class_="ui basic icon button item",
                style="background-color:white;",
                onclick=onclick_callback,
            ),
                # modue inside semantic page
                module.home.Home("homepage"),
                module.data.UIdata("data_section"),
                module.dashboard.UI("dash_section"),
                module.mapg.UImap("map_section"), 
                 
        ),   
         
        ui.nav_panel(
                    tags.div(
                    "Map",
                    class_="ui basic icon button item",
                    style="background-color:white;",
                    ),
                    
                     module.gisscript.UIgis("map_output"),
              ),  
                ui.nav_panel(
                    tags.div(
                    "Data Analysis",
                    class_="ui basic icon button item",
                    style="background-color:white;",
                    ),
                    ui.navset_card_pill(
                        ui.nav_panel("Kobotoolboxdata",
                            ui.h2("Retrieve Survey Data from KoboToolbox"),
                           module.koboscript.UIkobo("kobo_output"),
                        ),  
                    ui.nav_panel("Data-Explorer",
                            ui.layout_sidebar( 
                                      ui.sidebar(
                                    predic_sidebar_ui(),# This function was from the utils
                                    ),
                            ui.layout_columns( ui.output_plot("chart"),ui.card(ui.markdown("Frequency Distribution"),ui.output_data_frame("summary"),),col_widths=[8, 4],row_heights=(1, 2),height="40px",),            
                        
                        #   module.dataanlysis.UIdatanalysis("dataanalysis_output"),
                        height="650px",
                    ),             
                ), 
                ),
              ),     
            ui.nav_panel(
                    tags.div(
                    "About",
                    class_="ui basic icon button item",
                    style="background-color:white;",
                    ),
                    AppInfo(),WorkInfo(),
                ),
            
   ui.nav_spacer(),
  title="GIS-Health-System",
  fillable_mobile=False, 
    bg= "black",
  collapsible = True,
  inverse= True,
    # position='fixed-top',
  footer= ui.strong(ui.h4(ui.HTML("""<marquee> A-Musa Data-Solution @ 2024 </marquee>"""))),
   
 
),# End of Nav_barpage

    
)#end
def server(input, output, session):  
    model_infor_pop()        
#-------modulesegement------
    module.home.server("homepage")
    module.data.server("data_section")
    module.dashboard.server("dash_section")
    module.mapg.server("map_section") 
#==================GIS section========
    module.gisscript.server("map_output")
    
#==============kobotoolbox============
    module.koboscript.server("kobo_output")
 
    #------------------Frequencies      
    @render.data_frame  
    # @reactive.event(input.subDM) 
    def summary():
        selected_cols = input.patient_id()

        if selected_cols:
            freq_tables = [] 
            for col in selected_cols:
                if col in df_clean.columns: 
                    freq_table = df_clean[col].value_counts().to_frame(name='Frequency')
                    freq_table['Percentage'] = (freq_table['Frequency'] / len(df_clean) * 100).round(2)
                    freq_table.index.name = col 
                    freq_tables.append(freq_table)

            if freq_tables:
                result_df = pd.concat(freq_tables, axis=0).reset_index()
                return render.DataTable(result_df)  # Render as DataTable
            else:
                return render.DataTable(pd.DataFrame())  # Empty DataTable
        else:
            return render.DataTable(pd.DataFrame())  # Empty DataTable
        
    @render.plot
    def chart():
        selected_cols = input.patient_id()
        if selected_cols:
            num_plots = len(selected_cols)
            num_cols = 2  # Number of columns in the subplot grid
            num_rows = (num_plots + 1) // num_cols  # Calculate rows needed
    
            fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 7 * num_rows))
            axes = axes.flatten()  # Flatten the axes array for easier iteration
    
            for i, col in enumerate(selected_cols):
                if col in df_clean.columns:
                    freq_table = df_clean[col].value_counts().reset_index()
                    freq_table.columns = ['Category', 'Frequency']
    
                    # Calculate percentage
                    total = len(df_clean[col])
                    percentage = [(count / total) * 100 for count in freq_table['Frequency']]
    
                    axes[i].bar(freq_table['Category'], freq_table['Frequency'])
                    axes[i].set_title(f'{col}')
                    plt.setp(axes[i].get_xticklabels(), rotation=45, ha='right')
    
                    # Add percentage labels on top of bars
                    for j, v in enumerate(percentage):
                        axes[i].text(j, freq_table['Frequency'][j] / 2, f'{v:.1f}%', ha='center', va='bottom', color='black', fontweight='bold')
    
            # Hide any unused subplots
            for j in range(num_plots, len(axes)):
                axes[j].axis('off')
    
            # Adjust subplot spacing
            plt.subplots_adjust(hspace=1.0, wspace=0.4)  # Adjust hspace and wspace as needed
            return fig
    
        else:
            fig, ax = plt.subplots()  # Return an empty plot if no columns are selected
            return fig
    
www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)
