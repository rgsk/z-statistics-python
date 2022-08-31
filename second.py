# Python program creating a
# small document using pylatex

import numpy as np

# importing from a pylatex module
from pylatex import Document, Section, Subsection, Tabular
from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from pylatex.utils import italic
import os

if __name__ == '__main__':
    image_filename = os.path.join(os.path.dirname(__file__), 'kitten.jpg')

    geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
    doc = Document(geometry_options=geometry_options)

    # creating a pdf with title "the simple stuff"
    with doc.create(Section('The simple stuff changed again')):
        doc.append('Some regular text and some')
        doc.append(italic('italic text. '))
        doc.append('\nAlso some crazy characters: $&#{}')
        with doc.create(Subsection('Math that is incorrect')):
            doc.append(Math(data=['2*3', '=', 9]))
            doc.append(
                Math(data=['\\binom{n}{k}', '=', '\\frac{n!}{k!(n-k)!}']))

        # creating subsection of a pdf
        with doc.create(Subsection('Table of something')):
            with doc.create(Tabular('rc|cl')) as table:
                table.add_hline()
                table.add_row((1, 2, 3, 4))
                table.add_hline(1, 2)
                table.add_empty_row()
                table.add_row((4, 5, 6, 7))

    # making a pdf using .generate_pdf
    doc.generate_pdf('full', clean_tex=False)
