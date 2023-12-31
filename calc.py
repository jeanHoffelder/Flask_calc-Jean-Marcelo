from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operacao")
    if(operation == 'Adição'):
        result = var_1 + var_2
    elif(operation == 'Subtração'):
        result = var_1 - var_2
    elif(operation == 'Multiplicação'):
        result = var_1 * var_2
    elif(operation == 'Divisão'):
        result = var_1 / var_2
    else:
        result = 'Escolha inválida'
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
