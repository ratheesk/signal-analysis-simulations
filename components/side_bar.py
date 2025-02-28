from dash import html
import dash_bootstrap_components as dbc

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

SideBar = html.Div([
     html.H3("Wave Modulation"),
        html.Hr(),
        html.P(
            "By Rathees", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("AM Modulation", href="/am-modulation", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),], style=SIDEBAR_STYLE,)