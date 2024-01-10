#!/usr/bin/env python
# coding: utf-8

import os
import sys
import glob
# import importlib
import gif_animate
# importlib.reload(gif_animate)
from gif_animate import *
from s3_file import s3_download
import ard_stac_search
# importlib.reload(ard_stac_search)
from ard_stac_search import Astac

print ("Number of arguments:", len(sys.argv), "arguments")
print ("Argument List:", str(sys.argv))

arg=sys.argv[1]

a = arg.split('_')

H=a[0]
V=a[1]
YEAR=a[2]

date_range_text = f"{YEAR}-01-01/{YEAR}-12-31"

DATA_ROOT = '/wspcefs/opt/tony'
#DATA_ROOT = '/caldera/projects/usgs/water/impd/butzer'
#DATA_ROOT = '/data2/butzer'
BROWSE = f'{DATA_ROOT}/browse_{H}_{V}'
ANIMATIONS = f'{DATA_ROOT}/animations'

os.makedirs(BROWSE, exist_ok=True)
os.makedirs(ANIMATIONS, exist_ok=True)

stac_config = {}

stac_config['url'] = 'https://landsatlook.usgs.gov/stac-server'
stac_config['fav_collection'] = 'landsat-c2ard-sr'
stac_config['description'] = 'Landsat Collection 2 ARD Tiles Surface Reflection'


_stac = Astac(stac_config)

print(_stac.collection())
print(_stac.collections_list())
print(_stac.collections_df())

cloud_cover_pct_max = '99'

_assets = _stac.get_my_assets(None, H, V, date_range_text, cloud_cover_pct_max)

asset_df = _stac.fav_fields_df(_assets)

print(asset_df.head())
print(asset_df.columns)
print(_assets[0]['properties'].keys())


# # ref
# - https://github.com/Element84/geo-notebooks/blob/main/notebooks/planetary-computer-odc-stac-landsat.ipynb

for thumb in asset_df['reduced_resolution_browse']:
    print(thumb)

s3url = asset_df['reduced_resolution_browse'][0]
print(s3url)

s3_download(s3url, BROWSE)

# tqdm here perhaps?
for thumb in asset_df['reduced_resolution_browse']:
    s3url = thumb
    s3_download(s3url, BROWSE)
    #print(thumb)

#! mkdir /data2/butzer/animations

frame_folder=BROWSE
output_gif_name=f'{ANIMATIONS}/{YEAR}_{H}_{V}.gif'

for image in glob.glob(f"{frame_folder}/*.jpeg"):
    print(image)
    em_str = image.split('/')[-1].replace('_02_thumb_large.jpeg', '')
    emboss_image(image, em_str)

print('Building the animation ...')
make_gif_from_jpeg(frame_folder, output_gif_name)

print(f'SUCCESS {output_gif_name} created!')

# print(frame_folder)

#print(asset_df.head())





