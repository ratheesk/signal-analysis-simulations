from dash import html, dcc

def HomePage():
    return html.Div([
        html.H2("Welcome to Signal Analysis Simulation Platform"),

        html.P(
            "This platform allows you to visualize and analyze various signal processing "
            "concepts, including modulation, filtering, and Fourier transforms."
        ),

        html.H3("Features:"),
        html.Ul([
            html.Li("Amplitude and Frequency Modulation (AM & FM)"),
            html.Li("Custom Signal Generation and Analysis"),
            html.Li("Interactive Graphs and Real-time Plots")
        ]),

        html.H3("Get Started"),
        html.P(
            "Use the navigation menu to explore different modules and start analyzing signals. "
            "Select a feature from the sidebar to begin your simulation."
        ),

       
        html.Br(),

        html.Div(
            "Happy Analyzing!", 
            style={"textAlign": "center", "fontWeight": "bold", "fontSize": "18px"}
        )
    ])
