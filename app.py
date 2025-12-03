from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("myform.html")
@app.route('/submit', methods=['post'])
def submit():
    fname=request.form['fname']
    lname=request.form['lname']
    age=request.form['age']
    return render_template('greetings.html',fname=fname, lname=lname, age=age, phone number=phone number)
if(__name__=="__main__"):
    app.run(debug=True)
