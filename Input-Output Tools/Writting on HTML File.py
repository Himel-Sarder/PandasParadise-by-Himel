import pandas as pd
import os

# Sample data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve'],
    'Age': [30, 25, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert DataFrame to HTML
html_table = df.to_html(index=False)

# Specify the directory where you want to save the file
directory = r'E:\Python\Python Practice\Complete Pandas\Input-Output Tools\Output'
if not os.path.exists(directory):
    os.makedirs(directory)

# Specify the file path
file_path = os.path.join(directory, 'output4.html')

# Write HTML to the file
with open(file_path, 'w') as f:
    f.write(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sample HTML Page with Pandas</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f0f0f0;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Sample HTML Page with Pandas</h1>
        {html_table}
    </body>
    </html>
    ''')

print(f"HTML file generated successfully and saved to {file_path}")
