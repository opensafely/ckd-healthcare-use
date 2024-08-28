# converts all local codelists .csv files from UTF-8-with-BOM to UTF-8

import codecs
from glob import glob

for codelist in glob("local_codelists/*.csv"):
    has_bom = False
    with open(codelist, "rb") as f:
        has_bom = f.read(3) == codecs.BOM_UTF8
    if has_bom:
        with open(codelist, "r", encoding="utf-8-sig") as f:
            contents = f.read()
        with open(codelist, "w", encoding="utf-8") as f:
            f.write(contents)
