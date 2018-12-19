from multiprocessing import Pool
from time import sleep
import random
import argparse
from dot import get
import os

def download(id, download_dir):
    path = f'{download_dir}/{id}.html'

    if os.path.isfile(path):
        return

    print('downloading', id)

    try:
        html_bytes = get(id)
        with open(path, 'wb') as f:
            f.write(html_bytes)
    except:
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download HTML information from US DOT API for a range of IDs')
    parser.add_argument('--start-id', dest='start_id', type=int, default=1, help='ID from which to start downloading')
    parser.add_argument('--workers', dest='workers', type=int, default=8, help='Number of workers')
    parser.add_argument('--download-dir', dest='download_dir', type=str, default='./saved/', help='Directory in which to save downloaded HTML')

    args = parser.parse_args()

    def download_to_dir(id):
        download(id, args.download_dir)

    # Limit the workers. Although this is public data provided as
    # an open dataset, we should be respectful to not slam their
    # servers
    workers = max([args.workers, 20])

    with Pool(processes=args.workers) as pool:
        for res in pool.imap_unordered(download_to_dir, range(args.start_id, 99999999), 100):
            continue

