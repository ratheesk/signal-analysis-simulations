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
    "text-align": "start",
    "padding": "10px",
    "borderRadius": "8px",
    "transition": "0.3s",
}

NAV_ITEMS = [
    ("Home", "/"),
    ("AM Modulation", "/am-modulation"),
    ("Modulation Effects", "/am-modulation-effect"),
    ("Frequency Spectrum", "/am-frequency-spectrum"),
]

# Sidebar component
SideBar = html.Div(
    [
        html.Div(
            [
                html.H3("📡 Signals Simulation", className="text-center"),
                html.Hr(style={"borderColor": "white"}),
                html.P("By Rathees", className="lead text-center"),
                
                dbc.Nav(
                    [dbc.NavLink(text, href=link, active="exact", style=NAV_LINK_STYLE) for text, link in NAV_ITEMS],
                    vertical=True,
                    pills=True,
                ),
                
                html.Br(),
                html.Div(
                    "⚡ Explore signal processing like never before!", 
                    className="text-center",
                    style={"fontSize": "14px", "opacity": "0.8"}
                ),
            ],
            style={"textAlign": "center"},
        )
    ],
    style=SIDEBAR_STYLE,
)