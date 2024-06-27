import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape laptop data from laptop.lk
def scrape_laptop_data():
    base_url = 'https://www.laptop.lk/index.php/page/'
    end_url = '/?s&product_cat=laptops&post_type=product'
    laptop_data = []

    # Loop through multiple pages 
    for page in range(1, 5):  
        url = base_url + str(page) + end_url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(url)
        # Find the HTML elements containing the laptop data
        laptops = soup.find_all('li')  

        for laptop in laptops:
            model = laptop.find('h2', class_='woocommerce-loop-product__title')
            price = laptop.find('span', class_='woocommerce-Price-amount amount')
            specs = laptop.find('div', class_='product-short-description')
            
            # Only proceed if model and price elements are found
            if model and price:
                model_text = model.text.strip()
                price_text = price.text.strip()
                
                #store the value from website
                if specs:
                    specs_text = specs.text.strip()
                    spec_list = specs_text.split('\n')
                    ram = next((spec for spec in spec_list if 'RAM' in spec), 'N/A')
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

    #create dataframe
    df = pd.DataFrame(laptop_data, columns=['Model', 'Price', 'RAM', 'Generation', 'Processor Type', 'Hard Drive Type', 'Hard Drive Size'])
    return df

# Scrape and save data
laptop_data_df = scrape_laptop_data()
file_path = 'laptop_prices_laptop_lk.csv'
laptop_data_df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")
