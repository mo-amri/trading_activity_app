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
            st.text(f"Processing Date Data: {processing_date.strftime('%d-%m-%Y')}")
        with col2:
            st.text(f"Processing Time Data: {processing_time}")

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

    # ____ - Download CSV File.  ____________________________________________________________________________________
    # Generate a download button
    if st.button("Download CSV File"):
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
        csv_file = df.to_csv(index=False)

        # Provide the CSV string for download
        st.download_button(label="Click here to download", data=csv_file,
                           file_name=f"{company_name} .csv")

    # _____ - Display a File Uploader Widget. ________________________________________________________________________
    uploaded_file = st.file_uploader("Choose a File")
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

        # # To convert to a string based IO:
        # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # st.write(stringio)
        #
        # # To read file as string:
        # string_data = stringio.read()
        # st.write(string_data)

    # _____________________________ - END OF Function monitoring_trading() -  ________________________________________

# _____- Convert GBX to GBP. - _________________________________________________


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

# _____ - Convert GBP to GBX.  ________________________________________________________________________________________


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

# _____ - Main Entry App Function.  __________________________________________________________________________________


if __name__ == "__main__":
    monitoring_trading()
    converter_gbx_to_gbp()
    converter_gbp_to_gbx()





