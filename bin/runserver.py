#!/usr/bin/env python
# -*- coding: utf-8 -*-
# citation-curator (c) Pubgem Foundation

from citation_curator.wsgi import app
app.run(port=app.config['PORT'])
