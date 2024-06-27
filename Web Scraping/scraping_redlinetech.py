import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# Function to scrape laptop data from redlinetech
def scrape_laptop_data_():
    base_url = 'https://www.redlinetech.lk/product-category/laptops/gaming-laptops/page/'
    laptop_data = []

    # Loop through multiple pages 
    for page in range(1,4):  
        url = base_url + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(url)
        # Find the HTML elements containing the laptop data
        laptops = soup.find_all('div',class_='product-wrapper')  

        for laptop in laptops:
            href = laptop.find('a', class_='product-image-link')
            href_link = href.get('href')
            full_url = urljoin(url,href_link) # Combine two url
            #print(full_url)

            # Only proceed if model and price elements are found
            if full_url:
                response_ = requests.get(full_url)
                item = BeautifulSoup(response_.text, 'html.parser')
                model = item.find('div', class_='wd-product-brands')
                price = item.find('span', class_='screen-reader-text')
                specs = item.find('div', class_='woocommerce-product-details__short-description')
                
                if model and price :
                    model_text = model.text.strip()
                    price_text = price.text.strip()
                
                    if specs:
                        specs_text = specs.text.strip()
                        spec_list = specs_text.split('\n')
                        ram = next((spec for spec in spec_list if 'RAM' in spec or 'Ram' in spec or 'MHz' in spec), 'N/A')
                        generation = next((spec for spec in spec_list if 'Gen' in spec), 'N/A')
                        processor_type = next((spec for spec in spec_list if  'Processor'in spec or 'Core' in spec ), 'N/A')
                        hard_drive_type = next((spec for spec in spec_list if 'SSD' in spec or 'HDD' in spec or 'NVMe' in spec), 'N/A')
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
                print('URL is empty !')
   
    df = pd.DataFrame(laptop_data, columns=['Model', 'Price', 'RAM', 'Generation', 'Processor Type', 'Hard Drive Type', 'Hard Drive Size'])
    return df


# Scrape and save data
laptop_data_df = scrape_laptop_data_()

file_path = 'laptop_prices_redlinetech.csv'
laptop_data_df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")
