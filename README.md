# SI507-FinalProj

### Required Packages:
pandas, numpy, requests, json, webbrowser, BeautifulSoup, re ; also need to pip install tabulate

### Data Scraping
To scrape the data, first run movie list scraping.py, and you'll get movie_list.csv accordingly. And then run get movie info (API).py. For the API part, you'll need to ask for an API key from https://www.omdbapi.com/apikey.aspx, and stored as API_KEY to run the program. You'll get raw_movie_info.csv after running this program.

### Data to tree
To construct the data into a tree structure, run data_to_tree.py, and you can get data_tree_struct.json.

### Main program
Since I've put all the files that you'll get in the above steps in the resporitory, it's completely ok for you to directly run the main program.<br/>
Open your terminal, go to the directory you stored this project and enter "python3 main_program.py" and you can see the program running. You'll see instructions on how to interact with this program.
