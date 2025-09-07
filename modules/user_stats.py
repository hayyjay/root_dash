@module.ui
def user_stats_ui(data):

    return ui.layout_sidebar(
        ui.sidebar(
            ui.input_select('select_season',
                label='Season',
                choices=['M03','M02','M01','All'],
                selected='M03'),
            ui.input_select('select_user',
                label='User',
                choices=[]),
            position='right',
            width=275
        ),
        ui.card(
            ui.card_header(
                ui.h4("User Stats"),
                class_="d-flex align-tiems-center gap-3"
            ),
            output_widget('graph_user_stats'),
            full_screen_True,
            height=600
        )
    )

@module.server
def user_stats_server(input, output, session, data):

    season = input.select_season 
    user = input.select_user

    @reactive.calc
    def data_user_stats():
        df = []
        return data

    @render_plotly
    def graph_user_stats():
        if data_user_stats() is None:
            return None
        else:
            graph = []
            return graph    