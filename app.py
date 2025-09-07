#import packages
import pandas as pd
import numpy as np
from shiny import App, Inputs, ui, reactive, render, module
from shinywidgets import render_plotly, output_widget
from shinyswatch import theme

#import modules
from modules.user_stats import user_stats_ui, user_stats_server

#Loading Data (HARDCODED)
data = pd.concat([
    pd.read_csv('data/M01.csv'),
    pd.read_csv('data/M02.csv')],ignore_index=True)

#Defining Input Lists (HARDCODED)
seasons = []
factions = []

############################################################
############## UI # UI # UI ################################
############################################################

app_ui = ui.page_navbar(

    ############ USER STATS ###############
    ui.nav_panel('User Stats'
        user_stats_ui(
            data=data
        ))
    ############ PAGE PLACEHOLDER #########

    ############ TITLE & THEME ############
    window_title='Root Digital League Dashboard',
    id='tab',
    theme=theme.superhero(),

)

############################################################
############## SERVER # SERVER # SERVER ####################
############################################################

def server(input, output, session):
    
    ############ USER STATS ###############
    user_stats_server(
        'user_stats',
        data=data
    )

    ############ PAGE PLACEHOLDER #########

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()