from dependencies import *



st.write("#### Input Parameter for Oil Production")

# Define default values
default_values = {
    "md (ft)": 1.914800e+04,
    "tvd (ft)": 6.443000e+03,
    "date on production": 1.519862e+09,
    "footage lateral length": 1.196600e+04,
    "porpoise count": 1.200000e+01,
    "shale footage": 1.093000e+03,
    "acoustic impedance": 3.012320e+04,
    "porosity": 2.000000e-02,
    "poisson ratio": 3.400000e-01,
    "vcl": 4.200000e-01,
    "p-velocity": 1.359223e+04,
    "youngs modulus": 3.082000e+01,
    "isip": 4.149000e+03,
    "breakdown pressure": 7.365949e+03,
    "total number of stages": 5.600000e+01,
    "proppant volume": 2.156879e+07,
    "proppant fluid ratio": 1.230000e+00,
    "total_proppant_volume": 1.207852e+09,
    "production_rate": 4.692418e-01
}


col1, col2, col3, col4 = st.columns(4)
columns = [col1, col2, col3, col4]

# Create input widgets for each parameter
user_input = {}
for i, (param, default_value) in enumerate(default_values.items()):
    with columns[i % 4]:
        user_input[param] = st.number_input(param, value=default_value, step=0.01, format="%.2f")

confirmed = st.checkbox("Confirm Input")


# Display the user-inputted values after confirmation
if confirmed:
    
    st.write(user_input)
    
    
test_input= np.array(list(user_input.values()),ndmin=2)
#st.write(test_input)
   

import joblib


# Load your pre-trained model
model1 = joblib.load("./model/XGboost_Model.pkl")
model2=joblib.load("./model/LGB_Model.pkl")
model3=joblib.load("./model/ran_for_reg_Model.pkl")
model4=joblib.load("./model/grad_bos_reg_Model.pkl")
st.title("Oil Production Prediction with Different Models")
selected_model = st.selectbox("Select a model:", 
                              ["XgBOOST","LightGBM","Random Forest Regresssor","Gradient Boosting"])

if selected_model == "XgBOOST":
    prediction = model1.predict(test_input)
elif selected_model == "LightGBM":
    prediction = model2.predict(test_input)
elif selected_model == "Random Forest Regresssor":
    prediction =model3. predict(test_input)
elif selected_model == "Gradient Boosting":
    prediction = model4.predict(test_input)

# Display the prediction
st.write(f"Prediction of Oil in tonne: {np.round(prediction[0], 2)}")