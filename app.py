import os
import numpy as np
from shiny import App, Inputs, ui, reactive, render, module
from shinywidgets import render_plotly, output_widget

#import modeules
from modeules.user_stats import user_stats_ui, user_stats_server

#Defining Input Lists
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
)