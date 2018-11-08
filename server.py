
from flask import Flask, render_template, jsonify
from Dataset1State import *
from Dataset2State import *
from DatasetContext import *
from Dataset1Option1Data import *
from Dataset1Option2Data import *
from Dataset1Option3Data import *
from Dataset2Option1Data import *
from Dataset2Option2Data import *


my_list=[]

app = Flask(__name__)

@app.route('/')
def server_page():
    return render_template("startpage.html")

@app.route('/dataset1')
def dataset1_page():
    global  my_list
    dataContext = DatasetContext(Dataset1State())
    my_list = dataContext.getCSVData()
    return render_template("dataset1page.html")

@app.route('/dataset2')
def dataset2_page():
    global  my_list
    dataContext = DatasetContext(Dataset2State())
    my_list = dataContext.getCSVData()
    return render_template("dataset2page.html")

@app.route('/dataset1/option1')
def dataset1option1_page():
    return render_template("dataset1option1.html")

@app.route('/dataset1/option2')
def dataset1option2_page():
    return render_template("dataset1option2.html")

@app.route('/dataset1/option3')
def dataset1option3_page():
    return render_template("dataset1option3.html")

@app.route('/dataset2/option1')
def dataset2option1_page():
    return render_template("dataset2option1.html")

@app.route('/dataset2/option2')
def dataset2option2_page():
    return render_template("dataset2option2.html")

@app.route('/dataset1/option1/data')
def data1():
    dataTemplate = Dataset1Option1Data()
    global my_list
    res = dataTemplate.getData(my_list)
    return jsonify(res)

@app.route('/dataset1/option2/data')
def data2():
    dataTemplate = Dataset1Option2Data()
    global my_list
    res = dataTemplate.getData(my_list)
    return jsonify(res)

@app.route('/dataset1/option3/data')
def data3():
    dataTemplate = Dataset1Option3Data()
    global my_list
    res = dataTemplate.getData(my_list)
    return jsonify(res)

@app.route('/dataset2/option1/data')
def data4():
    dataTemplate = Dataset2Option1Data()
    global my_list
    res = dataTemplate.getData(my_list)
    return jsonify(res)

@app.route('/dataset2/option2/data')
def data5():
    dataTemplate = Dataset2Option2Data()
    global my_list
    res = dataTemplate.getData(my_list)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
