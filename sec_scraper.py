from sec_edgar_downloader import Downloader
import sec_parser as sp

# Initialize the downloader with your company name and email
dl = Downloader("Aditya Natham", "anatham3@gatech.edu")

# Download the latest 10-K filings for Apple Inc.
# The filings will be saved in the 'sec-edgar-filings' directory by default
ticker = "APPL"
dl.get("10-K", ticker, limit=3)

# Define the directory where the filings are saved
filings_dir = "sec-edgar-filings/" + ticker

# Function to parse and render filings
def parse_and_render_filing(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()
    elements = sp.Edgar10KParser().parse(html)
    parsed_output = sp.render(elements)
    return parsed_output

# Iterate through the downloaded filings and parse them
import os

for root, dirs, files in os.walk(filings_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            parsed_output = parse_and_render_filing(file_path)
            print(parsed_output)
