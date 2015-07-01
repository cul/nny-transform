To be run against HTML sources in:
/www/data/cu/lweb/digital/collections/nny/cerfb
/www/data/cu/lweb/digital/collections/nny/clarkk
/www/data/cu/lweb/digital/collections/nny/clarkm
/www/data/cu/lweb/digital/collections/nny/fonerm
/www/data/cu/lweb/digital/collections/nny/heiskella
/www/data/cu/lweb/digital/collections/nny/koche
/www/data/cu/lweb/digital/collections/nny/laskerm
/www/data/cu/lweb/digital/collections/nny/oakesjb
/www/data/cu/lweb/digital/collections/nny/perkinsf
/www/data/cu/lweb/digital/collections/nny/stantonf

RUNNING TESTS:

* include lib on PYTHONPATH ENV variable
* python -m unittest discover -s test

RUNNING SCRIPT:
* PYTHONPATH=$PYTHONPATH:lib python nny_urls.py $INPUT $OUTPUT
