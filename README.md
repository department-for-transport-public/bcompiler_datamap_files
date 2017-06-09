# Datamaps & Templates for bcompiler tool

These are supporting files for the bcompiler tool.

### Process for interleaving between Q4 and Q1

* `cp datamap.csv datamap.csv-bak`
* `cp bicc_template.xlsx bicc_template.csv-bak`
* `mv archive/bicc_template_old.xlsx bicc_template.xlsx`
* `mv archive/datamap_for_Q4_compilation.csv datamap.csv`
* `bcompiler compile -c` to clean the datamap
* Ensure all Q4 source files are in `~/Documents/bcompiler/source/returns`
* `bcompiler compile` to complile to `~/Documents/bcompiler/output/compiled_master....xlsx`
* Open the new compiled master file in spreadsheet application and resave as
    `~/Documents/bcompiler/source/master.csv`
* `python scripts/field_changes.py` to make WG field changes within the
    `master.csv` file. Ensure correct file targets are included in the script
    to do this.
* `bcompiler compile -p ~/Documents/bcompiler/source/master.csv` to
    transpose this file to `~/Documents/bcompiler/source/master_transposed.csv`
* `mv scripts/new-master.csv master.csv` to put the correct master in place.
* Put back `datamap.csv-bak` to `datamap.csv` and `bicc_template.xlsx-bak` to
    `bicc_template.xlsx`.
* `bcompiler compile -a` to export master data into the the template for each
    project.
