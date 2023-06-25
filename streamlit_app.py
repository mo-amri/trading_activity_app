
import streamlit as st
import pandas as pd



def monitoring_trading():
    # Set the page title and layout
    st.set_page_config(page_title='Amri Investment Web Application', layout='centered')  # wide

    st.title("Amri Investment Web Application")
    st.subheader("Monitoring Trading Activity")

    st.sidebar.write("**London Stock Exchange**")

    with st.sidebar.form("calculater_form"):
        # Get user input
        # ___Create two columns
        col1, col2 = st.columns(2)
        with col1:
            processing_date = st.date_input("Processing Date Data")
        with col2:
            processing_time = st.time_input("Processing Time Data")

        company_name = st.text_input("Company Symbol:")

        col1, col2 = st.columns(2)
        with col1:
            trading_budget = st.number_input("Trading Budget GBP", min_value=0.0)
        with col2:
            trading_fees = st.number_input("Trading Fees GBP", min_value=0.0)

        # ___Create four columns
        col1, col2 = st.columns(2)
        with col1:
            # ----------------------------------------"Please enter the Purchase Price per Share in the input field."
            purchase_price_per_share = st.number_input("Purchase Share Price GBX", min_value=0.0)
        with col2:
            # ----------------------------"Enter The Time at Which The purchase Price Occurred"
            purchase_time = st.text_input("Purchase Time")
        col1, col2 = st.columns(2)
        with col1:
            selling_price_per_share = st.number_input('Selling Share Price GBX', min_value=0.0)
        with col2:
            selling_time = st.text_input("Selling Time")

        # Add a submit button
        submit_button = st.form_submit_button("Calculate Profit / Loss")

        if submit_button:
            # ___ Process the form data & Calculate the trading profit / loss
            # ___ Convert purchase price from GBX to GBP.
            gbp_purchase = purchase_price_per_share / 100
            # ___ Convert selling price from GBX to GBP.
            gbp_selling = selling_price_per_share / 100

            amount_of_shares = trading_budget / gbp_purchase
            gross_amount = amount_of_shares * gbp_selling
            profit_or_lost_made = gross_amount - (trading_budget + trading_fees)

            # Check up the result
            if profit_or_lost_made == 0:
                st.info(f"NO Profit Made:  £{round(profit_or_lost_made, 2)}")
            elif profit_or_lost_made > 0:
                st.success(f"Profit Made:  £{round(profit_or_lost_made, 2)}")
            else:
                st.warning(f"Made a loss:  £ {round(profit_or_lost_made, 2)}")

            # Display the submitted user inputs
            st.write(f"Amount of Shares: {round(amount_of_shares, 2)}")
            st.write(f"Gross Amount: £{round(gross_amount, 2)}")

    # _____ - Display the Data. __________________________________________________________________________
    if st.button("Display Trading Data"):

        # ___ Calculate the trading profit / loss
        # ___ Convert purchase price from GBX to GBP.
        gbp_purchase = purchase_price_per_share / 100
        # ___ Convert selling price from GBX to GBP.
        gbp_selling = selling_price_per_share / 100

        amount_of_shares = trading_budget / gbp_purchase
        gross_amount = amount_of_shares * gbp_selling
        profit_or_lost_made = gross_amount - (trading_budget + trading_fees)

        # Check up the result
        if profit_or_lost_made == 0:
            st.text(f"NO Profit Made: £{round(profit_or_lost_made, 2)}")
        elif profit_or_lost_made > 0:
            st.text(f"Profit Made: £{round(profit_or_lost_made, 2)}")
        else:
            st.text(f"Made a loss: £ {round(profit_or_lost_made, 2)}")

        # ___Display the Data as a column layout
        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Company Symbol: {company_name}")

        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Data Processing Date: {processing_date.strftime('%d-%m-%Y')}")
        with col2:
            st.text(f"Data Processing Time: {processing_time}")

        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Trading Budget: £{trading_budget}")
        with col2:
            st.text(f"Trading Fees: £{trading_fees}")

        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Price per Share: {purchase_price_per_share} GBX")
        with col2:
            st.text(f"Purchase Time: {purchase_time}")

        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Selling Price per Share: {selling_price_per_share} GBX")
        with col2:
            st.text(f"Selling Time: {selling_time}")

        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Amount of Shares: {round(amount_of_shares, 2)}")
        with col2:
            st.text(f"Gross Amount: £{round(gross_amount, 2)}")

    # _____ - Display The Data as a Table. ________________________________________________________________________
    if st.button("Display Data as a Table "):
        # ___ Process the form data & Calculate the trading profit / loss
        # ___ Convert purchase price from GBX to GBP.
        gbp_purchase = purchase_price_per_share / 100
        # ___ Convert selling price from GBX to GBP.
        gbp_selling = selling_price_per_share / 100

        amount_of_shares = trading_budget / gbp_purchase
        gross_amount = amount_of_shares * gbp_selling
        profit_or_lost_made = gross_amount - (trading_budget + trading_fees)

        # Define the data to be written as a table
        data = [
            ['Processing_Date_Data', 'Processing_Time_Data', 'Company_Name', 'Trading_Budget', 'Trading_Fees',
             'Purchase_Price_per_Share', 'Purchase Time', 'Selling_Price_per_Share', 'Selling_Time',
             'Amount_of_Shares', 'Gross_Amount', 'Profit_Made'],
            [processing_date.strftime('%d-%m-%Y'), processing_time,  company_name, round(trading_budget, 2),
             round(trading_fees, 2), round(purchase_price_per_share, 2), purchase_time,
             round(selling_price_per_share, 2), selling_time, round(amount_of_shares, 2),
             round(gross_amount, 2), round(profit_or_lost_made, 2)]]

        df = pd.DataFrame(data)

        # Display the table
        st.table(df)

    # ******* Download CSV File.  *************************************************************************
    # Generate a download button
    if st.button("Download Trading Data"):
        # ___ Process the form data & Calculate the trading profit / loss
        # ___ Convert purchase price from GBX to GBP.
        gbp_purchase = purchase_price_per_share / 100
        # ___ Convert selling price from GBX to GBP.
        gbp_selling = selling_price_per_share / 100

        amount_of_shares = trading_budget / gbp_purchase
        gross_amount = amount_of_shares * gbp_selling
        profit_or_lost_made = gross_amount - (trading_budget + trading_fees)

        data = [
            ['Processing_Date_Data', 'Processing_Time_Data', 'Company_Name', 'Trading_Budget', 'Trading_Fees',
             'Purchase_Price_per_Share', 'Purchase Time', 'Selling_Price_per_Share', 'Selling_Time',
             'Amount_of_Shares', 'Gross_Amount', 'Profit_Made'],
            [processing_date.strftime('%d-%m-%Y'), processing_time, company_name, round(trading_budget, 2),
             round(trading_fees, 2), round(purchase_price_per_share, 2), purchase_time,
             round(selling_price_per_share, 2), selling_time, round(amount_of_shares, 2),
             round(gross_amount, 2), round(profit_or_lost_made, 2)]]

        df = pd.DataFrame(data)
        # Convert DataFrame to CSV File
        csv_file = df.to_csv(index=False, sep=',')

        # Provide the CSV string for download
        st.download_button(label="Click here to download", data=csv_file,
                           file_name=f"{company_name}.csv")

    # ******* Scrape The Top gainer table from Trading View Website ********************************************
    if st.button("Display The UK Top Gainers Table"):
        # url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/' # US Market
        url = 'https://www.tradingview.com/markets/stocks-united-kingdom/market-movers-gainers/'  # UK Market

        tables = pd.read_html(url)

        # ___Check how many table
        len(tables)

        # ___Read Table
        df = tables[0]

        # ___Add column of the current time to the table
        df['Date & Time'] = pd.to_datetime('today').strftime("%d/%m/%Y %H:%M:%S")

        # ___Print the Initial DataFrame
        df

    # ******* Download Top Gainers Table from Trading View Website **********************************************
    # Generate a download button
    if st.button("Download Top Gainers Table"):
        # url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/' # US Market
        url = 'https://www.tradingview.com/markets/stocks-united-kingdom/market-movers-gainers/'  # UK Market

        tables = pd.read_html(url)

        # ___Read Table
        df = tables[0]

        # ___Add column of the current time to the table
        df['Date & Time'] = pd.to_datetime('today').strftime("%d/%m/%Y %H:%M:%S")

        # Convert DataFrame to CSV File
        csv_file = df.to_csv(index=False, sep=',')

        # Provide the CSV string for download
        st.download_button(label="Click here to download", data=csv_file,
                           file_name="Top_Gainers.csv")

    # ****** Display a File Uploader Widget & Querying File Uploaded with User Prompts ***************************
    uploaded_file = st.file_uploader("Upload a CSV file for querying", type=['csv'])
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

        with st.form('Querying'):
            # Display the Search as a column layout
            col1, col2 = st.columns(2)
            with col1:
                search_column_name = st.text_input('Enter Column Name')
            with col2:
                search_column_value = st.text_input('Enter Row Value')

            # Add a submit button
            submit_button = st.form_submit_button("Generate")
            if submit_button:
                # Check if the search column name is provided
                if len(search_column_name .strip()) == 0:
                    st.error("Enter a column name!")
                # Check if the search column exists in the DataFrame
                elif search_column_name not in dataframe.columns:
                    st.warning(f"Column name {search_column_name} not found in the table.")
                # Check if the search column value is provided
                elif len(search_column_value.strip()) == 0:
                    st.error("Enter a row value!")
                # Check if the search column value exists in the DataFrame
                elif search_column_value not in dataframe[search_column_name].values:
                    st.warning(f"Value {search_column_value} not found in the column {search_column_name }")
                else:
                    # Iterate over each row in the DataFrame
                    for index, row in dataframe.iterrows():
                        # Check if the search value matches the desired column
                        if row[search_column_name ] == search_column_value:
                            # Entry found, perform the desired action
                            st.info("Entry Found")
                            st.write(row)

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
    st.sidebar.write("**GBX to GBP Converter**")

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
    st.sidebar.write("**GBP to GBX Converter**")

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





