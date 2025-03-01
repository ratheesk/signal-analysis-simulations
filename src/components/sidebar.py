# components/sidebar.py
from dash import html, dcc
import dash_bootstrap_components as dbc

# Colors and theme variables
SIDEBAR_BG = "#1e2a3a"
SIDEBAR_TEXT = "#ffffff"
ACCENT_COLOR = "#3498db"
HOVER_COLOR = "#2980b9"
SUBMENU_BG = "#2c3e50"

# Sidebar styling - made responsive
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "250px",
    "padding": "2rem 1rem",
    "paddingTop": "4.5rem",  # Additional padding for navbar
    "backgroundColor": SIDEBAR_BG,
    "color": SIDEBAR_TEXT,
    "boxShadow": "2px 0px 10px rgba(0,0,0,0.2)",
    "transition": "all 0.3s ease-in-out",
    "zIndex": 999,  # Just below navbar
    "overflowY": "auto",
}

# Content style when sidebar is expanded
CONTENT_STYLE = {
    "marginLeft": "250px",
    "padding": "2rem",
    "transition": "all 0.3s ease-in-out",
}

# Content style when sidebar is collapsed
CONTENT_COLLAPSED = {
    "marginLeft": "0px",
    "padding": "2rem",
    "transition": "all 0.3s ease-in-out",
}

# Style for navigation links
NAV_LINK_STYLE = {
    "color": SIDEBAR_TEXT,
    "fontSize": "15px",
    "padding": "10px 15px",
    "borderRadius": "8px",
    "transition": "all 0.2s",
    "margin": "4px 0",
    "display": "flex",
    "alignItems": "center",
    "justifyContent": "space-between",
}

# Navigation structure with multilevel items
NAV_ITEMS = [
    {"label": "Home", "href": "/", "icon": "fas fa-home"},
    {
        "label": "AM Modulation",
        "icon": "fas fa-broadcast-tower",
        "children": [
            {"label": "Overview", "href": "/am-modulation"},
            {"label": "Modulation Effects", "href": "/am-modulation-effect"},
            {"label": "Frequency Spectrum", "href": "/am-frequency-spectrum"},
            {"label": "DSB-SC", "href": "/am-double-sideband-suppressed-carrier"},
        ]
    },
    
    {
        "label": "FM Modulation",
        "icon": "fas fa-wave-square",
        "children": [
            {"label": "Overview", "href": "/fm-modulation"},
            {"label": "Frequency Deviation", "href": "/fm-frequency-deviation"},
            {"label": "Spectrum Analysis", "href": "/fm-spectrum-analysis"},
        ]
    },
    {"label": "Documentation", "href": "/docs", "icon": "fas fa-book"},
]

# Function to create a navigation item
def create_nav_item(item):
    # If the item has children, create a collapsible section
    if "children" in item:
        return html.Div([
            dbc.Button(
                [
                    html.I(className=f"{item['icon']} me-2"),
                    html.Span(item["label"]),
                    html.I(className="fas fa-chevron-down ms-auto")
                ],
                id=f"group-{item['label'].lower().replace(' ', '-')}",
                className="sidebar-btn",
                style={
                    **NAV_LINK_STYLE,
                },
                n_clicks=0,
                outline=True,
            ),
            dbc.Collapse(
                [
                    dbc.NavLink(
                        [
                            html.Span(child["label"]),
                        ],
                        href=child["href"],
                        active="exact",
                        style={
                            **NAV_LINK_STYLE,
                            "paddingLeft": "35px",
                            "fontSize": "14px",
                        },
                        className="sidebar-sublink",
                    )
                    for child in item["children"]
                ],
                id=f"collapse-{item['label'].lower().replace(' ', '-')}",
                is_open=False,
                style={"backgroundColor": SUBMENU_BG, "borderRadius": "5px"}
            ),
        ])
    else:
        # For regular items without children
        return dbc.NavLink(
            [
                html.I(className=f"{item['icon']} me-2"),
                html.Span(item["label"]),
            ],
            href=item["href"],
            active="exact",
            style=NAV_LINK_STYLE,
            className="sidebar-link",
        )

# Create the sidebar component
def Sidebar():
    return html.Div(
        [
            # Navigation menu
            html.Div(
                [create_nav_item(item) for item in NAV_ITEMS],
                className="sidebar-nav"
            ),
            
            # Footer section within sidebar
            html.Div(
                [
                    html.Hr(style={"borderColor": "rgba(255,255,255,0.1)", "margin": "20px 0"}),
                    html.P(
                        "⚡ Explore signal processing like never before!",
                        style={"fontSize": "13px", "opacity": "0.8", "textAlign": "center"}
                    ),
                     html.Div(
                                [
                                    html.A(
                                        html.I(className="fab fa-github fa-lg"),
                                        href="https://github.com/ratheesk/signal-analysis-simulations",
                                        className="text-white mx-2",
                                    ),
                                    html.A(
                                        html.I(className="fab fa-linkedin fa-lg"),
                                        href="https://www.linkedin.com/in/ratheesk/",
                                        className="text-white mx-2",
                                    ),
                                ],
                                className="d-flex justify-content-center mt-2"
                            ),
                ],
                style={"marginTop": "auto"}
            )
        ],
        id="sidebar",
        style=SIDEBAR_STYLE,
        className="sidebar"
    )