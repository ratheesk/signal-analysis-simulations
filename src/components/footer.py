# components/footer.py
from dash import html
import dash_bootstrap_components as dbc

def Footer():
    """
    Creates a responsive footer with multiple sections
    """
    return html.Footer(
        dbc.Container(
            [                # Copyright row
                html.Hr(className="mt-0 mb-3 border-light opacity-25"),
                dbc.Row(
                    [
                        dbc.Col(
                            html.P(
                                "© 2025 Signal Analysis Platform. All rights reserved.",
                                className="text-light opacity-75 small text-center text-lg-start mb-0"
                            ),
                            width=12, lg=6,
                            className="mb-3 mb-lg-0"
                        ),
                        dbc.Col(
                            html.Div(
                                    [
                                        html.A(
                                            html.I(className="fab fa-github fa-lg"),
                                            href="https://github.com/ratheesk/signal-analysis-simulations",
                                            className="text-white me-3",
                                        ),
                                        html.A(
                                            html.I(className="fab fa-linkedin fa-lg"),
                                            href="https://www.linkedin.com/in/ratheesk/",
                                            className="text-white me-3",
                                        ),
                                    ],
                                    className="mt-3"
                                ),
                            width=12, lg=6
                        ),
                    ],
                    className="pb-4"
                )
            ],
            fluid="md"
        ),
        className="footer mt-auto bg-dark"
    )