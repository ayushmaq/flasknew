from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Replace the following connection string with your SQL Server connection details
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=jan2bootcampserver.database.windows.net;'
    r'DATABASE=Jan2bootcampdatabase;'
    r'UID=bootcamp;'
    r'PWD=Pass@123;'
)

@app.route('/')
def display_top_20_rows():
    try:
        connection = pyodbc.connect(conn_str)
        cursor = connection.cursor()

        # Replace 'your_table_name' with the actual table name
        query = 'SELECT TOP 20 * FROM [SalesLT].[Customer]'
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        return render_template('index.html', rows=rows)

    except Exception as e:
        return f"Error: {str(e)}"

   

if __name__ == '__main__':
    app.run(debug=True)
