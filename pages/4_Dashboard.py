from dependencies import *

# Load your pre-trained models
model1 = joblib.load("./model/XGboost_Model.pkl")
model2 = joblib.load("./model/LGB_Model.pkl")
model3 = joblib.load("./model/ran_for_reg_Model.pkl")
model4 = joblib.load("./model/grad_bos_reg_Model.pkl")

# Load your dataset (replace with your dataset file)
df = pd.read_csv('./data/testing.csv')

# st.write(df.shape)
# Create a Streamlit title and selection box for models
st.title("Actual vs Predicted Production")
selected_model = st.selectbox("Select a model:", ["XGBOOST", "LightGBM", "Random Forest Regressor", "Gradient Boosting"])

number_of_records = st.number_input("Select number of records", value=20)
df = df.head(number_of_records)

# Define a function to make predictions and return a DataFrame
def predict_and_get_df(selected_model):
    if selected_model == "XGBOOST":
        model = model1
    elif selected_model == "LightGBM":
        model = model2
    elif selected_model == "Random Forest Regressor":
        model = model3
    elif selected_model == "Gradient Boosting":
        model = model4
    else:
        st.warning("Please select a model.")
        return None
    
    X = df.drop('production', axis=1)
    y = df['production']
    predictions = model.predict(X)
    data = {'Actual': y, 'Predicted': predictions}
    return pd.DataFrame(data)

# Create buttons for DataFrame and Graph
show_df = st.checkbox("Show DataFrame")
show_graph = st.checkbox("Show Graph")
# show_parameters = st.checkbox("Show Parameters")

# Display results based on user choices
if show_df:
    # st.write(f"## Model: {selected_model})")
    df_to_show = predict_and_get_df(selected_model)
    if df_to_show is not None:
        st.write(df_to_show)


if show_graph:
    df_for_graph = predict_and_get_df(selected_model)
    if df_for_graph is not None:
        fig = px.line(df_for_graph, x=df_for_graph.index, y=['Actual', 'Predicted'],
                      labels={'index': 'Number of Records', 'value': 'Value in tons'}, title=f'Actual vs Predicted Production')
        
        # Customize the line colors
        fig.update_traces(line=dict(color='blue'), selector=dict(name='Actual'))
        fig.update_traces(line=dict(color='red'), selector=dict(name='Predicted'))
        
        st.plotly_chart(fig)
