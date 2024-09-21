
from datetime import date

import pandas as pd  

from htmltools import div, tags
from shiny import *
from shiny.ui import output_text, tags

my_kdf =['date', 'Age', 'Ethnicity', 'Religion', 'Marital_status', 'Occupation', 'Education_attainment', 'Monthly_Income', 'Age_of_first_pregnancy', 'Is_this_your_first_pregnancy', 'Born_Alive', 'Howmany_born_alive', 'Parity', 'Gravidity', 'Place_of_Delivery', 'How_Many_ANC', 'Unforseen_problem', '_17_In_your_opinion_of_a_pregnant_woman_1', '_17_In_your_opinion_of_a_pregnant_woman_2', '_17_In_your_opinion_of_a_pregnant_woman_3', '_17_In_your_opinion_of_a_pregnant_woman_4', '_17_In_your_opinion_of_a_pregnant_woman_5', '_17_In_your_opinion_of_a_pregnant_woman_6', '_17_In_your_opinion_of_a_pregnant_woman_7', '_17_In_your_opinion_of_a_pregnant_woman_8', '_17_In_your_opinion_of_a_pregnant_woman_9', '_17_In_your_opinion_of_a_pregnant_woman_10', 'In_your_opinion_cou_these_problems_above']


onclick_callback = """
    $('.ui.sidebar')
        .sidebar({
            transition: 'overlay',
            dimPage: false,
            blurring: true,   
        })
        .sidebar('toggle');
"""


def sidebar():
    def _link(item, icon_name):
        return tags.a(
            ui.div(
                tags.i(class_=f"{icon_name} icon"),
                item,
                class_="item"
            ),
            href=f"#{item}",
            onclick="$('.ui.sidebar').sidebar('toggle');",
        )

    return (
        ui.img( src="static/img/mylogo.png", height="65px",
           style="float: left;",),
        tags.div(
            ui.div(
            ui.tags.a(
            ui.img( src="static/img/mylogo.png", height="80px",
                 style="border-radius: 50%; margin: 1rem auto; display: block;"
                ),
                    href="https://am-datasolution.com/",
            ),
            class_="ui center aligned"
            ),
            ui.hr(class_="horizontal"),
            ui.div(
            _link("Map", "map"),
            _link("Data Pipe Line", "database"),
            _link("Data-Analysis", "chart bar"),
            _link("Live-Map", "globe"),
            ),
            
            style="position: fixed; top: 0; bottom: 0; width: 14%; border-radius: 0 20px 20px 0;",
            class_="ui both vertical menu inverte sidebar",
            inverse= True,

        ),
        
    )
    
    
#=======================data-Analysis-UIpart===============
def predic_sidebar_ui():
    return ui.div(
            ui.input_select(
            "patient_id", 
            "Select Columns for Frequency Analysis:", 
            choices=my_kdf,
            multiple=True  # Allow multiple column selections
        ), 
        ui.hr(),
        ui.hr(),
        ui.br(),
            ui.card(ui.h5(ui.markdown("""
            Dear User kindly note that you can select many
            variables or individual in the dropdown box on the above filter to plot the
            each variable and the Frequency Distribution"""),              
                ),
            ),
    )