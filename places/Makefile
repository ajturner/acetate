F=fonts

all: place-labels-z3.shp place-labels-z4.shp place-labels-z5.shp place-labels-z6.shp place-labels-z7.shp place-labels-z8.shp place-labels-z9.shp place-labels-z10.shp



place-labels-z3.shp: place-labels-z3.json
	rm -f place-labels-z3.shp place-labels-z3.dbf place-labels-z3.shx place-labels-z3.prj
	ogr2ogr place-labels-z3.shp place-labels-z3.json

	rm -f place-points-z3.shp place-points-z3.dbf place-points-z3.shx place-points-z3.prj
	ogr2ogr place-points-z3.shp place-points-z3.json

place-labels-z4.shp: place-labels-z4.json
	rm -f place-labels-z4.shp place-labels-z4.dbf place-labels-z4.shx place-labels-z4.prj
	ogr2ogr place-labels-z4.shp place-labels-z4.json

	rm -f place-points-z4.shp place-points-z4.dbf place-points-z4.shx place-points-z4.prj
	ogr2ogr place-points-z4.shp place-points-z4.json

place-labels-z5.shp: place-labels-z5.json
	rm -f place-labels-z5.shp place-labels-z5.dbf place-labels-z5.shx place-labels-z5.prj
	ogr2ogr place-labels-z5.shp place-labels-z5.json

	rm -f place-points-z5.shp place-points-z5.dbf place-points-z5.shx place-points-z5.prj
	ogr2ogr place-points-z5.shp place-points-z5.json

place-labels-z6.shp: place-labels-z6.json
	rm -f place-labels-z6.shp place-labels-z6.dbf place-labels-z6.shx place-labels-z6.prj
	ogr2ogr place-labels-z6.shp place-labels-z6.json

	rm -f place-points-z6.shp place-points-z6.dbf place-points-z6.shx place-points-z6.prj
	ogr2ogr place-points-z6.shp place-points-z6.json

place-labels-z7.shp: place-labels-z7.json
	rm -f place-labels-z7.shp place-labels-z7.dbf place-labels-z7.shx place-labels-z7.prj
	ogr2ogr place-labels-z7.shp place-labels-z7.json

	rm -f place-points-z7.shp place-points-z7.dbf place-points-z7.shx place-points-z7.prj
	ogr2ogr place-points-z7.shp place-points-z7.json

place-labels-z8.shp: place-labels-z8.json
	rm -f place-labels-z8.shp place-labels-z8.dbf place-labels-z8.shx place-labels-z8.prj
	ogr2ogr place-labels-z8.shp place-labels-z8.json

	rm -f place-points-z8.shp place-points-z8.dbf place-points-z8.shx place-points-z8.prj
	ogr2ogr place-points-z8.shp place-points-z8.json

place-labels-z9.shp: place-labels-z9.json
	rm -f place-labels-z9.shp place-labels-z9.dbf place-labels-z9.shx place-labels-z9.prj
	ogr2ogr place-labels-z9.shp place-labels-z9.json

	rm -f place-points-z9.shp place-points-z9.dbf place-points-z9.shx place-points-z9.prj
	ogr2ogr place-points-z9.shp place-points-z9.json

place-labels-z10.shp: place-labels-z10.json
	rm -f place-labels-z10.shp place-labels-z10.dbf place-labels-z10.shx place-labels-z10.prj
	ogr2ogr place-labels-z10.shp place-labels-z10.json

	rm -f place-points-z10.shp place-points-z10.dbf place-points-z10.shx place-points-z10.prj
	ogr2ogr place-points-z10.shp place-points-z10.json



place-labels-z3.json: Countries.csv
	python arrange.py -z 3 -m   5 -p place-points-z3.json -l place-labels-z3.json --country-font "$F/Arial.ttf" 12 -c Countries.csv

place-labels-z4.json: Countries.csv Europe-z4-z6.txt US-z4-z8.txt Canada-z4-z8.txt Asia-z4-z6.txt Central-America-z4-z5.txt South-America-z4-z5.txt Australia-New-Zealand-z4-z5.txt Africa-z4-z5.txt
	python arrange.py -z 4 -m  10 -p place-points-z4.json -l place-labels-z4.json --country-font "$F/Arial Bold.ttf" 12 --pop25m-font "$F/Arial.ttf" 12 --pop250k-font "$F/Arial.ttf" 12 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries.csv Europe-z4-z6.txt Asia-z4-z6.txt Australia-New-Zealand-z4-z5.txt US-z4-z8.txt Canada-z4-z8.txt Central-America-z4-z5.txt South-America-z4-z5.txt Africa-z4-z5.txt

