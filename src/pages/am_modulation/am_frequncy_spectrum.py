import numpy as np
import plotly.graph_objs as go
from dash import html, dcc
from dash.dependencies import Input, Output
from scipy.fftpack import fft, fftfreq
import dash_bootstrap_components as dbc


def AMFrequencySpectrumPage():
    return html.Div([
        html.H3("Frequency Spectrum of AM Signal"),

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

        html.P("Frequency Spectrum:"),
          dcc.Markdown(r"""
        $$
        S(f) = \frac{A_c}{2} \left[ \delta(f - f_c) + \delta(f + f_c) \right] + \frac{A_c k_a A_m}{4} \left[ \delta(f - (f_c - f_m)) + \delta(f + (f_c - f_m)) \right] + \frac{A_c k_a A_m}{4} \left[ \delta(f - (f_c+ f_m)) + \delta(f + (f_c + f_m)) \right] 
        $$
        """, mathjax=True),

        html.H4("Adjust AM Parameters", className="mt-5 py-3"),
        
        dbc.Card([
            html.H6("Carrier Frequency (Hz)"),
            dcc.Slider(
                id='carrier-frequency-slider-freq',
                min=1, max=30, value=25,
                tooltip={"placement": "bottom", "always_visible": True}
            ),
            html.H6("Carrier Amplitude"),
            dcc.Slider(
                id='carrier-amplitude-slider-freq',
                min=1, max=10, value=8,
                tooltip={"placement": "bottom", "always_visible": True}
            ),
            html.H6("Modulating Frequency (Hz)"),
            dcc.Slider(
                id='modulating-frequency-slider-freq',
                min=1, max=30, value=3,
                tooltip={"placement": "bottom", "always_visible": True}
            ),
            html.H6("Modulating Amplitude"),
            dcc.Slider(
                id='modulating-amplitude-slider-freq',
                min=1, max=10, value=4,
                tooltip={"placement": "bottom", "always_visible": True}
            ),
             html.H6("Amplitude Sensitivity"),
            dcc.Slider(id='amplitude-sensitivity-slider', min=0, max=2, value=0.2, tooltip={"placement": "bottom", "always_visible": True}),
            dcc.Graph(id='am-signal-time-domain'),
            dcc.Graph(id='am-signal-frequency-domain'),
        ], className='p-3 mt-3'),

    ])

def compute_am_signal(carrier_f, modulating_f, modulating_a, carrier_a, amp_sens):
    """Generate AM signal and compute its Fourier Transform with correct scaling."""
    fs = 1000  # Sampling rate (Hz)
    T = 1.0    # Signal duration (sec)
    t = np.linspace(0, T, fs, endpoint=False)  

    N = len(t)     # Number of samples


    # AM Modulated Signal
    modulating_signal = modulating_a * np.cos(2 * np.pi * modulating_f * t)  
    carrier_wave = carrier_a * np.cos(2 * np.pi * carrier_f * t)
    am_signal = (1 + (amp_sens * modulating_signal)) * carrier_wave

    # Compute Fourier Transform (Correct Scaling)
    fft_values = fft(am_signal) / N  # Normalize by number of samples
    freqs = fftfreq(N, 1/fs)  # Frequency bins
    fft_magnitude = np.abs(fft_values)  # Get amplitude correctly

    return t, am_signal, freqs, fft_magnitude

def am_frequency_spectrum_callback(app):
    @app.callback(
        [Output('am-signal-time-domain', 'figure'),
         Output('am-signal-frequency-domain', 'figure')],
        [Input('carrier-frequency-slider-freq', 'value'),
         Input('carrier-amplitude-slider-freq', 'value'),
         Input('modulating-frequency-slider-freq', 'value'),
         Input('modulating-amplitude-slider-freq', 'value'),
         Input('amplitude-sensitivity-slider', 'value')]
    )
    def update_am_spectrum(carrier_f, carrier_a, modulating_f, modulating_a, amp_sens):
        t, am_signal, freqs, fft_amplitude = compute_am_signal(carrier_f, modulating_f, modulating_a, carrier_a, amp_sens)

        # Time-domain plot
        time_plot = go.Figure()
        time_plot.add_trace(go.Scatter(x=t, y=am_signal, mode='lines', name='AM Modulated Signal'))
        time_plot.update_layout(title="AM Signal in Time Domain", xaxis_title="Time (s)", yaxis_title="Amplitude", template="plotly_dark")

        # Frequency-domain plot (including negative frequencies)
        freq_plot = go.Figure()
        freq_plot.add_trace(go.Scatter(
                        x=freqs, 
                        y=fft_amplitude, 
                        mode='lines', 
                        name='Frequency Spectrum',
                        line=dict(color='orange')  # Set the line color to orange
))
        freq_plot.update_layout(title="Frequency Spectrum of AM Signal", xaxis_title="Frequency (Hz)", yaxis_title="Amplitude", template="plotly_dark")

        return time_plot, freq_plot
