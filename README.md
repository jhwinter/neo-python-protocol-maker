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
### 1. Clone/Download neo-python and this package
`git clone https://github.com/CityOfZion/neo-python.git` 

and in a neighboring directory:

`git clone https://github.com/jonathanhwinter/neo-cli-protocol-maker.git`

### 2. Install the dependencies
```
# create virtual environment and activate

python3.6 -m venv venv # this can also be python3 -m venv venv depending on your environment
source venv/bin/activate

# install the package in an editable form
(venv) pip install -e .
```

```
cd ../neo-cli-protocol-maker
pip install -r requirements.txt
```
### Note: 
I added in the default file path for protocol.mainnet.json for testing. You just have to change the file path 
in make_protocol.py if you want to test against it. 
### 3. Run the Package
Run the script `python make_protocol.py`

### 4. That's it!
You can run neo-python normally. It should automatically connect to live nodes and reconfigure itself to run on the best nodes every day.
