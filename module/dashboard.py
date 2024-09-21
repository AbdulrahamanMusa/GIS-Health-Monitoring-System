from datetime import date

import pandas as pd  # pip install pandas

from htmltools import div, tags
from shiny import *
from shiny.ui import output_text, tags
from shiny_semantic import page_semantic
from shiny_semantic.elements import (
    button,
    header,
    icon,
    segment,
    semantic_input,
    subheader,
)
from shiny_semantic.elements import (
    button,
    header,
    icon,
    segment,
    semantic_input,
    subheader,
    container,
)
from ._feature_layout import feature_section, feature_subsection

#
@module.ui
def UI():
    return feature_section(("Data-Analysis"),
        ui.strong(ui.h6(ui.HTML("""
                                 To see how this Plots and Table display dynamicaly please go to Data-Analysis section under Data explorer Tab and select the varaible in the filter
                                  """))),
        ui.br(),
        div(
            tags.div(
                
                tags.span(ui.img(src="static/img/dataexplor.png", width="95%", height="85%")),
            )
        )
)



@module.server
def server(input: Inputs, output: Outputs, session: Session):
  pass
 
