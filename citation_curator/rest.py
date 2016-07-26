# -*- coding: utf-8 -*-
# citation-curator (c) Pubgem Foundation

from flask.ext.restful import Resource
import flask
from flask import request
from .curator import CitationCurator


class Citation(Resource):

    def post(self):
        # curl -X POST --form 'bibtex=<citation_curator/tests/sample.bib' localhost:5049/citation

        if 'bibtex' in request.form:
            payload = request.form['bibtex']
        else:
            flask.abort(400)

        curator = CitationCurator()
        curator.process(payload)
        return "OK"


def init_rest(rest_extension):
    rest_extension.add_resource(Citation, '/citation')
