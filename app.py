from flask import Flask, render_template, request, redirect, url_for
import main
from utils import file_manipulation

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    print("xyz")
    if request.method == 'POST':
        if request.form['submit_btn'] == 'add-text':
            text = request.form['scenario']
            print(text)
            filehandle = open(".\\src\\data\\input_text.txt", "w")
            filebuffer = text
            filehandle.writelines(filebuffer)
            filehandle.close()

        elif request.form['submit_btn'] == 'query-generator':
            main.create_relational_schema()
            print("Successfully Generated Relational Schema")

        elif request.form['submit_btn'] == 'generate-er':
            main.create_er_diagram_xml_file()
            main.create_er_diagram_text_file()
            print("Successfully Generated ER Diagram")

        elif request.form['submit_btn'] == 'clear-all':
            file_manipulation.remove_files()

    return render_template('home.html')


if __name__ == '__main__':
    app.run()
