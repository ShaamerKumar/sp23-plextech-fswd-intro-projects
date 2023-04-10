from flask import Flask, request

app = Flask(__name__)




@app.route('/hello-json')
def index1():
    return {"text": "Hello World from Dictionary"}

@app.route('/hello-html')
def index2():
    return "<h1>Hello World</h1><p>Subtext</p>"


@app.route('/hello-html-error')
def index3():
    return ("<h1>Hello World</h1><p>Subtext</p>",404)

@app.route('/hello/<name>/change/<num>')
def whatevername(name, num):
   return 'Hello ' + str(name) + ", your change is " + str(10-int(num))

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return f'Hello {name}'
    else:
        return 'Hello World'
    
@app.route('/reflect', methods=['POST'])
def reflect():
    payload_text = request.data.decode('utf-8')
    return f"Hello {payload_text}"



@app.route('/reflect/plex', methods=['POST'])
def reflect_plex():
    data = request.get_json()
    reflected_data = {}
    for key, value in data.items():
        if isinstance(value, str) and isinstance(key,str):
            reflected_data[f"plex_{key}"] = f"plex_{value}"

        elif isinstance(key,str):
            reflected_data[f"plex_{key}"] = value
        else:
            reflected_data[key] = value
    return reflected_data 

@app.route('/reflect/plex/form', methods=['POST'])
def reflect_plex1():
    data = request.form()
    reflected_data = {}
    for key, value in data.items():
        if isinstance(value, str) and isinstance(key,str):
            reflected_data[f"plex_{key}"] = f"plex_{value}"

        elif isinstance(key,str):
            reflected_data[f"plex_{key}"] = value
        else:
            reflected_data[key] = value
    return reflected_data 

app.run(host='0.0.0.0', port=81)