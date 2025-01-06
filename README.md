
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

- **Python >= 3.13**
- **aiohttp**: For asynchronous HTTP requests.
- **asyncio**: To manage asynchronous execution.
- **pandas**: For data manipulation and analysis.
- **CSV**: For data storage.

## How to Use

### Prerequisites

Ensure that you have **Python >= 3.13** installed. Use [pyenv](https://github.com/pyenv/pyenv) to manage Python versions if necessary:

1. Install pyenv:
   ```bash
   curl https://pyenv.run | bash
   ```

2. Install Python 3.13:
   ```bash
   pyenv install 3.13
   pyenv local 3.13
   ```

### Setting Up the Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pablomendesfaria/korean-international-trade-scraper.git
   cd korean-international-trade-scraper
   ```

2. **Install Poetry:**
   Poetry is used to manage dependencies and the virtual environment.
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies:**
   Use Poetry to install project dependencies in an isolated environment:
   ```bash
   poetry install
   ```

4. **Activate the virtual environment:**
   ```bash
   poetry shell
   ```

### Running the Scraper

1. Execute the scraper with the desired output file name:
   ```bash
   python app/scraper.py output_file_name.csv
   ```

2. The collected data will be saved in the `output_file_name.csv` file inside the `data` folder.

### Exiting the Virtual Environment

When you finish using the scraper, exit the Poetry virtual environment:
   ```bash
   exit
   ```

## Project Structure

- `app`: Module that stores the project script.
   - `scraper.py`: Main script that performs scraping and saves the data.
- `data`: Folder with the output file.
   - `output_file_name.csv`: File generated with the collected data.
- `.python-version`: Specify the Python version used in the project.
- `pyproject.toml`: Configuration file for Poetry, specifying dependencies and project metadata.
- `.venv/`: Virtual environment directory managed by Poetry (not included in the repository).

## Notes

If you encounter any issues, verify that:
- Your Python version is correctly set to 3.13 using pyenv.
- Poetry has successfully installed all dependencies.

Feel free to open an issue or contribute to the repository!
