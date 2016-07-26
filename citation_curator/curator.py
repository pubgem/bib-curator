# -*- coding: utf-8 -*-
# citation-curator (c) Pubgem Foundation

import bibtexparser
from slugify import slugify
import flask
import os
from git import Repo
from git.exc import NoSuchPathError


class CitationCurator:

    def __init__(self):
        """
        """
        self.bib_path = flask.current_app.config.get("BIBLIOGRAPHY_PATH")
        self.repo = self.ensure_repo()
        self.commit_message = ""

    def process(self, bibtex):
        """
        """
        # first, determine whether it's already in the database.
        bib_database = bibtexparser.loads(bibtex)
        bib_filename = self.determine_filename(bib_database)

        # look in the bib file for the citation key (e.g. Cesar2013)
        if not self.is_citation_in_file(bib_database, bib_filename):
            # if it is not there, then append this citation to the file
            self.append_citation(bib_filename, bibtex)
            self.commit_message += "add citation for {0}\n".format(bib_database.entries[0]["title"])
            self.commit_changes()
        else:
            print("already in file")

    def determine_filename(self, bib_database):
        """
        """
        journal = bib_database.entries[0]["journal"]
        full_filename = os.path.join(self.bib_path, "{0}.bib".format(slugify(journal)))
        return(full_filename)

    def is_citation_in_file(self, bib_database, bib_filename):
        """
        """
        citation = bib_database.entries[0]
        if not os.path.isfile(bib_filename):
            return False
        else:
            with open(bib_filename, "r") as f:
                search_bib = bibtexparser.load(f)
                for entry in search_bib.entries:
                    if entry['title'] == citation['title'] and \
                            entry['year'] == citation['year']:
                                return(True)
            return(False)

    def append_citation(self, bib_filename, bibtex):
        """
        """
        if not os.path.isfile(bib_filename):
            with open(bib_filename, "w") as f:
                pass
            self.commit_message += "create journal {0}\n".format(os.path.basename(bib_filename))

        with open(bib_filename, "a") as f:
            f.write(bibtex)
            f.write("\n")

        self.repo.index.add([os.path.basename(bib_filename)])

    def ensure_repo(self):
        """
        """
        try:
            repo = Repo(self.bib_path)
        except NoSuchPathError:
            repo = Repo.clone_from("git@github.com:pubgem/bib.git", self.bib_path)
            if repo:
                print("cloned it")

        git = repo.git
        git.checkout("testing")
        git.push("--set-upstream", "origin", "testing")
        return(repo)

    def commit_changes(self):
        """
        commit the change to the github repository
        """

        # obtain the deploy key from the environment

        self.repo.index.commit(self.commit_message)
        origin = self.repo.remotes.origin
        origin.push()
