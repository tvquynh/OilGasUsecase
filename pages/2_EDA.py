from dependencies import *

# Load the Iris dataset (you can replace this with your own dataset)
data=pd.read_csv("./data/oil_gas_data.csv")

# Streamlit app title
st.title("Exploratory Data Analysis (EDA)")

# Sidebar with options
st.sidebar.title("Options")
show_data = st.sidebar.checkbox("Show Dataset", value=True)
selected_feature = st.sidebar.selectbox("Select a Feature for Analysis", data.columns)

# Show the dataset if selected
if show_data:
    st.write("## Oil-Gas Dataset")
    st.write(data)

# EDA Section
st.header("Exploratory Data Analysis")


# List of options
options = [ "Summary Statistics","Production Rate vs Proppant Volume","Average Production by Month","Average Well Spacing by Treatment Company"]
# Display radio buttons for selecting one option
selected_option = st.radio("Select one option:", options)

# Display the selected option
st.write("You selected:", selected_option)

if selected_option=="Summary Statistics":

    # st.write("### Summary Statistics")

    selected_options = st.multiselect("Select options:",data.columns, default=data.columns.tolist())

    st.write(data[selected_options].describe())



elif selected_option=="Production Rate vs Proppant Volume":
    fig = px.scatter(data, x='production', y='proppant volume', 
                 title="Production Rate vs Proppant Volume",
                 labels={'production': 'Production Rate', 'proppant volume': 'Proppant Volume'})
    
    st.plotly_chart(fig)


elif selected_option=="Average Production by Month":

    data['date on production'] = pd.to_datetime(data['date on production'],format='%m/%d/%Y')

    data['month'] = data['date on production'].dt.month
    # Group data by month and calculate the mean production for each month
    monthly_production = data.groupby('month')['production'].mean()
    fig = px.bar(
        x=monthly_production.index,
        y=monthly_production,
        labels={'x': 'Month', 'y': 'Average Production'},
        title="Average Production by Month",
    )

    fig.update_xaxes(tickvals=list(range(1, 13)), ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    fig.update_yaxes(title="Average Production")

    st.plotly_chart(fig)


elif selected_option=="Average Well Spacing by Treatment Company":
    
    fig = px.bar(
        data,
        x='treatment company',
        y='well spacing',
        title="Average Well Spacing by Treatment Company",
    )

    fig.update_xaxes(title="Treatment Company", tickangle=90)
    fig.update_yaxes(title="Average Well Spacing")

    st.plotly_chart(fig)