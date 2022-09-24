import pandas as pd
import numpy as np
import yfinance as yf


def GetData(name, startDate, endDate):
    '''
    Function gets stock or security data given a ticker, start date and end date
    :param name (string): security name
    :param startDate (string): start date. YYYY-MM-DD format
    :param endDate (string): end date. YYYY-MM-DD format
    :return df (pandas dataframe): security dataframe
    '''
    df = yf.download(name, start=startDate, end=endDate)
    df["Ticker"] = name
    # Handle potential missing data by doing a forward fill followed by a backfill
    df.fillna(method="ffill", inplace=True)
    df.fillna(method="bfill", inplace=True)

    return df
    #self.SP_df = yf.download("^GSPC", start=startDate, end=endDate)

def ComputeDailyReturns(input_df):
    '''
    Computes the daily returns of a security
    :param input_df (pandas dataframe): input dataframe with date and adjusted close
    :return dailyReturns (pandas dataframe): dataframe with daily returns
    '''
    dailyReturns = input_df[["Adj Close"]].copy()
    dailyReturns = (dailyReturns/dailyReturns.shift(1)) - 1
    dailyReturns.iloc[0,:] = 0
    dailyReturns.rename(columns={dailyReturns.columns[0]:"Daily_Return"}, inplace=True)
    dailyReturns["Ticker"] = input_df.Ticker
    dailyReturns = dailyReturns

    return dailyReturns






if __name__ == "__main__":
    meta = GetData("META", "2022-01-01", "2022-08-15")
    sp500 = GetData("^GSPC", "2022-01-01", "2022-08-15")
    meta_returns = ComputeDailyReturns(meta)
    print(meta_returns.head())
    print(meta.head())
