
# Korean International Trade Scraper

This project is a Python scraper that collects information about trade statistics between South Korea and foreign countries from the [TradeData](https://tradedata.go.kr/cts/index_eng.do#tabHsSgn2) website. It is designed to handle multiple pages and uses a hidden API, discovered through page inspection, to perform asynchronous requests efficiently.

## Features

- **Data Scraping:** Collects information on import and export between South Korea and foreign countries.
- **Asynchronous Requests:** Uses `aiohttp` and `asyncio` to improve scraper performance, especially when dealing with multiple pages.
- **DataFrame Generation:** The collected data is organized into a `pandas DataFrame`.
- **CSV storage:** The data is saved in a structured CSV file for later analysis.

## Data Collected

The scraper collects the following information from the website:

- **Year:** Year in which the trade took place.
- **Country:** Country with which Korea traded.
- **Goods:** Goods that were traded.
- **Export Weight:** Weight of exports in tons.
- **Export Value:** Monetary value of exports in dollars.
- **Import Weight:** Weight of imports in tons.
- **Import Value:** Monetary value of imports in dollars.
- **Balance of Trade:** Difference between the value of exports and imports.

## Technologies Used

- **Python 3.x**
- **aiohttp**: For asynchronous HTTP requests.
- **asyncio**: To manage asynchronous execution.
- **pandas**: For data manipulation and analysis.
- **CSV**: For data storage.

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pablomendesfaria/korean-international-trade-scraper.git
   cd korean-international-trade-scraper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper:**
   ```bash
   python scrape/scrapy.py output_file_name
   ```

4. **Access the data:**

   The collected data will be available in the `provided_file_name.csv` file generated at the scrape folder.

## Project Structure

- `scrape`: Module that stores the project's source files, such as the script, a sample of the scraped data and the output file.
- `scrapy.py`: Main script that performs scraping and saves the data.
- `requirements.txt`: List of project dependencies.
- `nome_informado.csv`: File generated with the collected data.
