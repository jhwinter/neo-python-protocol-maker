# neo-python-protocol-maker

One click (if you do it right) to update `protocol.json`

## Requirements:
1. python 3
2. selenium
3. apscheduler

### Additional things
1. Firefox or Chrome browser 
2. [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) if using Chrome
3. [geckodriver](https://github.com/mozilla/geckodriver/releases) if using Firefox. If there is any issue, I recommend reading [this](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path)

## Getting Started
### 1. Download the package

### 2. Install the dependencies
`pip install -r requirements.txt`

### 3. Run the Package
Run the script `python make_protocol.py`

### 4. That's it!
You can run neo-python normally. It should automatically connect to live nodes and reconfigure itself to run on the best nodes every day.