place-labels-z5.json: Countries-West.csv Countries-East.csv Europe-z4-z6.txt US-z4-z8.txt Canada-z4-z8.txt Asia-z4-z6.txt Central-America-z4-z5.txt South-America-z4-z5.txt Australia-New-Zealand-z4-z5.txt Africa-z4-z5.txt
	python arrange.py -z 5 -m  10 -p east-points-z5.json -l east-labels-z5.json --country-font "$F/Arial Bold.ttf" 15 --pop25m-font "$F/Arial.ttf" 15 --pop250k-font "$F/Arial.ttf" 10 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-East.csv Europe-z4-z6.txt Asia-z4-z6.txt Australia-New-Zealand-z4-z5.txt Africa-z4-z5.txt
	python arrange.py -z 5 -m  10 -p west-points-z5.json -l west-labels-z5.json --country-font "$F/Arial Bold.ttf" 15 --pop25m-font "$F/Arial.ttf" 15 --pop250k-font "$F/Arial.ttf" 10 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-West.csv US-z4-z8.txt Canada-z4-z8.txt Central-America-z4-z5.txt South-America-z4-z5.txt
	
	python join-geojson.py west-points-z5.json east-points-z5.json > place-points-z5.json
	python join-geojson.py west-labels-z5.json east-labels-z5.json > place-labels-z5.json

place-labels-z6.json: na-labels-z6.json eu-labels-z6.json sa-labels-z6.json au-labels-z6.json af-labels-z6.json
	python join-geojson.py na-points-z6.json eu-points-z6.json sa-points-z6.json au-points-z6.json af-points-z6.json > place-points-z6.json
	python join-geojson.py na-labels-z6.json eu-labels-z6.json sa-labels-z6.json au-labels-z6.json af-labels-z6.json > place-labels-z6.json

na-labels-z6.json: Countries-North-America.csv US-z4-z8.txt Canada-z4-z8.txt Central-America-z4-z5.txt Central-America-z6-z11.txt.gz
	python arrange.py -z 6 -m  20 -p na-points-z6.json -l na-labels-z6.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 13 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-North-America.csv US-z4-z8.txt Canada-z4-z8.txt Central-America-z4-z5.txt Central-America-z6-z11.txt.gz
sa-labels-z6.json: Countries-South-America.csv South-America-z4-z5.txt South-America-z6-z11.txt.gz
	python arrange.py -z 6 -m  20 -p sa-points-z6.json -l sa-labels-z6.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 13 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-South-America.csv South-America-z4-z5.txt South-America-z6-z11.txt.gz
eu-labels-z6.json: Countries-Eurasia.csv Europe-z4-z6.txt Asia-z4-z6.txt
	python arrange.py -z 6 -m  15 -p eu-points-z6.json -l eu-labels-z6.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 13 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-Eurasia.csv Europe-z4-z6.txt Asia-z4-z6.txt
af-labels-z6.json: Countries-Africa.csv Africa-z4-z5.txt Africa-z6-z11.txt.gz
	python arrange.py -z 6 -m   3 -p af-points-z6.json -l af-labels-z6.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 13 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-Africa.csv Africa-z4-z5.txt Africa-z6-z11.txt.gz
au-labels-z6.json: Countries-Australia-NZ.csv Australia-New-Zealand-z4-z5.txt Australia-New-Zealand-z6-z11.txt.gz
	python arrange.py -z 6 -m   2 -p au-points-z6.json -l au-labels-z6.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 13 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-Australia-NZ.csv Australia-New-Zealand-z4-z5.txt Australia-New-Zealand-z6-z11.txt.gz

place-labels-z7.json: na-labels-z7.json eu-labels-z7.json sa-labels-z7.json au-labels-z7.json af-labels-z7.json
	python join-geojson.py na-points-z7.json eu-points-z7.json sa-points-z7.json au-points-z7.json af-points-z7.json > place-points-z7.json
	python join-geojson.py na-labels-z7.json eu-labels-z7.json sa-labels-z7.json au-labels-z7.json af-labels-z7.json > place-labels-z7.json

na-labels-z7.json: Countries-North-America.csv US-z4-z8.txt Canada-z4-z8.txt Central-America-z4-z5.txt Central-America-z6-z11.txt.gz
	python arrange.py -z 7 -m  60 -p na-points-z7.json -l na-labels-z7.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 13 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-North-America.csv US-z4-z8.txt Canada-z4-z8.txt Central-America-z4-z5.txt Central-America-z6-z11.txt.gz
