# End_to_End-Car-Price-Prediction-Project

An end-to-end, containerized, web-based application that predicts the resale price of a car based on various features provided by the user. The project leverages a machine learning model (Random Forest) trained on car resale data and integrates it with a Flask-based user interface for seamless interaction. The entire application is containerized using Docker, making it highly portable and easy to deploy across different environments. Version control and collaboration were managed through Git to ensure a streamlined development process.

---

## **Features**
- Predicts the resale price of a car based on:
  - Present Price
  - Kilometers Driven
  - Number of Previous Owners
  - Year of Manufacture
  - Fuel Type (Petrol/Diesel)
  - Seller Type (Dealer/Individual)
  - Transmission Type (Manual/Automatic)
- Provides a user-friendly web interface for input and prediction.
- Containerized using Docker for easy deployment.

---

## **Technologies Used**
### **Frontend:**
- **HTML**
  - For creating the user interface.
- **Bootstrap**
  - For responsive and visually appealing design.

### **Backend:**
- **Flask**
  - To build the web application and handle HTTP requests.
- **Python**
  - For scripting and integrating the machine learning model.
- **scikit-learn**
  - For building and loading the machine learning model.

### **Model Development:**
- **Random Forest Regressor**
  - Used for predicting the car price with high accuracy.
- **NumPy**
  - For numerical computations and input feature processing.

### **DevOps & Deployment:**
- **Docker**
  - Containerized the application for consistent development and deployment environments.
- **Docker Compose**
  - Simplified multi-container application setup.
- **Git**
  - For version control and collaboration.

---

## **Skills Highlighted**
- Machine Learning Model Development
- End-to-End Web Application Development
- Data Preprocessing and Feature Engineering
- Docker Containerization and Deployment
- Dependency Management and Version Control

---

## **Project Structure**
```plaintext
car-price-prediction/
├── Dockerfile             # Docker configuration for containerizing the app
├── docker-compose.yaml    # Docker Compose setup for the app
├── car price prediction.ipynb  # Data preprocessing, feature engineering, and model deployment
├── app.py                 # Flask backend for the application
├── RF_model.pkl           # Pre-trained Random Forest model
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Frontend HTML file
└── README.md              # Project documentation

