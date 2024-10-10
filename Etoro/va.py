import re
import csv

# Read the input text file
with open('a.html', 'r') as file:
    text = file.read()

# Regular expression to find the value within the pattern
pattern = r'"screener-instrument-name" class="instrument-name">(.*?)</p>'

# Find all matches in the text
values = re.findall(pattern, text)

# Write the extracted values to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Value"])  # Header
    for value in values:
        writer.writerow([value])

# Optionally, write the values to a new text file
with open('output.txt', 'w') as txtfile:
    for value in values:
        txtfile.write(value + '\n')

print("Values have been extracted and saved to output.csv and output.txt")
