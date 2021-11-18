from pprint import pprint
from pybtex.database.input import bibtex
from pylatexenc.latex2text import LatexNodes2Text 
parser = bibtex.Parser()
bib_data = parser.parse_file('entrada.bib')
for key in  bib_data.entries.keys():
    
        paper = bib_data.entries[key]
        if paper.original_type == "inproceedings" and int(paper.fields['year']) <=2021:
            
            authors = ""
            for author in paper.persons['author']:
                first = ""
                midle = ""
                last = " "
                if len(author.first_names):
                    first = author.first_names[0]
                if len(author.middle_names):
                    midle = author.middle_names[0]
                if len(author.last_names):
                    last = author.last_names[0]     
                name = first + " "+midle+ " "+last
                authors = name + ", "+authors
            
            title = LatexNodes2Text().latex_to_text(paper.fields['title'])
            authors = LatexNodes2Text().latex_to_text(authors)
            result = "\""+title+"\";\""+authors+"\";\""+paper.fields['url']+"\""
            print (result)
            
            
    
