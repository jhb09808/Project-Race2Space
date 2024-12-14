import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_country_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []

    table = soup.find('table')
    if table:
        rows = table.find_all('tr')
        print(f"Total Rows Found: {len(rows)}")  # Debug: Print number of rows
        for row in rows[1:]:  # Skip the header row
            cols = row.find_all('td')
            print(f"Row columns: {len(cols)}")  # Debug: Print number of columns
            if len(cols) >= 14:  # Ensure there are enough columns
                state_org = cols[3].text.strip()  # "State/Organization" column
                name_of_object = cols[2].text.strip()  # "Name of Space Object" column
                print(f"Extracted - State/Organization: {state_org}, Name of Space Object: {name_of_object}")  # Debug: Print extracted values
                if state_org and name_of_object:
                    data.append({'Country': state_org, 'Name of Space Object': name_of_object})
            else:
                print(f"Row has insufficient columns: {len(cols)}")  # Debug: Print insufficient columns
    else:
        print("No table found")  # Debug: Print if no table is found

    return data

def scrape_unoosa_data():
    urls = {
        "Algeria": "https://www.unoosa.org/oosa/osoindex/search-ng.jspx?lf_id=#?c=%7B%22filters%22:%5B%7B%22fieldName%22:%22en%23object.launch.stateOrganization_s%22,%22value%22:%22Algeria%22%7D%5D,%22sortings%22:%5B%7B%22fieldName%22:%22object.launch.dateOfLaunch_s1%22,%22dir%22:%22desc%22%7D,%7B%22fieldName%22:%22object.nameOfSpaceObjectIno_s1%22,%22dir%22:%22asc%22%7D%5D,%22match%22:null%7D",
        "Angola": "https://www.unoosa.org/oosa/osoindex/search-ng.jspx?lf_id=#?c=%7B%22filters%22:%5B%7B%22fieldName%22:%22en%23object.launch.stateOrganization_s%22,%22value%22:%22Angola%22%7D%5D,%22sortings%22:%5B%7B%22fieldName%22:%22object.launch.dateOfLaunch_s1%22,%22dir%22:%22desc%22%7D,%7B%22fieldName%22:%22object.nameOfSpaceObjectIno_s1%22,%22dir%22:%22asc%22%7D%5D,%22match%22:null%7D",
        "Argentina": "https://www.unoosa.org/oosa/osoindex/search-ng.jspx?lf_id=#?c=%7B%22filters%22:%5B%7B%22fieldName%22:%22en%23object.launch.stateOrganization_s%22,%22value%22:%22Argentina%22%7D%5D,%22sortings%22:%5B%7B%22fieldName%22:%22object.launch.dateOfLaunch_s1%22,%22dir%22:%22desc%22%7D,%7B%22fieldName%22:%22object.nameOfSpaceObjectIno_s1%22,%22dir%22:%22asc%22%7D%5D,%22match%22:null%7D"
    }

    all_data = []
    for country, url in urls.items():
        print(f"Processing {country}: {url}")  # Debug: Print current country and URL
        country_data = scrape_country_data(url)
        all_data.extend(country_data)

    # Convert the list to a DataFrame
    df = pd.DataFrame(all_data)

    # Debug: Print DataFrame before grouping
    print("DataFrame before grouping:", df)

    if 'Country' in df.columns:
        df_grouped = df.groupby('Country').size().reset_index(name='Objects Launched')
    else:
        print("KeyError: 'Country' column not found in the DataFrame")
        return pd.DataFrame(columns=['Country', 'Objects Launched'])

    # Debug: Print grouped DataFrame
    print("Grouped DataFrame:", df_grouped)

    return df_grouped

def main():
    data = scrape_unoosa_data()
    print(data)

if __name__ == '__main__':
    main()
