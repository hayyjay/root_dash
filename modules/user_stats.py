from shiny import ui, reactive, module

@module.ui
def user_stats_ui(data):

    return ui.sidebar(
        ui.input_select('select_season',
            label='Season',
            choices=['M03','M02','M01','All'],
            selected='M03'),
        ui.input_select('select_user',
            label='User',
            choices=[]),
        position='right',
        width=275
    )

@module.server
def user_stats_server(data):

    @reative.effect
    def update_user_list():
        ui.update_select('select_user',
            label='User',
            choices=data[].distinct())

    return input.select_season,\
        input.select_user