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


if __name__ == "__main__":
    print(meta_returns.head())
    print(meta.head())
