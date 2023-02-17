import requests # library to import the source code of a website (for web scraping)
from pprint import pprint
from selectorlib import Extractor

# Web Scraping step by

headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

r = requests.get("https://www.timeanddate.com/weather/italy/rome", # creates a response class object
                 headers = headers) # Making website believe we are a browser (some websites block Python)
c = r.content # importing the page source code (the content of the page), useful to extract objects like PDFs (bite type)
t = r.text # better option to extract numbers or text (string type)

pp_c = pprint(c) # process the content to make it more readable and so Python can manipulate it afterwards
pp_t = pprint(t)

# Now the Webscraping part starts (extracting a value from the webpage)

extractor = Extractor.from_yaml_file("temperature.yaml") # Constructor Method of the Extractor Class

# In the yaml file, the full XPath of the website element (the temperature) needs to be pasted
# However, to copy the right XPath, we need to disable JavaScript (and only leave enabled HTML):
#   1- go on the Inspect Window, press Ctr+Shift+P
#   2- write Debugger, click on "Disable JavaScript"
#   3- Reload the page and copy the full XPath (it will have changed a bit) - use that one

raw_result = extractor.extract(t) # the raw result is a dictionary
# print(raw_result)

result = float(raw_result["temp"].replace("\xa0°C", "")) # extracting and converting the actual number
print(result)