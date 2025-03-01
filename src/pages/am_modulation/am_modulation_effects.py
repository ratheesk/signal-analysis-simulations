import numpy as np
import plotly.graph_objs as go
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


def AMModulationEffectsPage():
    return html.Div([
        html.H3("Modulation Effect"),

        html.P("Carrier Wave:"),
        dcc.Markdown(r"""
        $$
        c(t) = A_c \cos(2\pi f_c t)
        $$
        """, mathjax=True),

        html.P("Modulating Signal:"),
        dcc.Markdown(r"""
        $$
        m(t) = A_m \cos(2\pi f_m t)
        $$
        """, mathjax=True),
        
        html.P("Amplitude Modulated Signal:"),
        dcc.Markdown(r"""
        $$
        s(t) = A_c \cos(2\pi f_c t) + \frac{A_c k_a A_m}{2} \cos(2\pi (f_c - f_m) t) + \frac{A_c k_a A_m}{2} \cos(2\pi (f_c + f_m) t)
        $$
        """, mathjax=True),
        html.P("Modulation Percentage:"),

       dcc.Markdown(r"""
        $$ 
        \text{Modulation Percentage} = \max (\left| k_a m(t) \right|) \times 100\%
        $$
        """, mathjax=True), 

        html.P("Envelope of the AM Wave:"),
        dcc.Markdown(r"""
        $$
        E_{upper}(t) = A_c (1 + k_a A_m \cos(2\pi f_m t))
        $$
        """, mathjax=True),
        dcc.Markdown(r"""
        $$
        E_{lower}(t) = -A_c (1 + k_a A_m \cos(2\pi f_m t))
        $$
        """, mathjax=True),

        html.H4("Adjust Modulation Percentage (0% - 200%)"),


        dbc.Card([
            html.H6("Modulation Percentage"),
            dcc.Slider(
                id='modulation-index-slider',
                min=0,  # Corresponds to 0% modulation
                max=2,  # Corresponds to 200% modulation
                value=0.5,  # Default is 50% modulation
                marks={i: f"{int(i*100)}%" for i in np.linspace(0, 2, 5)},  # 0%, 50%, 100%, 150%, 200%
            ),
            dcc.Graph(id='modulation-effect-plot')
        ],  className='p-3 mt-3'),
    ])

def update_plot(modulation_index):
    t = np.linspace(0, 1, 1000)  # Time variable
    modulating_f = 3             # Modulating signal frequency
    carrier_f = 25               # Carrier frequency
    carrier_a = 8                # Carrier amplitude
    modulating_a = 3

    # Modulating signal equation
    modulating_signal = modulating_a * np.cos(2 * np.pi * modulating_f * t)  

    # Carrier wave signal
    carrier_wave = carrier_a * np.cos(2 * np.pi * carrier_f * t)

    # AM signal with user-defined modulation index
    am_signal = (1 + modulation_index * modulating_signal / modulating_a) * carrier_wave
    
    # Envelope
    envelope_upper = carrier_a * (1 + (modulation_index * modulating_signal / modulating_a))
    envelope_lower = -carrier_a * (1 + (modulation_index * modulating_signal / modulating_a))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=am_signal, mode='lines', name='AM Modulated Signal'))
    fig.add_trace(go.Scatter(x=t, y=envelope_upper, mode='lines', name='Upper Envelope', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=t, y=envelope_lower, mode='lines', name='Lower Envelope', line=dict(dash='dash')))
    fig.update_layout(title=f'AM Modulation Effect ({modulation_index*100:.0f}%)',
                      xaxis_title='Time (s)', 
                      yaxis_title='Amplitude', 
                      height=500, 
                      template="plotly_dark")
    return fig

def am_modulation_effects_callback(app):
    @app.callback(
        Output('modulation-effect-plot', 'figure'),
        [Input('modulation-index-slider', 'value')]
    )
    def update_output(modulation_index):
        return update_plot(modulation_index)
