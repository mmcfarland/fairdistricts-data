import json
import os
import requests

DIST_DIR = '/usr/dist/'
DATA_SOURCES = [
    {
        'name': 'pa-house',
        'url': 'http://www.pasda.psu.edu/json/PaHouse2017_01.geojson',
        'attr': 'LEG_DISTRI'
    },
    {
        'name': 'pa-senate',
        'url': 'http://www.pasda.psu.edu/json/PaSenatorial2017_01.geojson',
        'attr': 'LEG_DISTRI'
    },
    {
        'name': 'pa-congress',
        'url': 'http://www.pasda.psu.edu/json/PaCongressional2017_01.geojson',
        'attr': 'LEG_DISTRI'
    }
]


def make_dist(src):
    """Make a directory for each layer to store the geoJSON output"""
    out = DIST_DIR + src['name']
    os.makedirs(out, exist_ok=True)
    src.update({'path': out})
    return src


def process(src):
    """Request the layer as geoJSON and save out each feature as its own file"""
    r = requests.get(src['url'])
    layer = r.json()
    for feature in layer['features']:
        dist_id = src['attr']
        dist_name = '{}.geoJSON'.format(feature['properties'][dist_id])
        with open(os.path.join(src['path'], dist_name), 'w') as output:
            output.write(json.dumps(feature))


src_with_dir = [make_dist(src) for src in DATA_SOURCES]

for src in src_with_dir:
    print('processing {}'.format(src['name']))
    process(src)
