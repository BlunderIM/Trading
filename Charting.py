import pandas as pd
import numpy as np
import plotly.graph_objects as go

def computeHistogramBinCount(input_series):
    '''
    Compute the number of bins for histogram plotting using the Freedman-Diaconis rule
    :param input_df (pandas series): input series
    :return bin_count (integer): number of bins
    '''
    n = input_series.shape[0]
    quartiles = input_series.quantile([0.25, 0.75]).tolist()
    q1, q3 = quartiles[0], quartiles[1]
    IQR = q3 - q1
    bin_width = 2 * IQR * n ** (-1 / 3)
    bin_count = int(round((input_series.max() - input_series.min())/bin_width,0))

    return bin_count

def plotHistogram(input_dfs, col):
    fig = go.Figure()
    for df in input_dfs:
        fig.add_trace(go.Histogram(x=df[col], name=df.Ticker.values[0]))
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.8)

    return fig

def plotBBTi(df):
    '''
    Creates a chart with Bollinger Bands (R) indicator
    :param df:
    :return:
    '''

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df.upperBand, mode='lines', name='Bounds', marker_color="orange"))
    fig.add_trace(go.Scatter(x=df.index, y=df.lowerBand, mode='lines', marker_color="orange", showlegend=False,
                             fill="tonexty", fillcolor="rgba(225,235,236,0.3)"))
    fig.add_trace(go.Scatter(x=df.index, y=df.price, mode='lines', name='Price', marker_color="black"))
    fig.add_trace(go.Scatter(x=df.index, y=df.sma, mode='lines', name='SMA', marker_color="royalblue"))
    fig.add_trace(go.Scatter(x=df.index[df.buySignal], y=df[df.buySignal].price, mode="markers",
                             marker_color="green", marker_symbol="triangle-up", marker_size=15, name="Buy Signal"))
    fig.add_trace(go.Scatter(x=df.index[df.sellSignal], y=df[df.sellSignal].price, mode="markers",
                             marker_color="red", marker_symbol="triangle-down", marker_size=15, name="Sell Signal"))

    fig.update_layout(paper_bgcolor="rgb(255,255,255)", plot_bgcolor="rgb(255,255,255)",
                      title_text="Bollinger Bands\u00AE", title_x=0.5, xaxis_title="Date",
                      yaxis_title="Adjusted Close", )
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#E1EBEC')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#E1EBEC')

    return fig



if __name__ == "__main__":
    print("Charting")
