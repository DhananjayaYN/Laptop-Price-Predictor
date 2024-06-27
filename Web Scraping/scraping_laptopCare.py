import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# Function to scrape laptop data from laptop.lk
def scrape_laptop_data():
    base_url = ['https://laptopcare.lk/product-category/laptops/','https://laptopcare.lk/product-category/laptops/page/2/']
    
    laptop_data = []

    # Loop through multiple pages 
    for page in base_url:  
        url = page
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the HTML elements containing the laptop data
        laptops = soup.find_all('div', class_='product-outer product-item__outer')  

        for laptop in laptops:
            link = laptop.find('a', class_ ='woocommerce-LoopProduct-link woocommerce-loop-product__link')
            href = link.get('href')
            full_url = urljoin(url,href)
            
            if full_url:
                response_ = requests.get(full_url)
                soup_ = BeautifulSoup(response_.text, 'html.parser')
                contend = soup_.find('div', class_='summary entry-summary')

                model = contend.find('h1', class_='product_title entry-title')
                price = contend.find('span', class_='woocommerce-Price-amount amount')
                specs = contend.find('div', class_='woocommerce-product-details__short-description')

            
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
                        processor_type = next((spec for spec in spec_list if 'Intel' in spec or 'AMD' in spec), 'N/A')
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
                print('Url error !')

    #create dataframe
    df = pd.DataFrame(laptop_data, columns=['Model', 'Price', 'RAM', 'Generation', 'Processor Type', 'Hard Drive Type', 'Hard Drive Size'])
    return df

# Scrape and save data
laptop_data_df = scrape_laptop_data()
file_path = 'laptop_prices_laptopCare.csv'
laptop_data_df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")
