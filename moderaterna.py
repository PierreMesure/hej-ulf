from concurrent.futures import as_completed
from requests.adapters import HTTPAdapter
from requests_futures.sessions import FuturesSession
from urllib3.util import Retry

def generate_url(name):
    return f'https://video.seen.io/moderaterna-karnfragor/result/names/{name}.mov_720p000.ts'

class Moderaterna(object):

    def __init__(self):
        adapter = HTTPAdapter(max_retries=Retry(total=10, backoff_factor=0.1))

        self.s = FuturesSession(max_workers=30)
        self.s.mount('https://', adapter)

    def fetch_video(self, name):
        print(f'Downloading video for name {name}')

        future = self.s.get(generate_url(name), stream=True)
        future.name = name
        return future

    def fetch_videos(self, names):
        futures = [self.fetch_video(name) for name in names]

        i = 0
        for future in as_completed(futures):
            i += 1
            if future.result().status_code == 200:
                print(f'{future.name} was downloaded ({i}/{len(futures)})')
                with open(f'videos/{future.name}.mov_720p000.ts', 'wb') as out_file:
                    out_file.write(future.result().content)
                out_file.close()
            else:
                print(f'{future.name} was not found ({i}/{len(futures)})')
