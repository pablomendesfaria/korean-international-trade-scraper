import asyncio
import csv
import time
from datetime import datetime
from sys import argv

import aiohttp
import pandas as pd


async def fetch(session, url, payload, page, retries=3):
    """Make the request on the URL, if the request fails, it will be redone several times, if it fails every time the program will be terminated

    Args:
        session (aiohttp.ClientSession): A session to perform multiple requests (if necessary)
        url (str): String representing the server url
        payload (str): The content I want to request from the server
        page (int): The server page that will be scraped
        retries (int, optional): The number of attempts to make a request to the server. Defaults to 3.

    Returns:
        dict: The response in JSON
        None: If all three attempts failed
    """
    for attempt in range(retries):
        try:
            async with session.post(url, data=payload) as response:  # Make the request
                if response.status == 200:
                    return await response.json()  # If the connection is successful, return the response in JSON
                else:
                    print(f"Error {response.status} on page {page}")  # Otherwise, it prints the error status and the page number where the error occurred.
        except asyncio.TimeoutError:
            print(f"Timeout on page {page}")  # In the case of timeout, print the page number where it occurred
        except aiohttp.ClientError as e:
            print(f"Client error on page {page}: {e}")  # In case of an error with the client, print the page where it occurred and what error occurred.
        await asyncio.sleep(2)  # Wait before trying again, for cases where error occurred
    return None  # After 3 failed attempts, it returns None


