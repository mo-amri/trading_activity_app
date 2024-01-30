##########################################################################################################
# Beta v1.06 Enhancements
# Adding a survey satisfaction question to the interface
# How were satisfaction with the trade closure.
##########################################################################################################

import streamlit as st
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


def monitoring_trading():
    # Set the page title and layout
    st.set_page_config(page_title='Amri Investment Web Application', layout='centered')  # wide

    st.title("Amri Investment Web Application")
    st.subheader("Monitoring Trading Activity")

    st.sidebar.title("London Stock Exchange")
    with st.sidebar.form("calculater_form"):

        # Get user input of the stock symbol
        stock_symbol = st.text_input("Stock Symbol")

        # Store the initial value of widgets in session state
        if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False

        # ___Create two columns
        col1, col2 = st.columns(2)
        with col1:
            # Get the trading Strategies
            trading_strategies = st.selectbox(
                "Trading Strategies",
                ("Day Trading", "Swing Trading", "Value Investing"),
                label_visibility=st.session_state.visibility,
                disabled=st.session_state.disabled,

            )

        with col2:
            # Get the trading date
            trading_date = st.date_input("Trading Date")

        # ___Create two columns
        col1, col2 = st.columns(2)
        with col1:
            # Get the trading trading_date
            isin = st.text_input("ISIN")
        with col2:
            company_website = st.text_input("Company Website")

        # ___Create two columns
        col1, col2 = st.columns(2)
        with col1:
            sector = st.text_input("Sector")
        with col2:
            industry = st.text_input("Industry")

        # ___Create two columns
        col1, col2 = st.columns(2)
        with col1:
            trading_budget = st.number_input("Trading Budget GBP", min_value=0.0)
        with col2:
            trading_fees = st.number_input("Trading Fees GBP", min_value=0.0)

        # ___Create four columns
        col1, col2 = st.columns(2)
        with col1:
            # ------------------------"Please enter the Purchase Price per Share in the input field."
            buy_price_per_share = st.number_input("Buy Share Price GBX", min_value=0.0)
        with col2:
            # ------------------------"Enter The Time at Which The purchase Price Occurred"
            buy_date_time = st.text_input("Buy trading_date/Time")
        col1, col2 = st.columns(2)
        with col1:
            sell_price_per_share = st.number_input('Sell Share Price GBX', min_value=0.0)
        with col2:
            sell_date_time = st.text_input("Sell Date/Time")

        # Get the user input of trading satisfaction
        st.write("Satisfaction With The Trade Closure")

        overall_satisfaction = st.select_slider(
            "Overall Satisfaction",
            options=["Very Unsatisfied", "Unsatisfied", "Neutral", "Satisfied", "Very Satisfied"],
            format_func=lambda x: x,
        )

        # Add a submit button
        submit_button = st.form_submit_button("Calculate Profit / Loss")

        if submit_button:
            # ___ Process the form data & Calculate the trading profit / loss
            # ___ Convert purchase price from GBX to GBP.
            gbp_purchase = buy_price_per_share / 100
            # ___ Convert selling price from GBX to GBP.
            gbp_selling = sell_price_per_share / 100

            amount_of_shares = trading_budget / gbp_purchase
            gross_amount = amount_of_shares * gbp_selling
            profit_or_lost_made = gross_amount - (trading_budget + trading_fees)

            # st.info(f"Your satisfaction response '{overall_satisfaction}' has been recorded. Thank you!")

            # Check up the result
            if profit_or_lost_made == 0:
                st.info(f"NO Profit Made:  £{round(profit_or_lost_made, 2)}")
            elif profit_or_lost_made > 0:
                st.success(f"Profit Made:  £{round(profit_or_lost_made, 2)}")
            else:
                st.warning(f"Made a loss:  £ {round(profit_or_lost_made, 2)}")

            # ___ Display the Amount of Shares & Gross Amount
            # st.write(f"Amount of Shares: {round(amount_of_shares, 2)}")
            # st.write(f"Gross Amount: £{round(gross_amount, 2)}")

    # _____ - Display the Data. __________________________________________________________________________
    if st.button("Display Trading Activity Data"):

        # ___ Convert purchase price from GBX to GBP.
        gbp_purchase = buy_price_per_share / 100
        # ___ Convert selling price from GBX to GBP.
        gbp_selling = sell_price_per_share / 100

        # ___ Calculate the trading profit / loss.
        amount_of_shares = trading_budget / gbp_purchase
        gross_amount = amount_of_shares * gbp_selling
        profit_or_lost_made = gross_amount - (trading_budget + trading_fees)

        # ___Display the Stock Symbol
        st.text(f"Stock Symbol: {stock_symbol}")

        # ___Display the level of satisfaction with the trade closure
        st.text(f"Closing Deal Satisfaction: {overall_satisfaction}")

        # ___Display the Data as a column layout
        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Trading Strategies: {trading_strategies}")
        with col2:
            st.text(f"Trading Date: {trading_date.strftime('%d-%m-%Y')}")

        # ___Display the Data as a column layout
        col1, col2 = st.columns(2)
        with col1:
            st.text(f"ISIN: {isin}")
        with col2:
            st.text(f"Company Website: {company_website}")

        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Sector: {sector}")
        with col2:
            st.text(f"Industry: {industry}")

        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Trading Budget: £{trading_budget}")
        with col2:
            st.text(f"Trading Fees: £{trading_fees}")

        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Buy Price per Share: {buy_price_per_share} GBX")
        with col2:
            st.text(f"Buy Date/Time: {buy_date_time}")

        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Sell Price per Share: {sell_price_per_share} GBX")
        with col2:
            st.text(f"Sell Date/Time: {sell_date_time}")

        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Amount of Shares: {round(amount_of_shares, 2)}")
        with col2:
            st.text(f"Gross Amount: £{round(gross_amount, 2)}")

        # Print the profit / lost result:
        if profit_or_lost_made == 0:
            st.info(f"NO Profit Made: £{round(profit_or_lost_made, 2)}")
        elif profit_or_lost_made > 0:
            st.success(f"Profit Made: £{round(profit_or_lost_made, 2)}")
        else:
            st.warning(f"Made a loss: £ {round(profit_or_lost_made, 2)}")

    # _____ - Display The Data as a Table. ________________________________________________________________________
    if st.button("Generate a Trading Activity Table "):
        # ___ Process the form data & Calculate the trading profit / loss
        # ___ Convert purchase price from GBX to GBP.
        gbp_purchase = buy_price_per_share / 100
        # ___ Convert selling price from GBX to GBP.
        gbp_selling = sell_price_per_share / 100

        amount_of_shares = trading_budget / gbp_purchase
        gross_amount = amount_of_shares * gbp_selling
        profit_or_lost_made = gross_amount - (trading_budget + trading_fees)

        # Create a dictionary of the data to be displayed as a table
        data = {
            'Stock Symbol': [stock_symbol],
            'Closing Deal Satisfaction': [overall_satisfaction],
            'Trading Strategies': [trading_strategies],
            'Trading Date': [trading_date],
            'Trading Budget': [round(trading_budget, 2)],
            'Profit Made': [round(profit_or_lost_made, 2)],
            'Buy Price per Share': [round(buy_price_per_share, 2)],
            'Buy Date/Time': [buy_date_time],
            'Sell Price per Share': [round(sell_price_per_share, 2)],
            'Sell Date/Time': [sell_date_time],
            'ISIN': [isin],
            'Company Website': [company_website],
            'Sector': [sector],
            'Industry': [industry],
            'Amount of Shares': [round(amount_of_shares, 2)],
            'Gross Amount': [round(gross_amount, 2)],
            'Trading Fees': [round(trading_fees, 2)]
        }

        df = pd.DataFrame(data)

        # Set the "Stock Symbol" column as the index
        df.set_index('Stock Symbol', inplace=True)

        # Display the table
        st.table(df)

    # ******* Download CSV File.  *************************************************************************
    # Generate a download button
    if st.button("Download CSV Table of Trading Activity"):
        # ___ Process the form data & Calculate the trading profit / loss
        # ___ Convert purchase price from GBX to GBP.
        gbp_purchase = buy_price_per_share / 100
        # ___ Convert selling price from GBX to GBP.
        gbp_selling = sell_price_per_share / 100

        amount_of_shares = trading_budget / gbp_purchase
        gross_amount = amount_of_shares * gbp_selling
        profit_or_lost_made = gross_amount - (trading_budget + trading_fees)

        # Create a dictionary of the data to be displayed as a table
        data = {
            'Stock Symbol': [stock_symbol],
            'Closing Deal Satisfaction': [overall_satisfaction],
            'Trading Strategies': [trading_strategies],
            'Trading Date': [trading_date],
            'Trading Budget': [round(trading_budget, 2)],
            'Profit Made': [round(profit_or_lost_made, 2)],
            'Buy Price per Share': [round(buy_price_per_share, 2)],
            'Buy Date/Time': [buy_date_time],
            'Sell Price per Share': [round(sell_price_per_share, 2)],
            'Sell Date/Time': [sell_date_time],
            'ISIN': [isin],
            'Company Website': [company_website],
            'Sector': [sector],
            'Industry': [industry],
            'Amount of Shares': [round(amount_of_shares, 2)],
            'Gross Amount': [round(gross_amount, 2)],
            'Trading Fees': [round(trading_fees, 2)]
        }

        df = pd.DataFrame(data)

        # Set the "Stock Symbol" column as the index
        df.set_index('Stock Symbol', inplace=True)

        # Convert DataFrame to CSV File
        csv_file = df.to_csv(index=True, sep=',')

        # Provide the CSV string for download
        st.download_button(label="Click here to download", data=csv_file,
                           file_name=f"{stock_symbol}.csv")

    # ******  Uploader Widget for Uploading a CSV File  ***************************
    uploaded_file = st.file_uploader("Upload a CSV file")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

    # *************************************************************************************************************
    # ******************************END OF Function monitoring_trading()******************************************
    # *************************************************************************************************************


