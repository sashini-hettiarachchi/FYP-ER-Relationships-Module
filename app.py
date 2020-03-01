from time import sleep

from flask import Flask, request, jsonify, json

import main
from src import get_output_data, create_er_xml_file
from utils import file_manipulation

app = Flask(__name__)


@app.route('/api/v1/relationships', methods=['GET'])
def return_er_data():
    main.create_er_diagram_xml_file()
    sleep(1)
    relationship_data = get_output_data.get_relationship_list()
    print("Successfully Generated ER Diagram")
    print(relationship_data)
    return jsonify(relationship_data)


@app.route('/api/v1/schema', methods=['GET'])
def generate_relational_schema():
    main.create_relational_schema()
    return jsonify({"success": "true", "error": "false"})


@app.route('/api/v1/csv', methods=['POST'])
def create_er_csv():
    data = json.loads(request.data)
    create_er_xml_file.recreate_relation_xml(data)
    if data is None:
        return jsonify({"success": "false", "error": "true", "message": "JSON not found"})
    else:
        main.create_er_diagram_text_file()
        return jsonify({"success": "true", "error": "false"})


@app.route('/api/v1/clear', methods=['GET'])
def clear_files():
    file_manipulation.remove_files()
    return jsonify({"success": "true", "error": "false"})


# @app.route('/')
# def home_page():
#     return render_template('home.html')
#
#
# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         if request.form['submit_btn'] == 'add-text':
#             text = request.form['scenario']
#             print(text)
#             filehandle = open(file_manipulation.PATH + "\\input_text.txt", "w")
#             filebuffer = text
#             filehandle.writelines(filebuffer)
#             filehandle.close()
#             return render_template('home.html')
#
#         elif request.form['submit_btn'] == 'query-generator':
#             main.create_relational_schema()
#             print("Successfully Generated Relational Schema")
#             return render_template('home.html')
#
#         elif request.form['submit_btn'] == 'generate-er':
#             main.create_er_diagram_xml_file()
#             main.create_er_diagram_text_file()
#             relationship_data = get_output_data.get_relationship_list()
#             print("Successfully Generated ER Diagram")
#             print("rel", relationship_data)
#             print(len(relationship_data))
#             return render_template('er_draw.html', relationship_data=relationship_data)
#
#         elif request.form['submit_btn'] == 'clear-all':
#             file_manipulation.remove_files()
#             return render_template('home.html')
#
#
# @app.route('/list_change', methods=['POST'])
# def list_change():
#     if request.method == 'POST':
#         if request.form['submit_btn'] == 'update_list':
#             data = request.get_json()
#             print(data['html_data'])


if __name__ == '__main__':
    app.run()
