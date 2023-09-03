import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):

    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        neos = []
        for row in reader:
            row['pha'] = False if row["pha"] in ["", "N"] else True
            try:
                neo = NearEarthObject(
                    designation = row.get('pdes'),
                    name = row.get('name', None),
                    diameter = row.get('diameter',float('nan')),
                    hazardous = row['pha'],
                )
            except Exception as e:
                print(e)
            else:
                neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    
    with open(cad_json_path, 'r') as infile:
        reader = json.load(infile)
        reader = [dict(zip(reader["fields"], data)) for data in reader["data"]]
        cad_approaches = []
        for row in reader:
            try:
                cad_approach = CloseApproach(
                    designation = row.get('des'),
                    time = row.get('cd'),
                    distance = row.get('dist',0.0),
                    velocity = row.get('v_rel',0.0),
                )
            except Exception as e:
                print(e)
            else:
                cad_approaches.append(cad_approach) 
    return cad_approaches
