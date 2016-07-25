# -*- coding: utf-8 -*-
# citation-curator (c) Pubgem Foundation

from flask.ext.restful import Resource
import flask
from flask import request
from .curator import Curator


class Citation(Resource):

    def post(self):
        # curl -X POST -d bibtex='{blah}' localhost:5049/citation
        curator = Curator()

        if 'bibtex' in request.form:
            payload = request.form['bibtex']
        else:
            flask.abort(400)

        curator.handle_payload(payload)

        flask.abort(401)
        # return flask.Response(view_agent(id))


def init_rest(rest_extension):
    rest_extension.add_resource(Citation, '/citation')