# ******* Convert GBX to GBP. *********************************
def calculate_gbx_to_gbp(gbx_amount):
    gbp_amount = gbx_amount / 100
    return gbp_amount


def process_data_gbx_to_gbp(gbp):
    st.write("GBP Value: (£)", gbp)  # round(gbp, 2)


def converter_gbx_to_gbp():
    st.sidebar.write("GBX to GBP Converter")

    with st.sidebar.form("my_form_gbx_to_gb"):
        # st.header("GBX to GBP Converter")
        gbx = st.number_input("Enter GBX value:")
        if gbx:
            gbx = float(gbx)
            gbp_result = calculate_gbx_to_gbp(gbx)
            # st.write(f"Equivalent GBP value: {gbp:.2f}")

        submit_button = st.form_submit_button("Convert")

        if submit_button:
            # Process form submission
            process_data_gbx_to_gbp(gbp_result)

# ******* Convert GBP to GBX. **************************************


def calculate_gbp_to_gbx(gbp_amount):
    gbx_amount = gbp_amount * 100
    return gbx_amount


def process_data_gbp_to_gbx(gbx):
    # Process the form data
    st.write("GBX Value: (GBX)", gbx)


def converter_gbp_to_gbx():
    st.sidebar.write("GBP to GBX Converter")

    with st.sidebar.form("my_form_gbp_to_gbx"):
        # st.header("GBX to GBP Converter")
        gbp = st.number_input("Enter GBP value:")
        if gbp:
            gbp = float(gbp)
            gbx_result = calculate_gbp_to_gbx(gbp)
            # st.write(f"Equivalent GBP value: {gbp:.2f}")

        submit_button = st.form_submit_button("Convert")

        if submit_button:
            # Process form submission
            process_data_gbp_to_gbx(gbx_result)

# ******* Main Entry App Function. ************************************


if __name__ == "__main__":
    monitoring_trading()
    converter_gbx_to_gbp()
    converter_gbp_to_gbx()
    
