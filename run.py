from moderaterna import Moderaterna
from scb import SCB
from m3u8 import create_m3u8

import pandas as pd
import os

names = SCB.fetch_names(20000)

# df = pd.DataFrame(names)
# df.to_csv('names.csv')
# names = pd.read_csv('names.csv')['0'].to_list()

Moderaterna().fetch_videos(names)

filenames = os.listdir('videos')
filenames.remove('.DS_Store')
create_m3u8(filenames)
