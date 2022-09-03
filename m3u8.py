def create_m3u8(filenames):
    m3u8 = '\n'.join([
    '#EXTM3U',
    '#EXT-X-VERSION:5',
    '#EXT-X-TARGETDURATION:12',
    '#EXT-X-MEDIA-SEQUENCE:0'
       ])

    for filename in filenames:
        m3u8 += '\n'.join([
        '\n#EXT-X-DISCONTINUITY',
        '#EXTINF:1.0',
        'https://video.seen.io/moderaterna-karnfragor/result/names/' + filename
        ])

    m3u8 += '\n#EXT-X-ENDLIST'

    with open('hej.m3u8', 'w') as f:
        f.write(m3u8)

    print(f'Created a m3u8 file with {len(filenames)} videos.')
