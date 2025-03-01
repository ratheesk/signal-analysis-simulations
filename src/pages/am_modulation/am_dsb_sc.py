import numpy as np
import plotly.graph_objs as go
from dash import html, dcc
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output

def AMDSBSCPage():

    # Return the chapter content along with the three plots and sliders
    return html.Div([
        html.H3("Double-Sideband Suppressed Carrier (DSB-SC)"),
        html.P("Mathematical expressions for the signals:"),
        
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

        html.P("Amplitude Modulated Signal (Derivation):"),
        dcc.Markdown(r"""
        $$
        \begin{aligned}
        s(t) &= [A_c + A_m \cos(2\pi f_m t)] \cos(2\pi f_c t) \\
        &= A_c \left[1 + \frac{A_m}{A_c} \cos(2\pi f_m t)\right] \cos(2\pi f_c t) \\
        &= A_c \left[1 + \mu \cos(2\pi f_m t)\right] \cos(2\pi f_c t) \\
        &= A_c \cos(2\pi f_c t) + A_c \mu \cos(2\pi f_m t) \cos(2\pi f_c t) \\
        &= A_c \cos(2\pi f_c t) + \frac{A_c \mu}{2} \left[ \cos(2\pi (f_c - f_m) t) + \cos(2\pi (f_c + f_m) t) \right]\\
        &= A_c \cos(2\pi f_c t) + \frac{A_c \mu}{2} \cos(2\pi (f_c - f_m) t) + \frac{A_c \mu}{2} \cos(2\pi (f_c + f_m) t)
        \end{aligned}
        $$
        """, mathjax=True, ),

        html.P("Where:"),
        dcc.Markdown(
            r"""
            $$ 
            \begin{aligned}
                A_c  &= \text{amplitude of the carrier wave} \\
                f_c  &= \text{frequency of the carrier wave} \\
                A_m  &= \text{amplitude of the modulating signal} \\
                f_m  &= \text{frequency of the modulating signal} \\
                \mu  &= \frac{A_m}{A_c} \quad \text{modulation index} \\
                s(t) &= \text{amplitude modulated signal} 
            \end{aligned}
            $$
            """,
            mathjax=True
        ),      
       

        # Plot for Carrier Wave
        html.Div([
            html.H4("Simulate AM Modulation"),
            html.H6("Carrier Signal Frequency"),
            dcc.Slider(
                id='carrier-frequency-slider',
                min=1,
                max=30,
                value=25, 
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            html.H6("Carrier Signal Amplitude"),
            dcc.Slider(
                id='carrier-amplitude-slider',
                min=1,
                max=10,
                value=8, 
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            html.H6("Modulating Signal Frequency"),
             dcc.Slider(
                id='modulating-frequency-slider',
                min=1,
                max=30,
                value=3,  
                tooltip={"placement": "bottom", "always_visible": True},
            ),
             html.H6("Modulating Signal Amplitude"),
            dcc.Slider(
                id='modulating-amplitude-slider',
                min=1,
                max=10,
                value=4, 
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            dcc.Graph(id='am-dsb-sc-signal-plot')
        ]),
    ])


def update_plot(carrier_f, modulating_f, modulating_a, carrier_a):
    t = np.linspace(0, 1, 1000) # Time variable

    # Modulating signal equation
    modulating_signal = modulating_a * np.cos(2 * np.pi * modulating_f * t)  

    # carrier wave signal
    carrier_wave = carrier_a * np.cos(2 * np.pi * carrier_f * t)

    # am signal
    am_signal = carrier_wave + (modulating_a/2) * np.cos(2 * np.pi * (modulating_f + carrier_f) * t) + (modulating_a/2) * np.cos(2 * np.pi * (carrier_f - modulating_f  ) * t)


    combined_plot = make_subplots(rows=3, cols=1, vertical_spacing=0.05)

    combined_plot.append_trace(go.Scatter(x=t, y=carrier_wave, mode='lines', name="Carrier Wave" ), row=1, col=1)
    combined_plot.append_trace(go.Scatter(x=t, y=modulating_signal, mode='lines',name="Modulating Signal" ), row=2, col=1)
    combined_plot.append_trace(go.Scatter(x=t, y=am_signal, mode='lines', name='AM Modulated Signal' ), row=3, col=1)

    combined_plot.update_yaxes(title_text="Amplitude", row=1, col=1)
    combined_plot.update_yaxes(title_text="Amplitude", row=2, col=1)
    combined_plot.update_yaxes(title_text="Amplitude", row=3, col=1)

 
    combined_plot.update_xaxes(title_text="Time (s)", row=3, col=1)

    combined_plot.update_layout(height=800, template="plotly_dark")


    return  combined_plot

def am_dsb_sc_callback(app):
    @app.callback(
        Output('am-dsb-sc-signal-plot', 'figure'),
        [Input('carrier-frequency-slider', 'value'),
        Input('carrier-amplitude-slider', 'value'),
        Input('modulating-frequency-slider', 'value'),
        Input('modulating-amplitude-slider', 'value')]
    )
    def update_output(carrier_f, carrier_a, modulating_f, modulating_a ):
        return update_plot(carrier_f, modulating_f, modulating_a, carrier_a)

