import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape laptop data from SellX
def scrape_laptop_data():
    base_url = 'https://www.sellx.lk/products.php?ci=MQ=='
    
    laptop_data = []

    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(url)
    # Find the HTML elements containing the laptop data
    
    laptops= soup.find_all('div', class_='modal-dialog modal-lg')
    

    for laptop in laptops:
        model = laptop.find('h5', class_='modal-title text-uppercase')
        price = laptop.find('span', class_='float-left tx8')
        specs = laptop.find('div', class_='tx7')
        
        if model and price:
            model_text = model.text.strip()
            price_text = price.text.strip()

            if specs:
                table = specs.find('table') #get the table from website
                rows = []
                
                if table :
                    cells = table.find_all('td') # get the table data from table
                    if cells:
                        row = [cell.text.strip() for cell in cells]
                        rows.append(row)
                        #seperate the values
                        ram = rows[0][5] if rows[0][5] else 'N/A'
                        generation = rows[0][3] if rows[0][3] else 'N/A'
                        processor_type = rows[0][3] if rows[0][3] else 'N/A'
                        hard_drive_type = rows[0][7] if rows[0][7] else 'N/A'
                        hard_drive_size = rows[0][7] if rows[0][7] else 'N/A'
                        del rows
                    else:
                        print('Not work !')
                
                else:
                    print('table is empty')
            else:
                    # Default values if specs are not found
                ram = 'N/A'
                generation = 'N/A'
                processor_type = 'N/A'
                hard_drive_type = 'N/A'
                hard_drive_size = 'N/A'
                

            laptop_data.append([ #save the data 
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
    
    df = pd.DataFrame(laptop_data, columns=['Model', 'Price', 'RAM', 'Generation', 'Processor Type', 'Hard Drive Type', 'Hard Drive Size'])
    return df

# Scrape and save data
laptop_data_df = scrape_laptop_data()
file_path = 'laptop_prices_SellX.csv'
laptop_data_df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")
