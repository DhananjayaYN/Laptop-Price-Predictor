import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# Function to scrape laptop data from sense.lk
def scrape_laptop_data():
    url = 'https://www.sense.lk/shop?selected_category=43-2&selected_brand=&min_price=0&max_price=3447000&sort_order=&selected_filter_params='
    
    laptop_data = []
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the HTML elements containing the laptop data
    laptops = soup.find_all('div', class_='col-lg-3')
      

    for laptop in laptops:
        tag = laptop.find('a')
        
        if tag:
            href = tag.get('href')
            
            link = urljoin(url,href)
            #print(link)
            response_ = requests.get(link)
            #print(response_)
            soup_ = BeautifulSoup(response_.text, 'html.parser')
            content = soup_.find('div', class_='col-md-7 pt-lg-0 pt-sm-0 pt-4')
            #print(content)

            print('===================')
            if content:
                model = laptop.find('a', class_='p-mediam poppins-font subcat-title')
                price = content.find('h3', class_='p-large poppins-font fw-bolder pb-2 text-dark')
                specs = content.find('span', class_='poppins-font text-secondary p-small')
            
                # Only proceed if model and price elements are found
                if model and price:
                    model_text = model.text.strip()
                    price_text = price.text.strip()
                    
                    #store the value from website
                    if specs:
                        specs_text = specs.text.strip()
                        spec_list = specs_text.split('\n')
                        ram = next((spec for spec in spec_list if 'RAM' in spec or 'DDR' in spec), 'N/A')
                        generation = next((spec for spec in spec_list if 'Gen' in spec), 'N/A')
                        processor_type = next((spec for spec in spec_list if  'Processor' in spec), 'N/A')
                        hard_drive_type = next((spec for spec in spec_list if 'SSD' in spec or 'HDD' in spec), 'N/A')
                        hard_drive_size = next((spec for spec in spec_list if 'NVM' in spec or 'TB' in spec), 'N/A')
                    else:
                    # Default values if specs are not found
                        ram = 'N/A'
                        generation = 'N/A'
                        processor_type = 'N/A'
                        hard_drive_type = 'N/A'
                        hard_drive_size = 'N/A'
                        #print('not found')

                    laptop_data.append([
                        model_text, 
                        price_text, 
                        ram, 
                        generation, 
                        processor_type, 
                        hard_drive_type, 
                        hard_drive_size
                    ])
                else:
                    # Debug: Print which element is missing
                    if not model:
                        print("Model element not found")
                    if not price:
                        print("Price element not found")
            else:
                print('content is empty !')
        else:
            print('link is not work.')
    #create dataframe
    df = pd.DataFrame(laptop_data, columns=['Model', 'Price', 'RAM', 'Generation', 'Processor Type', 'Hard Drive Type', 'Hard Drive Size'])
    return df

# Scrape and save data
laptop_data_df = scrape_laptop_data()
file_path = 'laptop_prices_sense_lk.csv'
laptop_data_df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")
