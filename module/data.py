from htmltools import div, tags
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
from shiny.types import FileInfo

@module.ui
def UIdata():
    return feature_section(("Data Pipe Line"),
        ui.strong(ui.h6(ui.HTML("""
                                 Flow of data from its source in KoboToolbox to its final presentation in the user interface
                                  """))),
        ui.br(),
       tags.style(
            """
                .marquee {
                width: 100%;
                height: 600px; /* Adjust height as needed */
                overflow: hidden;
                }
                .marquee span {
                position: absolute;
                width: 100%;
                height: 90%;
                display: block;
                opacity: 0; /* Initially hide all images */
                animation: imageSlide 80s linear infinite; /* Total animation time: 10s * 3 images */
                }
                .marquee span:nth-child(1) { animation-delay: 0s; }  /* Image 1 starts immediately */
                .marquee span:nth-child(2) { animation-delay: 30s; } /* Image 2 starts after 60s */
                @keyframes imageSlide {
                0% {
                    opacity: 1;
                    transform: translateX(0);
                }
                33.33% { /* Hold for 60 seconds (30s / 80s * 100%) */
                    opacity: 1;
                    transform: translateX(0); 
                }
                100% {
                    opacity: 0;
                    transform: translateX(-100%);
                }
                }   
                """
        ),
        div(
            tags.div(
                
                tags.span(ui.img(src="static/img/dataflowAPI.png", width="95%", height="85%")),
                tags.span(ui.img(src="static/img/kobodata.png", width="95%", height="85%")),
                class_="marquee"
            )
        )
)



@module.server
def server(input: Inputs, output: Outputs, session: Session):
  pass
 