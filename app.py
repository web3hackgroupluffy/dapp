from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
from werkzeug.utils import secure_filename

#from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = 'uploads'  # Set the path to the upload directory
ALLOWED_EXTENSIONS = {'doc','docx','pptx', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # Allowed file types

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/add_data', methods=['POST'])
def add_data():
    field1 = request.form.get('id')
    field2 = request.form.get('password')

    # Insert data into the database
    conn = sqlite3.connect('db/newdb.db')
    cursor = conn.cursor()

    # Assuming you have a table with columns matching the names 'fieldname1' and 'fieldname2'
    cursor.execute("INSERT INTO mytable (id, password) VALUES (?, ?)", (field1, field2))

    conn.commit()
    conn.close()
    return redirect(url_for('home'))
    #return "Data added successfully!"

@app.route('/')
def home():
    try:
        conn = sqlite3.connect('db/newdb.db')  # Ensure this path is correct
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM mytable")  # Replace with your actual query
        rows = cursor.fetchall()
        conn.close()

        # Convert row objects to dictionaries
        data = [dict(row) for row in rows]
        print(rows) # debugging
        return render_template('home.html', data=data)

    except sqlite3.Error as e:
        print("Database error: %s" % e)  # Print any database errors
    finally:
        conn.close()  # Ensure the connection is closed even if an error occurs


@app.route('/upload_file', methods=['POST'])
def upload_file():
    # Handle file upload
    if 'document' in request.files:
        file = request.files['document']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Additional code to handle the uploaded file (e.g., storing in database)
    #return "File uploaded successfully!"
    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(debug=True)



