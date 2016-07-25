# -*- coding: utf-8 -*-
# citation-curator (c) Pubgem Foundation

import bibtexparser


class Curator:

    def __init__(self):
        pass

    def handle_payload(self, bibtex_payload):
        bib_database = bibtexparser.loads(bibtex_payload)
        print(bib_database.entries)

    def is_entry_in_database(self):
        pass