async def main():
    url = "https://tradedata.go.kr/cts/hmpgEng/retrieveTradeHsCountryEng.do"
    tasks = []  # List that will store the tasks, to be executed asynchronously
    results = []  # List that will store all items on each page
    timeout = aiohttp.ClientTimeout(total=90)  # Total timeout for each session in seconds
    connector = aiohttp.TCPConnector(limit=10)  # Limit of simultaneous connections, change as needed, always respecting the client's server limit
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "WMONID=5Pn7h-vJdpd; JSESSIONID=0001iNgPvlGG-VXNAfBxXs1c2Cb1mHIYGC92ZqTt4M-nBon8kWn8qKwq0DErtap0xH7E1Lq7bkiiAzW2wUn2WIOEFZ6EcboFutXPqViyyvN_qaPwANHUQhQMsKE1ENnASCm8:cts11",
        "Origin": "https://tradedata.go.kr",
        "Referer": "https://tradedata.go.kr/cts/index_eng.do",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "X-KL-kfa-Ajax-Request": "Ajax_Request",
        "X-Requested-With": "XMLHttpRequest",
        "isAjax": "true",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
    }  # The header generated when copying the cURL from the website's API, I did not change

    async with aiohttp.ClientSession(timeout=timeout, connector=connector, headers=headers) as session:  # Creates a session, this way there is no need to create and close a session for each new request
        page = 1  # The first page
        batch_size = 5  # The number of concurrent tasks in each batch
        batch_number = 1  # To count the number of batches made
        # HS code is the acronym for Harmonized System Code, which is a product classification system globally used by customs authorities.
        hs_code_chapters = "HS2_SGN"  # Make the request to get chapters.
        hs_code_headings = "HS4_SGN"  # Performs the request to get headings, which is a specific category of products within a chapter.
        hs_code_subheadings = "HS6_SGN"  # Performs the request to get subheadings, which is a subcategory within a heading.
        hs_code = ""  # Here a specific HS code can be entered to perform a more specific search. Including specific chapter, heading and subheading.
        # For example, 70 represents the chapter for glass and glassware; 70.09 represents the heading for glass mirrors, and 700910 is the subheading for rearview mirrors for vehicles.
        country_name = ""  # To search for trade information between Korea and a specific country, enter the country name here. For multiple countries add %2C between each country name.
        # like Algeria%2CAustralia%2CBangladesh
        while True:
            # The payload is the search and filtering data generated by copying the cURL from the website's api.
            # Here, the page number will be changed dynamically, to go through all existing pages.
            # The HS code can be changed as needed using the variables above.
            # The number of rows displayed has been changed to 10.000 to reduce the number of requests made to the site.
            if not hs_code:  # Change the hs_code_chapter for heading or subheading variables as needed
                payload = (
                    f"priodKind=YEAR&priodFr=2024&priodTo=2024&langTpcd=ENG&ttwgTpcd=1000&selectPaging={page}&showPagingLine=10000&sortColumn=&sortOrder=&hsSgnGrpCol={hs_code_chapters}&"
                    f"hsSgnWhrCol={hs_code_chapters}&hsSgn={hs_code}&cntyNm={country_name}"
                )
            elif len(hs_code) == 2:  # Request a specific chapter
                payload = (
                    f"priodKind=YEAR&priodFr=2024&priodTo=2024&langTpcd=ENG&ttwgTpcd=1000&selectPaging={page}&showPagingLine=10000&sortColumn=&sortOrder=&hsSgnGrpCol={hs_code_chapters}&"
                    f"hsSgnWhrCol={hs_code_chapters}&hsSgn={hs_code}&cntyNm={country_name}"
                )
            elif len(hs_code) == 4:  # Request a specific heading
                payload = (
                    f"priodKind=YEAR&priodFr=2024&priodTo=2024&langTpcd=ENG&ttwgTpcd=1000&selectPaging={page}&showPagingLine=10000&sortColumn=&sortOrder=&hsSgnGrpCol={hs_code_headings}&"
                    f"hsSgnWhrCol={hs_code_headings}&hsSgn={hs_code}&cntyNm={country_name}"
                )
            elif len(hs_code) == 6:  # Request a specific subheading
                payload = (
                    f"priodKind=YEAR&priodFr=2024&priodTo=2024&langTpcd=ENG&ttwgTpcd=1000&selectPaging={page}&showPagingLine=10000&sortColumn=&sortOrder=&hsSgnGrpCol={hs_code_subheadings}&"
                    f"hsSgnWhrCol={hs_code_subheadings}&hsSgn={hs_code}&cntyNm={country_name}"
                )
            else:
                raise ValueError("The HS code must be 2, 4 or 6 digits!")

            task = asyncio.create_task(fetch(session, url, payload, page))  # Creates a task for a page, which makes a request to the website and gets the result as JSON
            tasks.append(task)  # Stores the task in the list, as it will be executed later all at once.

            if len(tasks) >= batch_size:  # Limit the number of concurrent tasks in batches, change the batch size as needed
                batch_results = await asyncio.gather(*tasks)  # Performs all tasks at the same time, getting the response from all pages at once
                valid_results = [data for result in batch_results for data in result["items"][1:] if result and "items" in result and result["items"]]  # Get only valid values
                results.extend(valid_results)  # stores valid values in total results
                print(f"Batch {batch_number} with {len(tasks)} pages: {len(valid_results)} records collected. Total of {page} pages processed and {len(results)} records collected")
                batch_number += 1
                tasks = []  # Empty the list, indicating that all tasks have been completed
                # Checks if the result of any page has no data, indicating that there are no more pages to be scraped. And then ends the loop
                if any(not result or "items" not in result or not result["items"] for result in batch_results):
                    print("There are no more data to collect.")
                    break
            page += 1  # Go to the next page

    # If data was scraped, then save it to a CSV
    if valid_results:
        scrape_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")  # The date of scraping
        filename = argv[1]  # The file name must be entered on the command line when executing the script.
        columns = [
            "priodTitle",
            "cntyEnglNm",
            "englPrlstNm",
            "expTtwg",
            "expUsdAmt",
            "impTtwg",
            "impUsdAmt",
            "cmtrBlncAmt",
        ]  # Columns that need to be extracted

        scraped_data = pd.DataFrame(valid_results, columns=columns)  # Convert the list to a dataframe
        scraped_data.columns = ["Year", "Country", "Goods", "ExportWeightTon", "ExportValueKUSD", "ImportWeightTon", "ImportValueKUSD", "BalanceOfTradeKUSD"]  # Rename the columns
        scraped_data.insert(0, "ScrapeDatetime", scrape_datetime)  # Insert the scrape datetime column
        scraped_data.to_csv(f"data/{filename}.csv", encoding="utf-8", lineterminator="\n", quotechar='"', quoting=csv.QUOTE_ALL, index=False)  # Save the dataframe to a csv file?

        print(f"Data saved in data/{filename}.csv")
    else:
        print("No data was collected.")


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    time_different = time.time() - start_time
    print(f"Scraping time: {time_different} seconds")
