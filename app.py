import pickle
from flask import Flask, render_template, request, app, Response

app=Flask(__name__)

# Load the model
pickle.load(open("model.pkl",'rb'))

@app.route('/',methods=['GET'])

def home():
    return render_template('worldmap.html')


if __name__=="__main__":
    app.run(debug=True)