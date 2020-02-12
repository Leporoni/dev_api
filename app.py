from flask import Flask, jsonify, request
import json

app = Flask (__name__)

desenvolvedores = [
    {'nome':'Alessandro',
     'skills': ['Python','Flask', 'Django']},
    {'nome':'Andresa',
     'skills': ['Java', 'Spring']}
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Dev de ID {} do not exist'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Unknown error, call admin to resolve :)'
            response = {'status':'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'registro excluido'})


def lista_devs():
    pass


if __name__ == '__main__':
    app.run(debug=True)