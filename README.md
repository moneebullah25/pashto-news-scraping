# Pashto News Scraping

This project is a tool for scraping Pashto news articles from the website [khybernews.tv](https://khybernews.tv/) and saving them to a text file. The tool allows the user to specify the starting and ending page of the news section they want to scrape, as well as the URL of the news section.

**Requirements**

- Python 3.x
- BeautifulSoup4
- urllib
- re
- tkinter (for GUI)
- concurrent.futures (for running multiple threads)

**How to Use**

1. Install the required libraries by running **pip install -r requirements.txt** in the command line.
1. Run the script using **python main.py**
1. A GUI will appear where you can select the URL of the news section you want to scrape, the starting and ending page of the news section, and a button to start the scraping process.
1. Press the "Start Download" button to begin scraping. The articles will be saved to a text file in the working directory.
1. Press the "Process Files" button to process the downloaded text files. The function will remove multiple spaces and replace them with new lines.

**Available URLs**

However you could pass any url from the khybernews.tv domain

- balochistan = "<https://khybernews.tv/pu/%d8%a8%d9%84%d9%88%da%86%d8%b3%d8%aa%d8%a7%d9%86/>"
- afghanistan = "<https://khybernews.tv/pu/%d8%a7%d9%81%d8%ba%d8%a7%d9%86%d8%b3%d8%aa%d8%a7%d9%86/>"
- nationalNews = "<https://khybernews.tv/pu/%d9%82%d8%a7%d9%85%d9%89-%d8%ae%d8%a8%d8%b1%d9%88%d9%86%d9%87/>"
- kpkNews = "<https://khybernews.tv/pu/%d8%ae%db%90%d8%a8%d8%b1%d9%be%da%9a%d8%aa%d9%88%d9%86%d8%ae%d9%88%d8%a7/>"

**Note**

The script uses **concurrent.futures** library to run multiple threads of the `get\_news function, which speeds up the scraping process. However, it is important to note that excessive use of threads may cause the website to block your IP or cause other issues. Use the tool responsibly and with caution.

- The script uses regular expressions to filter out Pashto characters from the scraped text. However, the script may not be able to catch all Pashto characters or may include some non-Pashto characters. It is recommended to manually check the downloaded text files for errors.
- The script also includes a function for processing the downloaded text files, which replaces multiple spaces with new lines. This function is useful for formatting the text for natural language processing tasks.
- The GUI is basic and is intended to provide a simple interface for the user. More advanced users may prefer to use the script through the command line.
- The script is for educational and research purposes only. Do not use the tool for any illegal or unethical purposes.

Overall, this project is intended to be a starting point for creating a Pashto dataset for natural language processing tasks and research. With some modifications and improvements, it can be used to scrape data from other websites as well.

