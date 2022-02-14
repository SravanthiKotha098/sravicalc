from flask import Flask, render_template, request

app = Flask(__name__)
# app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def result():
    num_1 = request.form.get("var_1", type=int, default=0)
    num_2 = request.form.get("var_2", type=int, default=0)
    operation = request.form.get("operation")
    if(operation == 'Add'):
        result = num_1 + num_2
    elif(operation == 'Subtract'):
        result = num_1 - num_2
    elif(operation == 'Multiply'):
        result = num_1 * num_2
    elif(operation == 'Divide'):
    	if(num_1==0 and num_2==0):
    		result = 0
    	else:
        	result = num_1 / num_2
    else:
        result = 0
    entry = result
    return render_template('form.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
