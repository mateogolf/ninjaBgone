from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def whatName():
    return render_template('noNinja.html')


@app.route('/ninja')
def ninja():
    return render_template('ninja.html')#,color='tmnt')

@app.route('/ninja/<color>')
def turtleShow(color):
    # str1 = "{{url_for('static', filename='"
    # if color == "blue":
    #     str1 += "leonardo.png')}}"
    # elif color == orange:
    #     # return render_template('ninja.html',src="michelangelo.png')}}"
    # elif color == red:
    #     # return render_template('ninja.html',src="raphael.png')}}"
    # elif color == purple:
    #     # return render_template('ninja.html',src="donatello.png')}}"
    # else:
    #     str1 += "notapril.jpg')}}"
    # print str1
    return render_template('ninja.html',color=color)


app.run(debug=True)