sa-labels-z7.json: Countries-South-America.csv South-America-z4-z5.txt South-America-z6-z11.txt.gz
	python arrange.py -z 7 -m  60 -p sa-points-z7.json -l sa-labels-z7.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 13 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-South-America.csv South-America-z4-z5.txt South-America-z6-z11.txt.gz
eu-labels-z7.json: Countries-Eurasia.csv Europe-z4-z6.txt Europe-z7-z11.txt.gz Asia-z4-z6.txt Asia-z7-z11.txt.gz
	python arrange.py -z 7 -m  90 -p eu-points-z7.json -l eu-labels-z7.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 13 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-Eurasia.csv Europe-z4-z6.txt Europe-z7-z11.txt.gz Asia-z4-z6.txt Asia-z7-z11.txt.gz
af-labels-z7.json: Countries-Africa.csv Africa-z4-z5.txt Africa-z6-z11.txt.gz
	python arrange.py -z 7 -m  10 -p af-points-z7.json -l af-labels-z7.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 13 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-Africa.csv Africa-z4-z5.txt Africa-z6-z11.txt.gz
au-labels-z7.json: Countries-Australia-NZ.csv Australia-New-Zealand-z4-z5.txt Australia-New-Zealand-z6-z11.txt.gz
	python arrange.py -z 7 -m  10 -p au-points-z7.json -l au-labels-z7.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 13 --pop50k-font "$F/Arial.ttf" 10 --popother-font "$F/Arial.ttf" 10 -c Countries-Australia-NZ.csv Australia-New-Zealand-z4-z5.txt Australia-New-Zealand-z6-z11.txt.gz
	
place-labels-z8.json: na-labels-z8.json eu-labels-z8.json as-labels-z8.json sa-labels-z8.json au-labels-z8.json af-labels-z8.json
	python join-geojson.py na-points-z8.json eu-points-z8.json as-points-z8.json sa-points-z8.json au-points-z8.json af-points-z8.json > place-points-z8.json
	python join-geojson.py na-labels-z8.json eu-labels-z8.json as-labels-z8.json sa-labels-z8.json au-labels-z8.json af-labels-z8.json > place-labels-z8.json

na-labels-z8.json: Countries-North-America.csv US-z4-z8.txt Canada-z4-z8.txt Central-America-z4-z5.txt Central-America-z6-z11.txt.gz
	python arrange.py -z 8 -m  90 -p na-points-z8.json -l na-labels-z8.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-North-America.csv US-z4-z8.txt Canada-z4-z8.txt Central-America-z4-z5.txt Central-America-z6-z11.txt.gz
sa-labels-z8.json: Countries-South-America.csv South-America-z4-z5.txt South-America-z6-z11.txt.gz
	python arrange.py -z 8 -m  90 -p sa-points-z8.json -l sa-labels-z8.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-South-America.csv South-America-z4-z5.txt South-America-z6-z11.txt.gz
eu-labels-z8.json: Countries-Europe.csv Europe-z4-z6.txt Europe-z7-z11.txt.gz
	python arrange.py -z 8 -m 120 -p eu-points-z8.json -l eu-labels-z8.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Europe.csv Europe-z4-z6.txt Europe-z7-z11.txt.gz
as-labels-z8.json: Countries-Asia.csv Asia-z4-z6.txt Asia-z7-z11.txt.gz
	python arrange.py -z 8 -m 120 -p as-points-z8.json -l as-labels-z8.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Asia.csv Asia-z4-z6.txt Asia-z7-z11.txt.gz
af-labels-z8.json: Countries-Africa.csv Africa-z4-z5.txt Africa-z6-z11.txt.gz
	python arrange.py -z 8 -m  20 -p af-points-z8.json -l af-labels-z8.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Africa.csv Africa-z4-z5.txt Africa-z6-z11.txt.gz
au-labels-z8.json: Countries-Australia-NZ.csv Australia-New-Zealand-z4-z5.txt Australia-New-Zealand-z6-z11.txt.gz
	python arrange.py -z 8 -m  20 -p au-points-z8.json -l au-labels-z8.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Australia-NZ.csv Australia-New-Zealand-z4-z5.txt Australia-New-Zealand-z6-z11.txt.gz
	
