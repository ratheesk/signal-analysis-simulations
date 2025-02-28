import numpy as np
import plotly.graph_objs as go
from dash import html, dcc, Dash
from dash.dependencies import Input, Output

def AMFrequencySpectrumPage():
    return html.Div([
        html.H3("Frequency Spectrum of AM Wave"),
        
        html.P("The frequency spectrum of an AM wave consists of the carrier frequency and two sidebands."),
        dcc.Markdown(r"""
        $$
        S(f) = A_c \delta(f - f_c) + \frac{A_c \mu}{2} \delta(f - (f_c - f_m)) + \frac{A_c \mu}{2} \delta(f - (f_c + f_m))
        $$
        """, mathjax=True),
        
        html.Div([
            html.H4("Adjust Modulation Index"),
            dcc.Slider(
                id='modulation-index-slider',
                min=0.1,
                max=1.0,
                step=0.1,
                value=0.5, 
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            dcc.Graph(id='am-f-spectrum-plot')
        ]),
    ])

def update_spectrum_plot(modulation_index):
    carrier_f = 25
    modulating_f = 3
    carrier_a = 8
    modulating_a = carrier_a * modulation_index

    frequencies = [carrier_f - modulating_f, carrier_f, carrier_f + modulating_f]
    amplitudes = [modulating_a / 2, carrier_a, modulating_a / 2]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=frequencies, y=amplitudes, name='Frequency Spectrum'))
    fig.update_layout(title='Frequency Spectrum of AM Wave', xaxis_title='Frequency (Hz)', yaxis_title='Amplitude')
    
    return fig

def am_frequency_spectrum_callback(app):
    @app.callback(
        Output('am-f-spectrum-plot', 'figure'),
        [Input('modulation-index-slider', 'value')]
    )
    def update_output(modulation_index):
        return update_spectrum_plot(modulation_index)

