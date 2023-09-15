from dependencies import *


st.title("Oil & Gas Analytics Platform")

st.subheader('About')

st.write("At Oil & Gas Analytix, our expertise lies in the art of turning raw data into actionable intelligence. With a sophisticated blend of Exploratory Data Analysis (EDA) and advanced simulation techniques, we illuminate the complex dynamics of the oil and gas industry. Our solutions don't just stop at numbers; we craft insightful graphs that offer a clear and intuitive understanding of trends and patterns.")

st.subheader('Capabilities')

st.write(" Our capabilities revolve around the mastery of data-driven insights. We excel in the art of Exploratory Data Analysis (EDA) and sophisticated simulation techniques, enabling us to decode the intricate complexities of the oil and gas sector.")
# lottie_coding = load_lottiefile("./data/99797-data-management.json")  # replace link to local lottie file
# st.sidebar.image("./data/celebal_logo.png")
# st_lottie(
#     lottie_coding,
#     speed=1,
#     reverse=False,
#     loop=True,
#     quality="Hight", # medium ; high 
#     height=500,
#     width=None,
#     key=None,
# )



# Render the custom CSS

from PIL import Image

 

image = Image.open("./data/Oil-Pump2-e1507329016429.jpg")

resized_image = image.resize((700, 300))

 

st.image(resized_image)