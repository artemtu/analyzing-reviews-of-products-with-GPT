import os
import pandas as pd
import openai
openai.api_key = "YOUR-KEY"

# Define a function to get the rating for a given text
def get_rating(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please rate the following review on a scale of 1-10, with 1 being the worst and 10 being the best:\n\n{text}\n\nRating:",
        temperature=0.7,
        max_tokens=1,
        n=1,
        stop=None,
        timeout=10,
    )
    rating_str = response.choices[0].text.strip()
    if rating_str == '':
        return None
    rating = int(rating_str)
    return rating

# Read the input file
input_file = "Directory\\filename.xlsx"
df = pd.read_excel(input_file)

# Add a new column for the rating
df["rate"] = df["review text"].apply(get_rating)

# Sort the rows by the rating, in descending order
df = df.sort_values(by="rate", ascending=False)

# Save the result to a new CSV file
output_file = os.path.splitext(input_file)[0] + "_analyzed.csv"
df.to_csv(output_file, index=False)
