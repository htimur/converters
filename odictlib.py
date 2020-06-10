from ctypes import *
from bs4 import BeautifulSoup

lib = cdll.LoadLibrary("./odict.so")


def write_odict(tei_doc, output_path):
    print("Creating \"%s\"..." % output_path)

    soup = BeautifulSoup(tei_doc, 'lxml')
    entries = soup.body.findAll('entry')
    od_dictionary = "<dictionary>"

    for entry in entries:
        term = entry.orth.getText()

        print("Processing word \"%s\"..." % term)

        # pronunciation = entry.pron.getText()
        od_entry = "<entry term=\"%s\"><ety>" % term
        senses = entry.findAll('sense')

        for sense in senses:
            od_usage = "<usage>"
            citations = sense.findAll('cit')

            for cit in citations:
                od_usage += "<definition>%s</definition>" % cit.getText().strip()

            od_usage += "</usage>"
            od_entry += od_usage

        od_entry += "</ety></entry>"
        od_dictionary += od_entry

    od_dictionary += "</dictionary>"

    lib.CreateDictionaryFromXML(str.encode(od_dictionary), str.encode(output_path))