place-labels-z9.json: na-labels-z9.json eu-labels-z9.json as-labels-z9.json sa-labels-z9.json au-labels-z9.json af-labels-z9.json
	python join-geojson.py na-points-z9.json eu-points-z9.json as-points-z9.json sa-points-z9.json au-points-z9.json af-points-z9.json > place-points-z9.json
	python join-geojson.py na-labels-z9.json eu-labels-z9.json as-labels-z9.json sa-labels-z9.json au-labels-z9.json af-labels-z9.json > place-labels-z9.json

na-labels-z9.json: Countries-North-America.csv US-z4-z8.txt US-z9-z11.txt.gz Canada-z4-z8.txt Canada-z9-z11.txt.gz Central-America-z4-z5.txt Central-America-z6-z11.txt.gz
	python arrange.py -z 9 -m  90 -p na-points-z9.json -l na-labels-z9.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-North-America.csv US-z4-z8.txt US-z9-z11.txt.gz Canada-z4-z8.txt Canada-z9-z11.txt.gz Central-America-z4-z5.txt Central-America-z6-z11.txt.gz
sa-labels-z9.json: Countries-South-America.csv South-America-z4-z5.txt South-America-z6-z11.txt.gz
	python arrange.py -z 9 -m  90 -p sa-points-z9.json -l sa-labels-z9.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-South-America.csv South-America-z4-z5.txt South-America-z6-z11.txt.gz
eu-labels-z9.json: Countries-Europe.csv Europe-z4-z6.txt Europe-z7-z11.txt.gz
	python arrange.py -z 9 -m 120 -p eu-points-z9.json -l eu-labels-z9.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Europe.csv Europe-z4-z6.txt Europe-z7-z11.txt.gz
as-labels-z9.json: Countries-Asia.csv Asia-z4-z6.txt Asia-z7-z11.txt.gz
	python arrange.py -z 9 -m 120 -p as-points-z9.json -l as-labels-z9.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Asia.csv Asia-z4-z6.txt Asia-z7-z11.txt.gz
af-labels-z9.json: Countries-Africa.csv Africa-z4-z5.txt Africa-z6-z11.txt.gz
	python arrange.py -z 9 -m  20 -p af-points-z9.json -l af-labels-z9.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Africa.csv Africa-z4-z5.txt Africa-z6-z11.txt.gz
au-labels-z9.json: Countries-Australia-NZ.csv Australia-New-Zealand-z4-z5.txt Australia-New-Zealand-z6-z11.txt.gz
	python arrange.py -z 9 -m  20 -p au-points-z9.json -l au-labels-z9.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Australia-NZ.csv Australia-New-Zealand-z4-z5.txt Australia-New-Zealand-z6-z11.txt.gz
	
place-labels-z10.json: na-labels-z10.json eu-labels-z10.json as-labels-z10.json sa-labels-z10.json au-labels-z10.json af-labels-z10.json
	python join-geojson.py na-points-z10.json eu-points-z10.json as-points-z10.json sa-points-z10.json au-points-z10.json af-points-z10.json > place-points-z10.json
	python join-geojson.py na-labels-z10.json eu-labels-z10.json as-labels-z10.json sa-labels-z10.json au-labels-z10.json af-labels-z10.json > place-labels-z9.json

na-labels-z10.json: Countries-North-America.csv US-z4-z8.txt US-z9-z11.txt.gz Canada-z4-z8.txt Canada-z9-z11.txt.gz Central-America-z4-z5.txt Central-America-z6-z11.txt.gz
	python arrange.py -z 10 -m  90 -p na-points-z10.json -l na-labels-z10.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-North-America.csv US-z4-z8.txt US-z9-z11.txt.gz Canada-z4-z8.txt Canada-z9-z11.txt.gz Central-America-z4-z5.txt Central-America-z6-z11.txt.gz
sa-labels-z10.json: Countries-South-America.csv South-America-z4-z5.txt South-America-z6-z11.txt.gz
	python arrange.py -z 10 -m  90 -p sa-points-z10.json -l sa-labels-z10.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-South-America.csv South-America-z4-z5.txt South-America-z6-z11.txt.gz
eu-labels-z10.json: Countries-Europe.csv Europe-z4-z6.txt Europe-z7-z11.txt.gz
	python arrange.py -z 10 -m 120 -p eu-points-z10.json -l eu-labels-z10.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Europe.csv Europe-z4-z6.txt Europe-z7-z11.txt.gz
as-labels-z10.json: Countries-Asia.csv Asia-z4-z6.txt Asia-z7-z11.txt.gz
	python arrange.py -z 10 -m 120 -p as-points-z10.json -l as-labels-z10.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Asia.csv Asia-z4-z6.txt Asia-z7-z11.txt.gz
