import numpy as np
import pandas as pd
from flask import Flask, render_template


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0


@app.route("/")
def welcome():
    webpage = render_template('index.html')
    return webpage


if __name__ == '__main__':
    app.run(debug=True)