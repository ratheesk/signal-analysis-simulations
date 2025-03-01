import numpy as np
import plotly.graph_objs as go
from dash import html, dcc
from dash.dependencies import Input, Output

def AMModulationEffectsPage():
    return html.Div([
        html.H3("Modulation Effect"),
        
        html.P("Amplitude Modulated Signal:"),
        dcc.Markdown(r"""
        $$
        s(t) = A_c \cos(2\pi f_c t) + \frac{A_c \mu}{2} \cos(2\pi (f_c - f_m) t) + \frac{A_c \mu}{2} \cos(2\pi (f_c + f_m) t)
        $$
        """, mathjax=True),

        html.P("Modulation Index:"),
        dcc.Markdown(r"""
        $$ 
        \mu  = \frac{A_m}{A_c}
        $$
        """, mathjax=True),

        html.P("Envelope of the AM Wave:"),
        dcc.Markdown(r"""
        $$
        E_{upper}(t) = A_c (1 + \mu \cos(2\pi f_m t))
        $$
        """, mathjax=True),
        dcc.Markdown(r"""
        $$
        E_{lower}(t) = -A_c (1 + \mu \cos(2\pi f_m t))
        $$
        """, mathjax=True),

        html.Div([
            html.H4("Simulate Effect of Modulation Index"),
            dcc.Slider(
                id='modulation-index-slider',
                min=0.1,
                max=2.0,
                step=0.1,
                value=0.5, 
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            dcc.Graph(id='modulation-effect-plot')
        ]),
    ])

def update_plot(modulation_index):
    t = np.linspace(0, 1, 1000)  # Time variable
    modulating_f = 3             # Modulating signal frequency
    carrier_f = 25               # Carrier frequency
    carrier_a = 8                # Carrier amplitude
    modulating_a = 3

        # Modulating signal equation
    modulating_signal = modulating_a * np.cos(2 * np.pi * modulating_f * t)  

    # carrier wave signal
    carrier_wave = carrier_a * np.cos(2 * np.pi * carrier_f * t)

    # amplitude sensitivity
    amp_sens = 0.3


    # AM signal using cosines
    # am_signal = (carrier_a * np.cos(2 * np.pi * carrier_f * t) +
    #              (modulating_a / 2) * np.cos(2 * np.pi * (modulating_f + carrier_f) * t) +
    #              (modulating_a / 2) * np.cos(2 * np.pi * (carrier_f - modulating_f) * t))
    am_signal = (1 + amp_sens * modulating_signal) * carrier_wave
    
    # Envelope
    envelope_upper = carrier_a * (1 + modulation_index * np.cos(2 * np.pi * modulating_f * t))
    envelope_lower = -carrier_a * (1 + modulation_index * np.cos(2 * np.pi * modulating_f * t))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=am_signal, mode='lines', name='AM Modulated Signal'))
    fig.add_trace(go.Scatter(x=t, y=envelope_upper, mode='lines', name='Upper Envelope', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=t, y=envelope_lower, mode='lines', name='Lower Envelope', line=dict(dash='dash')))
    fig.update_layout(title='AM Modulation Effect', xaxis_title='Time (s)', yaxis_title='Amplitude', height=500, template="plotly_dark")
    return fig

def am_modulation_effects_callback(app):
    @app.callback(
        Output('modulation-effect-plot', 'figure'),
        [Input('modulation-index-slider', 'value')]
    )
    def update_output(modulation_index):
        return update_plot(modulation_index)

