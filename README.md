# trading_activity_app
📊 Amri Investment Web Application (Beta v1.09)
A Streamlit-powered web application for monitoring trading activities on the London Stock Exchange. The app supports detailed trade analysis, profit/loss calculations, GBX/GBP currency conversions, and enhanced CSV management features including multi-file merging.

🚀 Features
✅ Trade Monitoring & Profit/Loss Analysis
	•	Input key trading details such as stock symbol, ISIN, company sector/industry, budget, fees, and share prices.
	•	Calculate profit or loss with real-time currency conversion (GBX ➡ GBP).
	•	Record and display trading strategies, satisfaction ratings, and financial outcomes.
	•	Generate and download reports in table or CSV format.
 
📈 GBX/GBP Currency Conversion Tools
	•	Convert:
	◦	GBX (pence) ➡ GBP (pounds)
	◦	GBP (pounds) ➡ GBX (pence)
	•	Accessible from the app sidebar.
 
🗃️ CSV Tools
	•	Combine multiple CSV files into a single file with one click.
	•	Preview the merged data.
	•	Download the combined CSV. 
Run the app: bash  streamlit run app.py
Note: Replace app.py with the actual filename if different.

📂 File Structure
.
├── app.py              # Main application script
├── README.md           # This file
├── requirements.txt    # Python dependencies
└── ...                 # Optional: CSVs, assets, etc.

📝 Sample Usage
	1	Open the app in your browser via the terminal launch link.
	2	Fill in trading details and click "Calculate Profit / Loss".
	3	View your performance, download reports, or merge existing CSVs.
	4	Use the sidebar tools for GBX/GBP conversion.

💡 Example CSV Combination Workflow
	1	Go to the "📂 CSV Combiner" section.
	2	Upload two or more .csv files.
	3	Preview the merged data.
	4	Click "📥 Download Combined CSV" to get the result.

🔧 Dependencies
	•	Streamlit
	•	Pandas
✅ requirements.txt
streamlit>=1.35.0
pandas>=2.2.0

Optional (for full compatibility / CSV encoding edge cases):
If you're handling more complex CSV files (e.g., with encodings, missing values), you may want to include:
numpy>=1.26.0
Usage:
To install dependencies:
bash
pip install -r requirements.txt

📌 Version
Beta v1.09
	•	Added CSV merging and download functionality
	•	Improved layout and form interactions
	•	GBX/GBP conversion enhancements

👨‍💻 Author
Mo Amri Computer Scientist & Algo Trading Enthusiast Feel free to contribute or report issues.

📃 License
This project is licensed under the MIT License — see the LICENSE file for details.

