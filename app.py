import graphene
from flask import Flask
from flask_graphql import GraphQLView

from yandex_direct.graphql.query import QueryType


schema = graphene.Schema(query=QueryType)


app = Flask(__name__)


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
