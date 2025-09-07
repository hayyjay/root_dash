#import packages
import pandas as pd
import numpy as np
from shiny import App, Inputs, ui, reactive, render, module
#from shinywidgets import render_plotly, output_widget

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
)

############################################################
############## SERVER # SERVER # SERVER ####################
############################################################

def server(input, output, session):
    
    ############ USER STATS ###############
    user_stats_server