from flask import Flask, request
from flask_restful import Resource, Api
from skills import Skills
import json



app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':'0,',
        'nome':'Alessandro',
        'skills': ['Python','Flask', 'Django']},
    {
        'id':'1',
        'nome':'Andresa',
        'skills': ['Java', 'Spring']}
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Dev de ID {} do not exist'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Unknown error, call admin to resolve :)'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem': 'registro excluido'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Skills, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)