from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model
# model = pickle.load(open('/Users/santhoshreddy/Desktop/vscode/OnineProjects/End-to-End-Machine-Learning-Projects-master/CarPrice/RF_model.pkl', 'rb'))
model = pickle.load(open('RF_model.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    Present_Price = float(request.form['Present_Price'])
    Kms_Driven = float(request.form['Kms_Driven'])
    Owner = int(request.form['Owner'])
    Year = int(request.form['Year'])
    Fuel_Type_Diesel = int(request.form['Fuel_Type_Diesel'])
    Fuel_Type_Petrol = int(request.form['Fuel_Type_Petrol'])
    Seller_Type_Individual = int(request.form['Seller_Type_Individual'])
    Transmission_Mannual = int(request.form['Transmission_Mannual'])
    
    # Prepare the input data for the model
    features = np.array([[Present_Price, Kms_Driven, Owner, Year, Fuel_Type_Diesel,
                          Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
    
    # Make a prediction
    predicted_price = model.predict(features)[0]
    
    return render_template('index.html', prediction_text=f"You can sell the car at: {predicted_price:.2f} price.")

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')
