import os
import pandas as pd
import numpy as np
from shiny import App, Inputs, ui, reactive, render, module
from shinywidgets import render_plotly, output_widget

#import modeules
from modeules.user_stats import user_stats_ui, user_stats_server

#Defining Input Lists
seasons = []
factions = []

#Loading Data (HARD-CODED FOR NOW)
data = pd.concat([
    pd.read_csv('data/M01.csv'),
    pd.read_csv('data/M02.csv')],ignore_index=True)

############################################################
############## UI # UI # UI ################################
############################################################

app_ui = ui.page_navbar(

    ############ USER STATS ###############
    ui.nav_panel('User Stats'
        user_stats_ui(
            data=data
        ))
)