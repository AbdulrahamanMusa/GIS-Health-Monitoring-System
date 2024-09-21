from shiny import ui

def AppInfo():
    return ui.div(
    ui.accordion(
    ui.accordion_panel("Author",
        ui.tags.img( src="your_image.jpg", height="420px",
           style="float: right;"
            'border-radius: 15px;'),
            ui.div(
            ui.h5(
                ui.markdown(
                  """
                Hello everyone I am Abdulrahaman A Musa Passionate Data Scientist in the field of Artificial Intelligent (AI) Machine learning 
                and predictive modelling in the Academic, 
                Health and Humanitarian sectors
               
              Data is the new oil! Whether it comes from satellites, sensors, rivers or even our phones, it holds valuable insights. 
              Data from the spread of disease to the impacts of extreme weather, data about health and climate change surrounds us and 
              GIS allow us to know what is happening in our neighbourhood and what is happening in our community for effective decision-making

              ## Our areas of expertise include:
              -   Building R and Python Shiny Dashboard
              -   Business Analytics Dashboard (Power BI/Tableau)
              -   Training/Coaching on Data Analysis using the following
                  -   R and Python program
                  -   SPSS and Epi-Info software
              -   Building of Survey Platform
              -   Scripting and developing data collection tools
              -   Setting/Implementing of EHR in the private Health sector
              -   Monitoring and Evaluation of program/survey

                - For more information visit:https://am-datasolution.com/.
                - If you want to hire me for Full-Stack Data Science App contact me @ abdulrahaman@am-datasolution.com.
                                            """,)
    ),
    
    style='margin-right: 10px;''margin-top: 70px;' 'margin-bottom: 10px;'
            "background-color: white"                      
    ), 
  ),
    open=True 
  ),        
   
 )
    
def WorkInfo():
    return ui.div(
    ui.accordion(
    ui.accordion_panel("How does it Work?",
              ui.layout_columns(
            ui.div(
            ui.h5(
                ui.markdown(
                    """                
                #### Interactive Mapping: 
                Our intuitive map interface empowers stakeholders to visualize the locations of healthcare facilities, each marked with a health score. This bird's-eye view highlights areas in need of improvement, enabling targeted resource allocation and strategic decision-making.
                #### Data-Driven Insights: 
                We seamlessly integrate survey data from KoboToolbox, storing it securely in a SQL database. Our system then cleans and analyzes this data, presenting it in easy-to-understand plots and frequency distributions. This empowers managers and decision-makers to quickly grasp key trends and make informed decisions based on real-world evidence.
                #### User-Friendly Navigation: 
                Our landing page provides a clear overview of the app's capabilities, ensuring a smooth and intuitive user experience. The hamburger menu, with its dynamic scrolling banner, allows for effortless navigation between tabs, putting the power of data at your fingertips.

            
                #### Acknowledgements
                I am extend my sincere gratitude to: 
                - Posit for developing Shiny for Python, 
                - Appsilon for  shiny_semantic and 
                - eHealth Africa for providing insightful learning materials/data that supported this project.
                                            """,)
    ),
    
    style='margin-right: 10px;''margin-top: 70px;' 'margin-bottom: 10px;'
            "background-color: white"                      
    ),
    ui.div(
        ui.HTML("""
                Your Youtube challen
        """),
      ),     
    ), 
  ),
    open=True
  ),        
    
 )
    
    
def model_infor_pop():
      mod = ui.modal(
            ui.card(
            ui.row(
                ui.layout_columns(
                   ui.h4(
                        ui.layout_columns(
                        ui.card(
                         ui.img(src="images/Amusa.png", style="width: 120px; display: left; margin: 0 auto;",),
                         ui.h6(ui.markdown("""
                               Data is the new oil! Whether it comes from satellites, sensors, rivers or even our phones, it holds valuable insights. 
                               Data from the spread of disease to the impacts of extreme weather, data about health and climate change surrounds us and 
                               GIS allow us to know what is happening in our neighbourhood and what is happening in our community for effective decision-making
                               """)),
                        )),
                         ui.hr(),
                         ui.h6(ui.markdown("""Hello everyone I am Abdulraham A Musa Passionate Data/ML Scientist in the field of Artificial Intelligent (AI) Machine learning and predictive modelling in the Academic, Health and Humanitarian sectors
                        For more information visit:https://am-datasolution.com/.
                    
                     """),
                         ui.hr(),
                         ui.a("github-link", href="https://github.com/AbdulrahamanMusa",class_="docs-link",)),
                         
                    ),
                ),
            ),
        ),
        title=ui.span("GIS-Health-System:", style="color: #486590; font-size: 2rem;"),
        easy_close=True,
        footer=None,
    )
      return ui.modal_show(mod) 
    