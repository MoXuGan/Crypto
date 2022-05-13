import warnings
warnings.filterwarnings('ignore')
import os
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import streamlit as st

df = pd.read_csv('archive\coin_Bitcoin.csv')
st.write("Hello Moi")