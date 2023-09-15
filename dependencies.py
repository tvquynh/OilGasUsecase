import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
from itertools import permutations

from scipy.stats import skew

import warnings
warnings.filterwarnings('ignore')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import Ridge, Lasso

import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import ElasticNet
import lightgbm as lgb
from sklearn.neighbors import KNeighborsRegressor

import streamlit as st
import numpy as np
import joblib
import pickle

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import streamlit as st
from scripts.loadanimation import load_lottiefile
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from scripts.loadanimation import load_lottiefile

import plotly.express as px