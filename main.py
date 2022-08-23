#Creating Website using Flask Framework.
#Importing Flaks and render_template method from flask library
from flask import Flask, render_template

#App is Flask object. __name__ passed in to determine root path
app = Flask(__name__)


#Routing/Mapping URL to Python Function. Homepage is "/" root directory
@app.route('/')
#home function for the home page
def home():
    #returning html template
    return render_template('main.html')

#Dunder name condition, means the indented code below will only run when this file is called directly
if __name__ == "__main__":
    #Function to start/run the app
    app.run(debug=True)

