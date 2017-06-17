import glob
import dominate
from dominate import document
from dominate.tags import *


def createIndexHTML():
    doc = dominate.document(title='REPONAME')

    with doc.head:
        meta(charset='utf-8')
        meta(name='viewport', content='width=device-width, initial-scale=1')
        link(rel='stylesheet', href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css')
        script(src='ttps://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js')

    with doc:
        with div():
            attr(cls='container')
            h1(img(src='PUTIMAGEHERE.PNG'), " NAMEOFREPO")

        with div():
            attr(cls='container')
            with div():
                attr(cls='well')
                p(span(b('NAMEOFREPO'), cls='text-primary'), " MORE DESC")
                a(cls='btn btn-sm btn-default', href='ydia://url/https://cydia.saurik.com/api/share#?source=REPO_URL_HERE')

        with div():
            attr(cls='container')
            h3(id='wells', cls='page-header')

        with div():
            attr(cls='container')

            with div():
                attr(cls='panel panel-default')

                with div():
                    attr(cls='panel-heading', 'PACK_NAME')

                with div():
                    attr(cls='panel-body', 'DESCRIPTION_OF_PACKAGE')

                a(cls='btn btn-xs btn-default', href="PATH_TO_DEPICS_FOLDER", 'More info')

    print(doc.render())

createIndexHTML()
