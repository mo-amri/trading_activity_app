
from io import StringIO

import streamlit as st
import csv
import time
import pandas as pd
from streamlit import session_state


def monitoring_trading():

    st.title("Amri Investment Web Application")
    st.subheader("Monitoring Trading Activity")

    # st.sidebar.markdown("<h1 style='color: salmon;'>Amri Investment Ltd</h1>", unsafe_allow_html=True)
    st.sidebar.subheader("London Stock Exchange")

    with st.sidebar.form("calculater_form"):
        # Get user input
        # ___Create two columns
        col1, col2 = st.columns(2)
        with col1:
            processing_date = st.date_input("Processing Date")
        with col2:
            processing_time = st.time_input("Processing Time")
        company_name = st.text_input("Trading Company Name:")
        trading_budget = st.number_input("Trading Budget GBP", min_value=0.0)
        # ___Create four columns
        col3, col4 = st.columns(2)
        with col3:
            # ----------------------------------------"Please enter the Purchase Price per Share in the input field."
            purchase_price_per_share = st.number_input("Purchase Share Price GBX", min_value=0.0)
        with col4:
            # ----------------------------"Enter The Time at Which The purchase Price Occurred"
            purchase_time = st.text_input("Purchase Time")
        col5, col6 = st.columns(2)
        with col5:
            selling_price_per_share = st.number_input('Selling Share Price GBX', min_value=0.0)
        with col6:
            selling_time = st.text_input("Selling Time")

        # Add a submit button
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Process the form data
            # You can perform any necessary operations with the form data here
            # For example, you can store it in a database or display it on the screen
            st.success("Form Submitted!")
            st.write("Processing Date", processing_date.strftime('%d-%m-%Y'), "Processing Time",  processing_time)
            st.write("Company Name:", company_name)
            st.write("Trading Budget:", trading_budget)
            st.write("Purchase Price per Share:", purchase_price_per_share, "Purchase Time:", purchase_time)
            st.write("Selling Price per Share:", selling_price_per_share, "Selling Time:", selling_time)

    # _____ - Calculate & Display the Data. __________________________________________________________________________
    if st.button("Calculate The Profit or Loss"):

        # Create progress bar
        progress_bar = st.progress(0)
        # Update the progress bar
        for percent_complete in range(100):
            time.sleep(0.01)  # Simulate some computation
            progress_bar.progress(percent_complete + 1)

        # Calculate the trading profit or lost
        amount_of_shares = trading_budget / purchase_price_per_share
        gross_amount = amount_of_shares * selling_price_per_share
        profit_or_lost_made = gross_amount - trading_budget

        # Display the submitted user inputs
       # st.write(f"Trading Date: {processing_date.strftime('%d-%m-%Y')}, Processing Time: {processing_time}")
        st.write(f"Company Name: {company_name}")
        st.write(f"Trading Budget: £{round(trading_budget, 2)}")
        # st.write(f"Purchase Price per Share: {purchase_price_per_share} " f"GBX  - Purchase Time: {purchase_time}")
        st.write(f"Selling Price per Share: {selling_price_per_share} " f"GBX  - Selling Time: {selling_time}")
       # st.write(f"Amount of Shares: {round(amount_of_shares, 2)}")
        st.write(f"Gross Amount: £{round(gross_amount, 2)}")
        # Check up the result
        if profit_or_lost_made == 0:
            st.info(f"NO Profit Made:  £{round(profit_or_lost_made, 2)}")
        elif profit_or_lost_made > 0:
            st.success(f"Profit Made:  £{round(profit_or_lost_made, 2)}")
            st.snow()
        else:
            st.warning(f"Made a loos:  £{round(profit_or_lost_made, 2)}")

    # _____ - Display The Data as a Table. ________________________________________________________________________
    if st.button("Display The Table Data"):
        # Calculate the trading profit or lost
        amount_of_shares = trading_budget / purchase_price_per_share
        gross_amount = amount_of_shares * selling_price_per_share
        profit_or_lost_made = gross_amount - trading_budget

        # Define the data to be written as a table
        data = [
            ['Processing_Date', 'Processing_Time', 'Company_Name', 'Trading_Budget', 'Purchase_Price_per_Share',
             'Purchase Time', 'Selling_Price_per_Share', 'Selling_Time', 'Amount_of_Shares', 'Gross_Amount',
             'Profit_Made'],
            [processing_date.strftime('%d-%m-%Y'), processing_time,  company_name, round(trading_budget, 2),
             round(purchase_price_per_share, 2), purchase_time, round(selling_price_per_share, 2),
             selling_time, round(amount_of_shares, 2), round(gross_amount, 2), round(profit_or_lost_made, 2)]]

        df = pd.DataFrame(data)

        # Display the table
        st.table(df)
        # st.dataframe(df)

    # # +++++++++++++++++++++++++++++ Create a CSV file & Download to the local directory +++++++++++++++++++++++++++
    # if st.button("Download the Data Table to Local Directory"):
    #     # Calculate the trading profit or lost
    #     amount_of_shares = trading_budget / purchase_price_per_share
    #     gross_amount = amount_of_shares * selling_price_per_share
    #     profit_or_lost_made = gross_amount - trading_budget
    #
    #     # # Define the data to be written to the CSV file
    #     data = [
    #         ['Processing_Date', 'Processing_Time', 'Company_Name', 'Trading_Budget', 'Purchase_Price_per_Share',
    #          'Purchase Time', 'Selling_Price_per_Share', 'Selling_Time', 'Amount_of_Shares', 'Gross_Amount',
    #          'Profit_Made'],
    #         [processing_date.strftime('%d-%m-%Y'), processing_time, company_name, round(trading_budget, 2),
    #          round(purchase_price_per_share, 2), purchase_time, round(selling_price_per_share, 2),
    #          selling_time, round(amount_of_shares, 2), round(gross_amount, 2), round(profit_or_lost_made, 2)]]
    #
    #     # Specify the file path for the CSV file
    #     file_path = f"Data/ {company_name} .csv"
    #
    #     # Write the data to the CSV file
    #     with open(file_path, 'w', newline='') as csvfile:
    #         writer = csv.writer(csvfile)
    #         writer.writerows(data)
    #
    #     # Provide a success message to the user
    #     st.success(f"CSV File Downloaded Successfully!")

    # ____ - Download CSV File.  ____________________________________________________________________________________
    # Generate a download button
    if st.button("Download CSV File"):
        # Calculate the trading profit or lost
        amount_of_shares = trading_budget / purchase_price_per_share
        gross_amount = amount_of_shares * selling_price_per_share
        profit_or_lost_made = gross_amount - trading_budget

        data = [
            ['Processing_Date', 'Processing_Time', 'Company_Name', 'Trading_Budget', 'Purchase_Price_per_Share',
             'Purchase Time', 'Selling_Price_per_Share', 'Selling_Time', 'Amount_of_Shares', 'Gross_Amount',
             'Profit_Made'],
            [processing_date.strftime('%d-%m-%Y'), processing_time, company_name, round(trading_budget, 2),
             round(purchase_price_per_share, 2), purchase_time, round(selling_price_per_share, 2),
             selling_time, round(amount_of_shares, 2), round(gross_amount, 2), round(profit_or_lost_made, 2)]]

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
    st.sidebar.subheader("GBX to GBP Converter")

    with st.sidebar.form("my_form_gbx_to_gb"):
        # st.header("GBX to GBP Converter")
        gbx = st.number_input("Enter GBX value:")
        if gbx:
            gbx = float(gbx)
            gbp_result = calculate_gbx_to_gbp(gbx)
            # st.write(f"Equivalent GBP value: {gbp:.2f}")

        submit_button = st.form_submit_button("Submit")

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
    st.sidebar.subheader("GBP to GBX Converter")

    with st.sidebar.form("my_form_gbp_to_gbx"):
        # st.header("GBX to GBP Converter")
        gbp = st.number_input("Enter GBP value:")
        if gbp:
            gbp = float(gbp)
            gbx_result = calculate_gbp_to_gbx(gbp)
            # st.write(f"Equivalent GBP value: {gbp:.2f}")

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Process form submission
            process_data_gbp_to_gbx(gbx_result)

# _____ - Main Entry App Function.  __________________________________________________________________________________


if __name__ == "__main__":
    monitoring_trading()
    converter_gbx_to_gbp()
    converter_gbp_to_gbx()





