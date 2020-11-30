import pandas as pd
import yfinance as yf
import locale
import datetime

# Creates variable for While loop to allow user to enter multiple stock tickers
loop_variable = 'yes'

# Creating empty dataframe
analysis_df = pd.DataFrame(columns=['Ticker', 'Name', #'Summary',
                                    'Sector', 'Industry', 'Market Cap',
                                    'Enterprise Value', 'Net Profit Margin',
                                    'Beta', 'P/E', 'Forward EPS', 'Trailing EPS',
                                    'PEG','P/B','Dividend Yield','Dividend Payout Ratio','Institutional Holding'])

# Begin while loop
# User inputs 1 stock ticker
# Calling Yahoo Finance API to return stock data points
while loop_variable.upper() == 'YES':

    input_ticker = input('Input 1 stock ticker ')

    stock = yf.Ticker(input_ticker)

    # this returns a long string of stuff
    # putting all this info into a datframe
    stock_info_df = stock.info

    stock_name = stock_info_df['shortName']
    print('Name: ' + stock_name)

    stock_info = stock_info_df['longBusinessSummary']
    print('Summary: ' + stock_info)

    stock_sector = stock_info_df['sector']
    print('Sector: '+ stock_sector)

    stock_industry = stock_info_df['industry']
    print('Industry: '+ stock_industry)

    locale.setlocale(locale.LC_ALL, '')
    stock_marketcap = str('{:n}'.format(round(stock_info_df['marketCap']/1000000,1)))
    print(f"Market Cap: ${stock_marketcap} million")

    stock_enterprisevalue = str('{:n}'.format(round(stock_info_df['enterpriseValue']/1000000,1)))
    print(f"Enterprise Value: ${stock_enterprisevalue} million")

    stock_netmargin = str(round(stock_info_df['profitMargins']*100,4))
    print(f"Net Profit Margin: {stock_netmargin}%")

    if stock_info_df['beta'] is None:
        stock_beta = str(0)
    else:
        stock_beta = str(round(stock_info_df['beta'],2))
    print('Beta: '+ stock_beta)

    if stock_info_df['trailingPE'] is None:
        stock_pe = str(0)
    else:
        stock_pe = str(round(stock_info_df['trailingPE'],2))
    print('PE: '+ stock_pe)

    if stock_info_df['forwardEps'] is None:
        stock_forwardeps = str(0)
    else:
        stock_forwardeps = str(round(stock_info_df['forwardEps'],2))
    print('Forward PE: '+ stock_forwardeps)

    if stock_info_df['trailingEps'] is None:
        stock_trailingeps = str(0)
    else:
        stock_trailingeps = str(round(stock_info_df['trailingEps'],2))
    print('Trailing EPS: '+ stock_trailingeps)

    if stock_info_df['pegRatio'] is None:
        stock_peg = str(0)
    else:
        stock_peg = str(round(stock_info_df['pegRatio'],2))
    print('PEG: '+ stock_peg)

    if stock_info_df['priceToBook'] is None:
        stock_pricetobook = str(0)
    else:
        stock_pricetobook = str(round(stock_info_df['priceToBook'],2))
    print('PB: '+ stock_pricetobook)

    stock_dividend = str(round(int(stock_info_df['trailingAnnualDividendYield'] or 0) *100,2))
    print('Dividend Yield: '+ stock_dividend + '%')

    stock_payout = str(round(stock_info_df['payoutRatio']*100,4))
    print('Dividend Payout: '+ stock_payout + '%')

    stock_insthold = str(round(stock_info_df['heldPercentInstitutions']*100,2))
    print('Institutional Holding: '+ stock_insthold + '%')

    data = {'Ticker': [input_ticker],
            'Name': [stock_name],
            # 'Summary': [stock_info],
            'Sector': [stock_sector],
            'Industry': [stock_industry],
            'Market Cap': [stock_marketcap],
            'Enterprise Value': [stock_enterprisevalue],
            'Net Profit Margin': [stock_netmargin],
            'Beta': [stock_beta],
            'P/E': [stock_pe],
            'Forward EPS': [stock_forwardeps],
            'Trailing EPS': [stock_trailingeps],
            'PEG': [stock_peg],
            'P/B': [stock_pricetobook],
            'Dividend Yield': [stock_dividend],
            'Dividend Payout Ratio': [stock_payout],
            'Institutional Holding': [stock_insthold]}


    analysis_df = analysis_df.append(data, ignore_index=True)

    # analysis_df = analysis_df.insert(column_df,input_ticker,data,True)

    loop_subvariable = 1
    while loop_subvariable == 1:

        loop_variable = input('Do you wish to enter another ticker? Enter "YES" or "NO" ')
        if loop_variable.upper() == 'YES' or loop_variable.upper() == 'NO':
            loop_subvariable = 0
        else:
            loop_subvariable = 1
            print('ERROR: Please enter Yes or No')

# Output results into CSV file
print(analysis_df)
pd.DataFrame.to_csv(analysis_df,path_or_buf = r'C:\Users\Temp\Documents\Stock_Funadmental_Analysis.csv', sep=',')
