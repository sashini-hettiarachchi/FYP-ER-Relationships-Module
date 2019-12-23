from flask import Flask, render_template, request
from src.features import draw_er, create_er_xml_file, map_er_to_relational_schema

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
            filehandle = open("data\\input_text.txt", "w")
            filebuffer = text
            filehandle.writelines(filebuffer)
            filehandle.close()

        elif request.form['submit_btn'] == 'clear-text':
            pass  # do something else
        elif request.form['submit_btn'] == 'generate-er':
            create_er_xml_file.create_output_xml_file()
            map_er_to_relational_schema.build_output_xml_file()
            draw_er.create_csv_file()
            draw_er.create_draw_text_file()

    return 'You entered: {}'.format(request.form['scenario'])


if __name__ == '__main__':
    app.run()
