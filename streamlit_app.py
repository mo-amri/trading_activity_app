##########################################################################################################
# Beta v1.10 Enhancements:
# Removed the "Generate a trading activity table" Button
# Try to wake up the app 
##########################################################################################################
import streamlit as st
import pandas as pd
import warnings
import io

warnings.filterwarnings('ignore')


def monitoring_trading():
    # Set the page title and layout
    st.set_page_config(page_title='Amri Investment Web Application', layout='centered')  # wide

    st.title("Amri Investment Web Application")
    st.subheader("Monitoring Trading Activity")

    st.sidebar.header("London Stock Exchange")
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

            # ___Check up the result & displayed.
            # create a string for currency presentation & rounding to 2 figure.
            spec: str = ',.2f'
            if profit_or_lost_made == 0:
                st.info(f"NO Profit Made: £{profit_or_lost_made: {spec}}")
            elif profit_or_lost_made > 0:
                st.success(f"Profit Made:  £{profit_or_lost_made: {spec}}")
            else:
                st.warning(f"Made a loss:  £ {profit_or_lost_made: {spec}}")

    # *************************** Display the Data as a Text Format. ***************************************************
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

        # create a string for currency presentation & rounding to 2 figure.
        spec: str = ',.2f'
        # Create a string for rounding currency variable to 2 figure.
        round_2_figure: str = '.2f'
        col1, col2 = st.columns(2)
        with col1:
            st.text(f"Trading Budget: £{trading_budget:{spec}}")
        with col2:
            st.text(f"Trading Fees: £{trading_fees:{spec}}")

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
            st.text(f"Quantity of Shares: {amount_of_shares: {round_2_figure}}")
        with col2:
            st.text(f"Gross Amount: £{gross_amount:{spec}}")

        # ___Check up the result & displayed.
        if profit_or_lost_made == 0:
            st.info(f"NO Profit Made: £{profit_or_lost_made:{spec}}")
        elif profit_or_lost_made > 0:
            st.success(f"Profit Made:  £{profit_or_lost_made:{spec}}")
        else:
            st.warning(f"Made a loss:  £ {profit_or_lost_made:{spec}}")

    # *************************** Download the data as a CSV File. ********************************************
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

        # ___Create a dictionary of the data to be displayed as a table
        # create a string for currency presentation & rounding to 2 figure.
        spec: str = ',.2f'
        # Create a string for rounding currency variable to 2 figure.
        round_2_figure: str = '.2f'
        data = {
            'Stock Symbol': [stock_symbol],
            'Closing Deal Satisfaction': [overall_satisfaction],
            'Trading Strategies': [trading_strategies],
            'Trading Date': [trading_date.strftime('%d-%m-%Y')],
            'Trading Budget': [f'£{trading_budget:{spec}}'],
            'Profit Made': [f'£{profit_or_lost_made: {spec}}'],
            'Buy Price per Share': [f'{buy_price_per_share: {round_2_figure}} GBX'],
            'Buy Date/Time': [buy_date_time],
            'Sell Price per Share': [f'{sell_price_per_share: {round_2_figure}} GBX'],
            'Sell Date/Time': [sell_date_time],
            'ISIN': [isin],
            'Company Website': [company_website],
            'Sector': [sector],
            'Industry': [industry],
            'Quantity of Shares': [f'{amount_of_shares: {round_2_figure}}'],
            'Gross Amount': [f'£{gross_amount:{spec}}'],
            'Trading Fees': [f'£{trading_fees:{spec}}']
        }

        df = pd.DataFrame(data)

        # Set the "Stock Symbol" column as the index
        df.set_index('Stock Symbol', inplace=True)

        # Convert DataFrame to CSV File
        csv_file = df.to_csv(index=True, sep=',')

        # Provide the CSV string for download
        st.download_button(label="Click here to download", data=csv_file,
                           file_name=f"{stock_symbol}.csv")

    # ****************** Combine multiple CSV files into one. And then download the merging csv file *****************

    st.subheader("📂 CSV Combiner")
    st.markdown("Upload multiple CSV files and download a single combined file.")

    # File uploader
    uploaded_files = st.file_uploader("Upload CSV files", type="csv", accept_multiple_files=True)

    if uploaded_files:
        try:
            # Read and combine
            df_list = [pd.read_csv(file) for file in uploaded_files]
            combined_df = pd.concat(df_list, ignore_index=True)

            # Preview
            st.success("✅ Files combined successfully!")
            st.write("Preview of combined data:")
            st.dataframe(combined_df.head())

            # Download
            csv_buffer = io.StringIO()
            combined_df.to_csv(csv_buffer, index=False)
            st.download_button(
                label="📥 Download Combined CSV",
                data=csv_buffer.getvalue(),
                file_name="combined.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.info("Please upload two or more CSV files.")

    # *************************************************************************************************************
    # ******************************END OF Function monitoring_trading()******************************************
    # *************************************************************************************************************

# ******* Convert GBX to GBP. *********************************
def calculate_gbx_to_gbp(gbx_amount):
    gbp_amount = gbx_amount / 100
    return gbp_amount


def process_data_gbx_to_gbp(gbp):
    st.write(f"GBP Value: £ {gbp}")  # round(gbp, 2)


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
    st.write(f"GBX Value: {gbx} GBX")


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


