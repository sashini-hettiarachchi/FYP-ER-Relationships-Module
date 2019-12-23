from flask import Flask, render_template, request
import relational_schema_mapping
import draw_er
import create_er_xml_file

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
            filehandle = open("res\\input_text.txt", "w")
            filebuffer = text
            filehandle.writelines(filebuffer)
            filehandle.close()

        elif request.form['submit_btn'] == 'clear-text':
            pass  # do something else
        elif request.form['submit_btn'] == 'generate-er':
            create_er_xml_file.create_input_xml_file()
            relational_schema_mapping.build_output_xml_file()
            draw_er.create_csv_file()
            draw_er.create_draw_text_file()

    return 'You entered: {}'.format(request.form['scenario'])


if __name__ == '__main__':
    app.run()
