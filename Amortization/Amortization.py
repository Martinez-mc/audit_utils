
import numpy as np
import pandas as pd
import numpy_financial as npf

def compounder(start, periods, comp, rate, ann, principal):
    """Returns compounded rate, frequency and payment"""

    frequency = ''
    compounded_rate = 0.00

    if comp == 'Daily':
        if ann == 'Ordinary':
            frequency = 'D' 
        compounded_rate = rate / 365
    elif comp == 'Weekly': 
        if ann == 'Ordinary':
            frequency = 'W'
        else:
            frequency = 'W-MON' 
            compounded_rate = rate / 52
    elif comp == 'Monthly':
        if ann == 'Ordinary':
            frequency = 'ME'
        else:
            frequency = 'MS'
        compounded_rate = rate / 12
    elif comp == 'Semi-Annual':
        compounded_rate = rate / 2
    elif comp == 'Annual':
        if ann == 'Ordinary':
            frequency = 'YE'
        else:
            frequency = 'YS'
        compounded_rate = rate / 1

    dates = pd.date_range(start=start, periods=periods+1, freq=frequency)

    payment = npf.pmt(rate=compounded_rate, nper=periods, pv=-principal)

    return [dates, compounded_rate, payment]
    
def amortize(start, periods, comp, rate, ann, pmt, principal):
    """Returns Amortization Table in HTML format"""
    dates_rates_payment = compounder(start, periods, comp, rate, ann, principal)

    # Populate Payment Column
    pmt_list = [0]
    for x in range(0, periods):
        pmt_list.append(dates_rates_payment[2])

    # Define the data structure
    data = {
            'Date': dates_rates_payment[0],
            'Payment': pmt_list,
            'Interest':[0],
            'Principal':[0],
            'Balance':[principal]
        }

    for t in range(0, periods):
        interest = data['Balance'][-1] * dates_rates_payment[1]
        principal = float(pmt) - interest

        data['Interest'].append(interest)
        data['Principal'].append(principal)
        data['Balance'].append(data['Balance'][-1] - principal)
    
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    # Round the relevant columns to 2 decimal places
    df[['Payment', 'Interest', 'Principal', 'Balance']] = df[['Payment', 'Interest', 'Principal', 'Balance']].round(2)

    # Set values less than 0.5 to 0
    df[['Interest', 'Principal', 'Balance']] = df[['Interest', 'Principal', 'Balance']].apply(lambda x: np.where(x < 0.5, 0, x)).astype(int)

    formatted_df = df.style.format({
      'Payment': '{:,.2f}',
      'Interest': '{:,.2f}',
      'Principal': '{:,.2f}',
      'Balance': '{:,.2f}',
    })

    html = formatted_df.to_html(index=False)
    return [df, html]
