import pandas as pd
import numpy as np

def bb(df):
    '''
    Computes the Bollinger Bands (R) technical indicator
    :param inputdf (pandas dataframe): input dataframe with a price column
    :return outputdf (pandas dataframe): output dataframe with bb information
    return fig (plotly figure): chart
    '''
    df["prevPrice"] = df.price.shift(1)
    df["sma"] = df.price.rolling(window=20).mean()
    df["stdev"] = df.price.rolling(window=20).std()
    df["upperBand"] = df.sma + 2.0 * df.stdev
    df["lowerBand"] = df.sma - 2.0 * df.stdev
    df["prevLowerBand"] = df.lowerBand.shift(1)
    df["prevUpperBand"] = df.upperBand.shift(1)

    # BB logic
    ## Buy signal is when the previous price is below the lower band and the current price is above the lower band
    df["buySignal"] = np.where((df.prevPrice < df.prevLowerBand) &
                                    (df.price > df.lowerBand), True , False)
    # Sell signal is when the previous price is above the upper band and the current price is below the upper band
    df["sellSignal"] = np.where((df.prevPrice > df.prevUpperBand) &
                                     (df.price < df.upperBand), True, False)

    # Creating a single vector output to be used by a learner
    df["percentBB"] = (df.price - df.lowerBand)/(df.upperBand - df.lowerBand)

    return df.iloc[20:]