af-labels-z10.json: Countries-Africa.csv Africa-z4-z5.txt Africa-z6-z11.txt.gz
	python arrange.py -z 10 -m  20 -p af-points-z10.json -l af-labels-z10.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Africa.csv Africa-z4-z5.txt Africa-z6-z11.txt.gz
au-labels-z10.json: Countries-Australia-NZ.csv Australia-New-Zealand-z4-z5.txt Australia-New-Zealand-z6-z11.txt.gz
	python arrange.py -z 10 -m  20 -p au-points-z10.json -l au-labels-z10.json --country-font "$F/Arial Bold.ttf" 18 --pop25m-font "$F/Arial.ttf" 18 --pop250k-font "$F/Arial.ttf" 18 --pop50k-font "$F/Arial.ttf" 13 --popother-font "$F/Arial.ttf" 10 -c Countries-Australia-NZ.csv Australia-New-Zealand-z4-z5.txt Australia-New-Zealand-z6-z11.txt.gz
	


clean:
	rm -f place-labels-z3.json
	rm -f place-labels-z4.json
	rm -f place-labels-z5.json west-labels-z5.json east-labels-z5.json
	rm -f place-labels-z6.json na-labels-z6.json eu-labels-z6.json sa-labels-z6.json au-labels-z6.json af-labels-z6.json
	rm -f place-labels-z7.json na-labels-z7.json eu-labels-z7.json sa-labels-z7.json au-labels-z7.json af-labels-z7.json
	rm -f place-labels-z8.json na-labels-z8.json eu-labels-z8.json sa-labels-z8.json au-labels-z8.json af-labels-z8.json
	rm -f place-labels-z9.json na-labels-z9.json eu-labels-z9.json sa-labels-z9.json au-labels-z9.json af-labels-z9.json
	rm -f place-labels-z10.json na-labels-z10.json eu-labels-z10.json sa-labels-z10.json au-labels-z10.json af-labels-z10.json

	rm -f place-points-z3.json
	rm -f place-points-z4.json
	rm -f place-points-z5.json west-points-z5.json east-points-z5.json
	rm -f place-points-z6.json na-points-z6.json eu-points-z6.json sa-points-z6.json au-points-z6.json af-points-z6.json
	rm -f place-points-z7.json na-points-z7.json eu-points-z7.json sa-points-z7.json au-points-z7.json af-points-z7.json
	rm -f place-points-z8.json na-points-z8.json eu-points-z8.json sa-points-z8.json au-points-z8.json af-points-z8.json
	rm -f place-points-z9.json na-points-z9.json eu-points-z9.json sa-points-z9.json au-points-z9.json af-points-z9.json
	rm -f place-points-z10.json na-points-z10.json eu-points-z10.json sa-points-z10.json au-points-z10.json af-points-z10.json

	rm -f place-labels-z3.shp place-labels-z3.dbf place-labels-z3.shx place-labels-z3.prj
	rm -f place-labels-z4.shp place-labels-z4.dbf place-labels-z4.shx place-labels-z4.prj
	rm -f place-labels-z5.shp place-labels-z5.dbf place-labels-z5.shx place-labels-z5.prj
	rm -f place-labels-z6.shp place-labels-z6.dbf place-labels-z6.shx place-labels-z6.prj
	rm -f place-labels-z7.shp place-labels-z7.dbf place-labels-z7.shx place-labels-z7.prj
	rm -f place-labels-z8.shp place-labels-z8.dbf place-labels-z8.shx place-labels-z8.prj
	rm -f place-labels-z9.shp place-labels-z9.dbf place-labels-z9.shx place-labels-z9.prj
	rm -f place-labels-z10.shp place-labels-z10.dbf place-labels-z10.shx place-labels-z10.prj

	rm -f place-points-z3.shp place-points-z3.dbf place-points-z3.shx place-points-z3.prj
	rm -f place-points-z4.shp place-points-z4.dbf place-points-z4.shx place-points-z4.prj
	rm -f place-points-z5.shp place-points-z5.dbf place-points-z5.shx place-points-z5.prj
	rm -f place-points-z6.shp place-points-z6.dbf place-points-z6.shx place-points-z6.prj
	rm -f place-points-z7.shp place-points-z7.dbf place-points-z7.shx place-points-z7.prj
	rm -f place-points-z8.shp place-points-z8.dbf place-points-z8.shx place-points-z8.prj
	rm -f place-points-z9.shp place-points-z9.dbf place-points-z9.shx place-points-z9.prj
	rm -f place-points-z9.shp place-points-z9.dbf place-points-z9.shx place-points-z9.prj
