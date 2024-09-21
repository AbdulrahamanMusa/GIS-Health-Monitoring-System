from __future__ import annotations
from pathlib import Path
# import chatstream
# import shiny.experimental as x
from htmltools import TagList, div, tags
from htmltools import TagList, div, tags
from shiny import *
from shiny_semantic import page_semantic
# import shinyswatch
from shiny.ui import output_text, tags
import os
# from dotenv import load_dotenv
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
# load_dotenv()

@module.ui
def Home():
    return feature_section(("Map"),
        ui.strong(ui.h6(ui.HTML("""<marquee>
                                 Map Showing Health Care Faciltity with Higher Score From Sokoto, Kano and Kaduna
                                  </marquee>"""))),
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
                animation: imageSlide 180s linear infinite; /* Total animation time: 60s * 3 images */
                }
                .marquee span:nth-child(1) { animation-delay: 0s; }  /* Image 1 starts immediately */
                .marquee span:nth-child(2) { animation-delay: 60s; } /* Image 2 starts after 60s */
                .marquee span:nth-child(3) { animation-delay: 120s; }/* Image 3 starts after 120s */
                @keyframes imageSlide {
                0% {
                    opacity: 1;
                    transform: translateX(0);
                }
                33.33% { /* Hold for 60 seconds (60s / 180s * 100%) */
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
                
                tags.span(ui.img(src="static/img/SokotoHF.png", width="95%", height="85%")),
                tags.span(ui.img(src="static/img/KanoHF.png", width="95%", height="85%")),
                tags.span(ui.img(src="static/img/Kaduna.png", width="95%", height="85%")),
                class_="marquee"
            )
        )
)



@module.server
def server(input: Inputs, output: Outputs, session: Session):
  pass
 








