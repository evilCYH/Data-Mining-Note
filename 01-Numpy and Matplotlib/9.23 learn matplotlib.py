import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# url = "C:\Users\13391\Desktop"
iris = pd.read_csv('./data/iris.csv')

print(iris['Species'].index)

