from flask_restful import Resource

skills = ['Python', 'Java', 'PHP', 'Flask', 'Ruby', 'C++', 'Assembly']

class Skills(Resource):
    def get(self):
        return skills