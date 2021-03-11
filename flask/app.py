# Importing of Libraries
from flask import Flask, render_template, request, redirect, url_for
import requests

# Flask App
app = Flask(__name__)
@app.route('/')

# Defining stats function 
def stats():
    url = "https://j5blqfss4j.execute-api.us-east-2.amazonaws.com/attendance_count/getcount"
    # Change the above url with your API Url
    response = requests.get(url)
    # Converting the json format
    r = response.json()
    print(r)
    # Rendering the html template
    return render_template('stats.html',a=sum(r),b=str(r[0]),c=str(r[1]),d=str(r[2]))

if __name__ == "__main__":
    app.run(debug=True)