from dash import html
import dash_bootstrap_components as dbc

def Footer():
    """
    Creates a responsive footer with centered content.
    """
    return html.Footer(
        dbc.Container(
            [
                html.Hr(className="mt-0 mb-3 border-light opacity-25"),
                
                dbc.Row(
                    [
                        # Copyright text centered
                        dbc.Col(
                            html.P(
                                "© 2025 Signal Analysis Simulation. Licensed under MIT License.",
                                className="text-light opacity-75 small text-center mb-0"
                            ),
                            width=12,
                        ),
                        
                        # Social media icons centered
                        dbc.Col(
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
                            width=12,
                        ),
                    ],
                    className="pb-4 text-center"
                )
            ],
            fluid="md"
        ),
        className="footer mt-auto bg-dark"
    )
