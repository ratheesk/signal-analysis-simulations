# app.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# Import the new sidebar component
from components import  CONTENT_STYLE, Sidebar, NavBar, Footer

# Import pages
from pages import HomePage
from pages.am_modulation import (
    AMFrequencySpectrumPage, 
    AMModulationEffectsPage, 
    AMModulationPage,
    AMDSBSCPage, 
    am_frequency_spectrum_callback, 
    am_modulation_effects_callback, 
    am_modulation_callback,
    am_dsb_sc_callback

)

# Initialize the Dash app with Font Awesome for icons
app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://use.fontawesome.com/releases/v5.15.4/css/all.css"  # Font Awesome for icons
    ],  
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},  # Add responsive viewport
        {"name": "description", "content": "An interactive platform for signal analysis and simulation."},
        {"name": "keywords", "content": "Signal Processing, Modulation, Fourier Transform, Dash, Python"},
        {"name": "author", "content": "Rathees Koneswaran"}
    ]
)
app.title = "Signal Analysis Simulation Platform"

# Create the content div with adjusted top padding for navbar
content_style = CONTENT_STYLE.copy()
content_style["paddingTop"] = "4.5rem"  # Add padding for navbar
content = html.Div(id="page-content", style=content_style)

# Add CSS for additional styling

# Layout for the app
app.layout = html.Div([
    
    # URL routing system
    dcc.Location(id='url', refresh=False),
    
    # Main container
    html.Div([
        # Navbar at the top
        NavBar(),
        
        # Content container with sidebar and main content
        html.Div([
            # Sidebar
            Sidebar(),
            
            # Main content
            content
        ], className="content-container"),
        
        # Footer at the bottom
        Footer()
    ], className="main-container"),
    
    # Store to track sidebar state (expanded/collapsed)
    dcc.Store(id='sidebar-state', data={'collapsed': False}),
    
    # Include clientside JS
    html.Div(id='clientside-script-output')
], className='wrapper')

# Register the clientside JavaScript for sidebar toggle
app.clientside_callback(
    """
    function(n_clicks, data) {
        if (!data) {
            data = {collapsed: false};
        }
        
        const sidebar = document.getElementById('sidebar');
        
        if (n_clicks) {
            data.collapsed = !data.collapsed;
            
            if (data.collapsed) {
                sidebar.style.left = '-250px';
            } else {
                sidebar.style.left = '0px';
            }
        }
        
        // Handle initial state for responsive layouts
        const mediaQuery = window.matchMedia('(max-width: 768px)');
        if (mediaQuery.matches && !n_clicks) {
            sidebar.style.left = '-250px';
            data.collapsed = true;
        }
        
        return data;
    }
    """,
    Output('sidebar-state', 'data'),
    Input('navbar-toggle-btn', 'n_clicks'),
    State('sidebar-state', 'data')
)

# Update content margin based on sidebar state
app.clientside_callback(
    """
    function(data) {
        if (!data) {
            data = {collapsed: false};
        }
        
        const style = {
            transition: "margin-left 0.3s ease-in-out",
            padding: "2rem",
            paddingTop: "4.5rem"  // Account for navbar
        };
        
        if (data.collapsed) {
            style.marginLeft = "0px";
        } else {
            style.marginLeft = "250px";
        }
        
        // Handle responsive layout
        const mediaQuery = window.matchMedia('(max-width: 768px)');
        if (mediaQuery.matches) {
            style.marginLeft = "0px";
        }
        
        return style;
    }
    """,
    Output('page-content', 'style'),
    Input('sidebar-state', 'data')
)

# Routing for pages
@app.callback(
    Output('page-content', 'children'),
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
    elif pathname == '/am-double-sideband-suppressed-carrier':
        return AMDSBSCPage()  
    else:
        return html.Div([html.H2("Page not found")])

# Create callbacks for collapsible menu items
for item in ['am-modulation', 'fm-modulation']:
    @app.callback(
        Output(f'collapse-{item}', 'is_open'),
        Input(f'group-{item}', 'n_clicks'),
        State(f'collapse-{item}', 'is_open')
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open
        return is_open

# Update the output graphs when sliders are changed
am_modulation_callback(app)
am_modulation_effects_callback(app)
am_frequency_spectrum_callback(app)
am_dsb_sc_callback(app)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)