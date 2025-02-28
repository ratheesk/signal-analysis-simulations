# app.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from components.side_bar import SideBar
from pages.am_modulation import AMModulationPage, update_plot 
from pages.home import HomePage
from pages.am_modulation_effects import am_modulation_effects_callback, AMModulationEffectsPage
from pages.am_frequncy_spectrum import AMFrequencySpectrumPage, am_frequency_spectrum_callback

# Initialize the Dash app
app = dash.Dash(__name__, 
                suppress_callback_exceptions=True, 
                external_stylesheets=[dbc.themes.BOOTSTRAP],  
                meta_tags=[
                    {"name": "description", "content": "An interactive platform for signal analysis and simulation."},
                    {"name": "keywords", "content": "Signal Processing, Modulation, Fourier Transform, Dash, Python"},
                    {"name": "author", "content": "Rathees Koneswaran"}
                 ])
app.title = "Signal Analysis Simulation Platform"


# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1.2rem",
}


content = html.Div(id="content", style=CONTENT_STYLE)

# Layout for the app
app.layout = html.Div([
    # URL routing system
    dcc.Location(id='url', refresh=False), SideBar, content
], className='wrapper')

# Routing for pages
@app.callback(
    Output('content', 'children'),
    Input('url', 'pathname')
)

def display_page(pathname):
    if pathname == '/':
        return HomePage()
    elif pathname == '/am-modulation':
        return AMModulationPage()  
    elif pathname == '/am-modulation-effect':
        return AMModulationEffectsPage()  
    elif pathname == '/am-frequency-spectrum':
        return AMFrequencySpectrumPage()  
    else:
        return html.Div([html.H2("Page not found")])

# Update the output graphs when sliders are changed
@app.callback(
    Output('combined-signal-plot', 'figure'),
    [Input('carrier-frequency-slider', 'value'),
     Input('carrier-amplitude-slider', 'value'),
     Input('modulating-frequency-slider', 'value'),
     Input('modulating-amplitude-slider', 'value')]
)
def update_output(carrier_f, carrier_a, modulating_f, modulating_a ):
    return update_plot(carrier_f, modulating_f, modulating_a, carrier_a)

am_modulation_effects_callback(app)
am_frequency_spectrum_callback(app)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
