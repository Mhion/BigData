import pandas as pd
import tkinter as tk
import tglearn


def predict_life_satisfaction():
    x = int(en_GDP_per_capita.get())
    X_new = [[x]]

    life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
    X = life_satisfaction[["GDP per capita (USD)"]].values  # return 2d array