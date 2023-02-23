import pandas as pd
import openai
import os


input_filename = "directory\\filename_analyzed.csv"
df = pd.read_csv(input_filename)

print(df)
