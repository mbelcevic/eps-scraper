import requests
from bs4 import BeautifulSoup

# URL of the target webpage
url = "https://elektrodistribucija.rs/planirana-iskljucenja-beograd/Dan_1_Iskljucenja.htm"

# Send a GET request to fetch the page content
headers = {"User-Agent": "Mozilla/5.0"}  # Set a user-agent to avoid being blocked
response = requests.get(url, headers=headers)

# Try to detect and set the correct encoding
response.encoding = response.apparent_encoding  # Automatically detects encoding

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Ask for a keyword
    keyword = input("Enter the keyword to search for: ").strip().capitalize()
    
    # Extract relevant information (modify based on page structure)
    data = []
    for row in soup.find_all("tr"):  # Assuming data is in table rows
        columns = row.find_all("td")
        if columns:
            row_data = [col.text.strip() for col in columns]
            if any(keyword in col for col in row_data):  # Check if keyword exists in any column
                data.append(row_data)
    
    # Print extracted data that contains the keyword
    if data:
        for item in data:
            print(item)
    else:
        print("No matches found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
