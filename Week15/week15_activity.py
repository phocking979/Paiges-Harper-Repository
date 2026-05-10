import requests
import json
import unittest
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

# the API client

class WikiPageviewClient:
    """
    handles communication with the Wikimedia Analytics API
    the AQS (Analytics Query Service) provides pageview data for Wikipedia articles
    """
    BASE_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access"
    
    USER_AGENT = "AnalyticsAssignmentBot/1.0 "

    def get_top_articles(self, year, month):
        """
        fetches the top 1000 articles for a single specific month
        
        args:
            year (int): the calendar year (e.g., 2024)
            month (int): the month number (1-12)
            
        returns:
            dict: the JSON response from the API or None if the request fails
        """
        # construct the specific endpoint for the requested month using the all-days option
        # used :02d to ensure the month is two digits
        endpoint = f"{self.BASE_URL}/{year}/{month:02d}/all-days"
        
        headers = {"User-Agent": self.USER_AGENT}
        
        response = requests.get(endpoint, headers=headers)
        
        # 200 is the standard HTTP success code
        if response.status_code == 200:
            return response.json()
        
        # if the API returns an error (like 404 for data not yet available), return None
        return None

# data processing and conversion

def dict_to_xml(data_dict):
    """
    converts the Python dictionary (JSON structure) into a formatted XML string
    
    args:
        data_dict (dict): the dictionary containing 12 months of article data
        
    returns:
        str: a XML string representing the data
    """
    root = ET.Element("WikiAnalytics")
    
    # iterate through each month in our collected data
    for period, articles in data_dict.items():
        month_el = ET.SubElement(root, "Month", period=period)
        
        # iterate through the top 1000 articles for that month
        for rank, art in enumerate(articles, 1):
            art_el = ET.SubElement(month_el, "Article", rank=str(rank))
            
            ET.SubElement(art_el, "Title").text = art.get('article')
            ET.SubElement(art_el, "Views").text = str(art.get('views'))
    
    # convert the tree to a string and return it
    return ET.tostring(root, encoding='unicode')

def run_main():
    """
    the main execution loop, it manages the 12 separate API requests,
    compiles the data, and saves it to both JSON and XML formats
    """
    client = WikiPageviewClient()
    all_monthly_results = {}
    
    # start from the current date and move backward
    now = datetime.now()
    
    print("Starting data retrieval for the previous 12 months")
    
    for i in range(1, 13):
        # calculate the month to request, subtract roughly i months
        # replace day=1 to avoid issues with shorter months like February
        target_date = (now.replace(day=1) - timedelta(days=i*28)).replace(day=1)
        year, month = target_date.year, target_date.month
        
        print(f"Request {i}/12: Fetching data for {year}-{month:02d}")
        
        # call the API for this specific month
        data = client.get_top_articles(year, month)
        # sometimes the Wikimedia API may not have data available for a specific month or the request may temporarily fail
        if data and 'items' in data:
            # the API returns a list, the first item contains the articles list
            # slice the list [:1000] to ensure that it only gets the top 1000
            top_1000 = data['items'][0]['articles'][:1000]
            all_monthly_results[f"{year}-{month:02d}"] = top_1000
        else:
            print(f"Warning: Could not retrieve data for {year}-{month:02d}")

    # save JSON output 
    with open("pageviews_report.json", "w") as json_file:
        json.dump(all_monthly_results, json_file, indent=4)
    print("Successfully created 'pageviews_report.json'")
    
    # save XML output
    xml_output = dict_to_xml(all_monthly_results)
    with open("pageviews_report.xml", "w") as xml_file:
        xml_file.write(xml_output)
    print("Successfully created 'pageviews_report.xml'")

# testing

class TestWikiApplication(unittest.TestCase):
    """
    unit tests to verify that the code behaves correctly without 
    actually needing to hit the live Wikimedia API every time
    """
    @patch('requests.get')
    def test_successful_api_retrieval(self, mock_get):
        #tests that a valid API response is correctly parsed
        # setup a fake response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "items": [{"articles": [{"article": "Python_Programming", "views": 1000}]}]
        }
        mock_get.return_value = mock_response

        client = WikiPageviewClient()
        result = client.get_top_articles(2024, 1)
        
        self.assertIsNotNone(result)
        self.assertEqual(result['items'][0]['articles'][0]['article'], "Python_Programming")

    def test_xml_generation_logic(self):
        #tests that our dictionary-to-XML converter produces the right structure
        sample_data = {"2024-01": [{"article": "Test", "views": 10}]}
        xml_str = dict_to_xml(sample_data)
        
        self.assertIn('<Month period="2024-01">', xml_str)
        self.assertIn('<Title>Test</Title>', xml_str)

# program entry point

if __name__ == "__main__":
    import sys
    # check if the user passed 'test' as a command-line argument
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        sys.argv.pop()
        unittest.main()
    else:
        # otherwise, run the main collection and file creation logic
        run_main()