import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def scrape_html(url:str):
    '''
    Returns a scrapped html page for further analysis
    Input: html address
    Output: parsed html text
    '''
    url = url

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup
