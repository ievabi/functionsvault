from functionsvault.scraping import scrape_html
def test_scrape_html():
    url='https://www.google.com/'
    soup = scrape_html(url)
    assert len(soup) != 0
