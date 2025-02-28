from dash import html
import dash_bootstrap_components as dbc

# Sidebar styling
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "1.5rem",
    "background-color": "#343a40",  # Dark theme
    "color": "white",
    "boxShadow": "2px 0px 5px rgba(0,0,0,0.1)",
}

NAV_LINK_STYLE = {
    "color": "white",
    "fontSize": "14px",
    "text-align":'start',
    "padding": "10px",
    "borderRadius": "8px",
    "transition": "0.3s",
}

NAV_LINK_HOVER = {
    "color": "white",
    "backgroundColor": "#495057",
}

# Sidebar component
SideBar = html.Div([
    html.Div([
        html.H3("📡 Signals Simulation", className="text-center"),
        html.Hr(style={"borderColor": "white"}),

        html.P("By Rathees", className="lead text-center"),

        dbc.Nav(
            [
                dbc.NavLink("Home",
                    href="/", active="exact", style=NAV_LINK_STYLE
                ),
                dbc.NavLink("AM Modulation", 
                    href="/am-modulation", active="exact", style=NAV_LINK_STYLE
                ),
                dbc.NavLink("Modulation Effects", 
                    href="/am-modulation-effect", active="exact", style=NAV_LINK_STYLE
                ),
                dbc.NavLink("Frequency Spectrum", 
                    href="/am-frequency-spectrum", active="exact", style=NAV_LINK_STYLE
                ),
            ],
            vertical=True,
            pills=True,
        ),

        html.Br(),

        html.Div(
            "⚡ Explore signal processing like never before!", 
            className="text-center",
            style={"fontSize": "14px", "opacity": "0.8"}
        )
    ], style={"textAlign": "center"})
], style=SIDEBAR_STYLE)
