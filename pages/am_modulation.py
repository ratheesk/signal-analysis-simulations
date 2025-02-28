import numpy as np
import plotly.graph_objs as go
from dash import html, dcc
from plotly.subplots import make_subplots

def AMModulationPage():
    # Generate data for the modulating signal (low frequency)
    t = np.linspace(0, 1, 1000) # Time variable
    modulating_f = 3  # Default Modulating signal frequency
    modulating_a = 4
    carrier_f = 25
    carrier_a = 8

    modulating_signal = modulating_a * np.sin(2 * np.pi * modulating_f * t)  # Modulating signal equation

    # carrier wave signal
    carrier_wave = carrier_a * np.sin(2 * np.pi * carrier_f * t)

    # am signal
    am_signal = carrier_wave + (modulating_a/2) * np.cos(2 * np.pi * (modulating_f + carrier_f) * t) - (modulating_a/2) * np.cos(2 * np.pi * (carrier_f - modulating_f  ) * t)

    combined_plot = make_subplots(rows=3, cols=1, subplot_titles=("Carrier Wave", "Modulating Signal", "AM Modulated Signal"))

    combined_plot.append_trace(go.Scatter(x=t, y=carrier_wave, mode='lines', ), row=1, col=1)
    combined_plot.append_trace(go.Scatter(x=t, y=modulating_signal, mode='lines', ), row=2, col=1)
    combined_plot.append_trace(go.Scatter(x=t, y=am_signal, mode='lines', ), row=3, col=1)

    combined_plot.update_layout(height=800)

    # Return the chapter content along with the three plots and sliders
    return html.Div([
        html.H3("Amplitude Modulation"),
        html.P("Mathematical expressions for the signals:"),
        
           html.P("Carrier Wave:"),
        dcc.Markdown(r"""
        $$
        c(t) = A_c \sin(2\pi f_c t)
        $$
        """, mathjax=True),

        html.P("Modulating Signal:"),
        dcc.Markdown(r"""
        $$
        m(t) = A_m \sin(2\pi f_m t)
        $$
        """, mathjax=True),

        html.P("Amplitude Modulated Signal (Derivation):"),
        dcc.Markdown(r"""
        $$
        \begin{aligned}
        s(t) &= [A_c + A_m \sin(2\pi f_m t)] \sin(2\pi f_c t) \\
        &= A_c \left[1 + \frac{A_m}{A_c} \sin(2\pi f_m t)\right] \sin(2\pi f_c t) \\
        &= A_c \left[1 + \mu \sin(2\pi f_m t)\right] \sin(2\pi f_c t) \\
        &= A_c \sin(2\pi f_c t) + A_c \mu \sin(2\pi f_m t) \sin(2\pi f_c t) \\
        &= A_c \sin(2\pi f_c t) + \frac{A_c \mu}{2} \left[ \cos(2\pi (f_c - f_m) t) - \cos(2\pi (f_c + f_m) t) \right]\\
        &= A_c \sin(2\pi f_c t) + \frac{A_c \mu}{2} \cos(2\pi (f_c - f_m) t) - \frac{A_c \mu}{2} \cos(2\pi (f_c + f_m) t)
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
        html.P("The last step uses the trigonometric identity:"),
        dcc.Markdown(r"""
        $$
        \sin(A) \sin(B) = \frac{1}{2} [\cos(A-B) - \cos(A+B)]
        $$
        """, mathjax=True),

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
            dcc.Graph(id='combined-signal-plot', figure=combined_plot)
        ]),
    ])


def update_plot(carrier_f, modulating_f, modulating_a, carrier_a):
    t = np.linspace(0, 1, 1000) # Time variable

    # Modulating signal equation
    modulating_signal = modulating_a * np.sin(2 * np.pi * modulating_f * t)  

    # carrier wave signal
    carrier_wave = carrier_a * np.sin(2 * np.pi * carrier_f * t)

    # am signal
    am_signal = carrier_wave + (modulating_a/2) * np.cos(2 * np.pi * (modulating_f + carrier_f) * t) - (modulating_a/2) * np.cos(2 * np.pi * (carrier_f - modulating_f  ) * t)


    combined_plot = make_subplots(rows=3, cols=1, subplot_titles=("Carrier Wave", "Modulating Signal", "AM Modulated Signal"))

    combined_plot.append_trace(go.Scatter(x=t, y=carrier_wave, mode='lines', ), row=1, col=1)
    combined_plot.append_trace(go.Scatter(x=t, y=modulating_signal, mode='lines', ), row=2, col=1)
    combined_plot.append_trace(go.Scatter(x=t, y=am_signal, mode='lines', ), row=3, col=1)

    combined_plot.update_layout(height=800)


    return  combined_plot

