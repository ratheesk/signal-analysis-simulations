# components/navbar.py
from dash import html
import dash_bootstrap_components as dbc

def NavBar():
    """
    Creates a responsive navbar with sidebar toggle button
    """
    return html.Nav(
        dbc.Navbar(
            dbc.Container(
                [
                    # Left side of navbar with toggle button and brand
                    html.Div(
                        [
                            # Sidebar toggle button
                            html.Button(
                                html.I(className="fas fa-bars"),
                                id="navbar-toggle-btn",
                                className="navbar-toggle-btn btn btn-link text-white me-3",
                                style={
                                    "fontSize": "20px", 
                                    "background": "none", 
                                    "border": "none",
                                    "padding": "0.25rem 0.75rem",
                                    "marginLeft": "-10px"
                                }
                            ),
                            
                            # App brand/logo
                            html.A(
                                [
                                    html.I(className="fas fa-broadcast-tower me-2", 
                                           style={"fontSize": "20px"}),
                                    "Signal Analysis Simulation"
                                ],
                                href="/",
                                className="navbar-brand d-flex align-items-center",
                                style={"color": "white", "fontWeight": "500"}
                            ),
                        ],
                        className="d-flex align-items-center"
                    ),
                  
                ]
            ),
            color="#1e2a3a",
            dark=True,
            fixed="top",
            className="py-2"
        ),
        className="navbar-container"
    )