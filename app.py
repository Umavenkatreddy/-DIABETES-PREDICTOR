from flask import Flask, request, render_template
import pickle
import psycopg2
app = Flask(__name__)  # initialising flask app

model = pickle.load(open('f_model', 'rb')) # load ml model

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        Pregnacies = float(request.form['Pregnacies'])
        Glucose = float(request.form['Glucose'])
        Skinthickness= float(request.form['Skinthickness'])
        blood_pressure = float(request.form['bloodpressure'])
        insulin = float(request.form['insulin'])
        BMI = float(request.form['bmi'])
        diabecticspedreefunction = float(request.form['diabecticspedreefunction'])
        age = float(request.form['age'])

        #model = pickle.load(open('model', 'rb'))  # load ml model
        prediction = model.predict([[Pregnacies, Glucose, Skinthickness, blood_pressure, insulin, BMI, diabecticspedreefunction,age]])
        output = round(prediction[0], 2)
        
        Pregnacies = float(request.form['Pregnacies'])
    Glucose = float(request.form['Glucose'])
    Skinthickness= float(request.form['Skinthickness'])
    blood_pressure = float(request.form['bloodpressure'])
    insulin = float(request.form['insulin'])
    BMI = float(request.form['bmi'])
    diabecticspedreefunction = float(request.form['diabecticspedreefunction'])
    age = float(request.form['age'])


    
    

   
    # Close the database connection
   
   

    return render_template('index.html', output="{}".format(output))


if __name__ == '__main__':
    app.run(debug=True)