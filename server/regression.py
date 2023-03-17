import numpy as np
from flask import Flask, request, jsonify
import pickle
import os

# Get path to file dynamically
WD = os.path.dirname('')
print(WD)

# generate flask app object
app = Flask(__name__)
# Read pickle regression model
file_path = os.path.join(WD, 'models/pickled/model.pkl')
with open(file_path, 'rb') as f:
    model = pickle.load(f)

print(model)

# Create endpoint /predict-salary
@app.route('/predict-salary', methods=['POST', 'GET'])
def predict():
    # Get 'exp' parameter from URL and convert to integer
    exp = int(request.args.get('exp'))
    # get argument parameter from endpoint
    data = request.args
    # Predict with regression model
    prediction = model.predict([[np.array(eval(data['exp']))]])
     # Format prediction with dollar sign and thousand separator
    formatted_prediction = "$" + format(prediction[0], ",.2f")
    # Return estimate salary message
    return f"From {exp} years of experience estimated salary is {formatted_prediction} per year."
    # # Get first index
    # output = formatted_prediction
    # # Return prediction result
    # return jsonify(output)

# Run endpoint server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
