from shiny import* 
from shiny_semantic.elements import segment
from shiny.types import FileInfo
from datetime import date
from pathlib import Path
import sqlite3
from itables.shiny import DT
from itables import show
from htmltools import TagList, div, tags

#====================kobotoolbox=================
import pykobo
import pandas as pd
# KoboToolbox API Configuration
URL_KOBO = "Your kobo URL"  
API_VERSION = 2
MYTOKEN = "your kobo token" 
km = pykobo.Manager(url=URL_KOBO, api_version=API_VERSION, token=MYTOKEN)
uid= 'Your form ID'
#=================================================

# Create SQLite database connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@module.ui
def UIkobo():
    return  ui.input_action_button("Load_DB_Button1", "Load Data", style = "bordered",),ui.column(12, ui.output_table("form_data_table")),

@module.server
def server(input: Inputs, output: Outputs, session: Session):
    
    @reactive.Calc
    def get_form_data():
        form = km.get_form(uid)
        form.fetch_data()
        return form.data  # Access the DataFrame from the form object

    @render.ui
    @reactive.event(input.Load_DB_Button1)
    def form_data_table():
        kobo_df = get_form_data() 
    
        # Convert columns with list-like data to strings
        for col in kobo_df.columns:
            if kobo_df[col].apply(lambda x: isinstance(x, (list, dict))).any():
                kobo_df[col] = kobo_df[col].astype(str)
        # Append data to the table (don't replace)
        kobo_df.to_sql("kobdata", conn, if_exists='replace', index=False)        
        query = "SELECT * FROM kobdata"
        kdf = pd.read_sql_query(query, conn)
        return  ui.HTML(DT(kdf,select=True, scrollY="350px", scrollCollapse=True, 
                        #    layout={"top": "searchBuilder"}, 
                            keys=True,classes="display nowrap table_with_monospace_font", 
                                                buttons=["pageLength","copyHtml5", "csvHtml5", "excelHtml5",'print'],))
    
    
    @reactive.Effect
    @reactive.event(input.Load_DB_Button1)
    def _():
        m = ui.modal(
            "Data loaded successfully.",
            title="Notification",
            easy_close=True,
            footer=None,
        )
        ui.modal_show(m) 
    
