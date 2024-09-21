from htmltools import div, tags
# from tensorflow.keras.models import load_model
from shiny.ui import output_text, tags
from datetime import datetime
from typing import Any, Awaitable
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
import pandas as pd
from shiny import *
import numpy as np
from pathlib import Path



#
@module.ui
def UImap():
    return feature_section(("Live-Map"),
        ui.strong(ui.h6(ui.HTML("""
                                 To Interact with the Map dynamicaly please go to Map section you can also select/unselect multiple states, also you can view the Map in full screen mode    
                                  """))),
        ui.br(),
        div(
            tags.div(
                
                tags.span(ui.img(src="static/img/mapgis.png", width="95%", height="85%")),
            )
        )
)



@module.server
def server(input: Inputs, output: Outputs, session: Session):
  pass