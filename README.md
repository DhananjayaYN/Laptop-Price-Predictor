
# 💻 Laptop Price Predictor

An end-to-end machine learning web application that predicts laptop prices based on user-specified hardware and software configurations. This project encompasses data collection through web scraping, data preprocessing, model training, and a user-friendly frontend interface built with Flask, HTML, CSS, JavaScript, and Three.js.

---

## 🚀 Features

- **Real-World Data Collection**: Utilizes BeautifulSoup to scrape up-to-date laptop specifications and prices from e-commerce websites.
- **Data Preprocessing**: Cleans and transforms raw data, handling missing values, encoding categorical variables, and feature engineering.
- **Model Training**: Implements machine learning algorithms to predict laptop prices based on various features.
- **Interactive Frontend**: Provides a responsive user interface for inputting laptop specifications and viewing predicted prices.
- **3D Visualization**: Incorporates Three.js for dynamic and interactive 3D representations of laptop models.

---

## 🧰 Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript, Three.js
- **Data Collection**: BeautifulSoup
- **Machine Learning**: scikit-learn, pandas, NumPy

---

## 📁 Project Structure

```
├── Web Scraping/
│   └── scrape_data.py
├── Model/
│   ├── preprocess_data.py
│   ├── train_model.py
│   └── model.pkl
├── Interface/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   └── index.html
│   └── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DhananjayaYN/Laptop-Price-Predictor.git
   cd Laptop-Price-Predictor
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   cd Interface
   python app.py
   ```

5. **Access the Web Interface**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 📊 Usage

1. Navigate to the web interface.
2. Input the desired laptop specifications, including brand, processor, RAM, storage, and other relevant features.
3. Click on the "Predict Price" button.
4. View the predicted price along with a 3D visualization of the laptop.

---

## 🧪 Model Details

- **Algorithm Used**: Random Forest Regressor (or specify the algorithm you've used)
- **Features Considered**:
  - Brand
  - Processor Type
  - RAM Size
  - Storage Capacity
  - Operating System

---

## 📌 Future Enhancements

- Integrate more advanced machine learning models for improved accuracy.
- Expand the dataset to include more diverse laptop models and brands.
- Implement user authentication for personalized experiences.
- Deploy the application on cloud platforms for broader accessibility.


---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
