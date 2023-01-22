from bs4 import BeautifulSoup
import urllib.request
import re
import codecs
import os
import tkinter as tk
from tkinter import messagebox
from concurrent.futures import ThreadPoolExecutor


def process_txt_files():
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.endswith(".txt"):
            replace_spaces_with_newlines(filename)


def get_data(url):
    data = urllib.request.urlopen(url).read()
    page_content = data.decode("utf-8")
    soup = BeautifulSoup(page_content, "html.parser")
    return soup


def get_relevant_links(soup):
    lista = []
    items = soup.find_all("h3", class_="entry-title td-module-title")
    if items == None:
        return
    for item in items:
        lista.append(item.find("a").get("href"))

    return lista


def extract_pashto(string):
    pashto = """"""
    res = re.sub(" +", " ", string)
    for char in res:
        if re.search(r"[\u0080-\uFFFF]", char):
            pashto = pashto + char
        if char == " ":
            pashto = pashto + " "
        if char == "۔":
            pashto = pashto + char

    return pashto


def extract_pashto_from_links(links):
    pashto = """"""
    for link in links:
        soup = get_data(link)
        if soup != None:
            par = soup.find("div", class_="td-post-content tagdiv-type")
            if par != None:
                data = extract_pashto(str(par))
                if data != None and len(data) > 0:
                    pashto += data

    return pashto


def save_to_file(string, filename):
    with codecs.open(filename, "w", "utf-8") as f:
        f.write(string)


def replace_spaces_with_newlines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        file_contents = f.read()
    modified_contents = re.sub(" +", " ", file_contents)
    modified_contents = modified_contents.replace(" ", "\n")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(modified_contents)


def download_page(URL, page):
    # Selection file name based on URL
    url = URL + "/page/" + str(page) + "/"
    filename = "ds-p" + str(page) + ".txt"

    # Initializing Variables
    pashto = """"""
    links = []

    # Processing Data
    soup = get_data(url)
    links = get_relevant_links(soup)
    pashto = extract_pashto_from_links(links)
    save_to_file(pashto, filename)


def start_download():
    # Get the user's input from the Entry widgets
    url = url_entry.get()
    start_page = start_page_entry.get()
    end_page = end_page_entry.get()
    thread_count = thread_count_entry.get()

    # Perform input validation
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return
    if not start_page.isdigit() or not end_page.isdigit() or not thread_count.isdigit():
        messagebox.showerror("Error", "Start page, end page and thread count must be integers.")
        return
    if int(start_page) > int(end_page):
        messagebox.showerror("Error", "Start page must be smaller than end page.")
        return

    # Pass the user's input to your scraping function
    start = int(start_page)
    end = int(end_page)
    tcount = int(thread_count)
    with ThreadPoolExecutor(max_workers=tcount) as executor:
      for i in range(start, end):
          executor.submit(download_page, url, i)


# Create the main window
root = tk.Tk()
root.title("Pashto Data Scraper")

# Create the label and entry widgets for the URL
url_label = tk.Label(root, text="URL:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Create the start page Entry widget
start_page_label = tk.Label(root, text="Start page:")
start_page_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
start_page_entry = tk.Entry(root)
start_page_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the end page Entry widget
end_page_label = tk.Label(root, text="End page:")
end_page_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
end_page_entry = tk.Entry(root)
end_page_entry.grid(row=2, column=1, padx=10, pady=10)

# Create the thread count Entry widget
thread_count_label = tk.Label(root, text="Enter Max Threads to use:")
thread_count_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")
thread_count_entry = tk.Entry(root)
thread_count_entry.grid(row=3, column=1, padx=10, pady=10)

# Create the download button
download_button = tk.Button(root, text="Download", command=start_download)
download_button.grid(row=4, column=0, padx=10, pady=10)

# Create the process files button
process_button = tk.Button(root, text="Process Files", command=process_txt_files)
process_button.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()


'''
balochistan = "https://khybernews.tv/pu/%d8%a8%d9%84%d9%88%da%86%d8%b3%d8%aa%d8%a7%d9%86/"
afghanistan = "https://khybernews.tv/pu/%d8%a7%d9%81%d8%ba%d8%a7%d9%86%d8%b3%d8%aa%d8%a7%d9%86/"
nationalNews = "https://khybernews.tv/pu/%d9%82%d8%a7%d9%85%d9%89-%d8%ae%d8%a8%d8%b1%d9%88%d9%86%d9%87/"
kpkNews = "https://khybernews.tv/pu/%d8%ae%db%90%d8%a8%d8%b1%d9%be%da%9a%d8%aa%d9%88%d9%86%d8%ae%d9%88%d8%a7/"
'''