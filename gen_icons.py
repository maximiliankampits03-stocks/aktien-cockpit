#!/usr/bin/env python3
"""Erzeugt App-Icons (PNG) ohne externe Bibliotheken."""
import struct, zlib, os

def png_bytes(w, h, px):
    def chunk(t, d):
        c = struct.pack('>I', len(d)) + t + d
        return c + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    raw = b''.join(b'\x00' + b''.join(bytes(p) for p in row) for row in px)
    return (b'\x89PNG\r\n\x1a\n'
            + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw, 9))
            + chunk(b'IEND', b''))

BG = (14, 17, 19)       # #0E1113
GREEN = (76, 175, 80)   # #4CAF50
RED = (239, 83, 80)     # #EF5350
ORANGE = (245, 166, 35) # #F5A623

def make(size, path):
    px = [[BG for _ in range(size)] for _ in range(size)]
    def rect(x0, y0, x1, y1, c):
        for y in range(max(0, int(y0)), min(size, int(y1))):
            row = px[y]
            for x in range(max(0, int(x0)), min(size, int(x1))):
                row[x] = c
    s = size / 512.0
    # drei Kerzen, aufwaerts von links nach rechts
    candles = [
        (128, 300, 430, 265, 460, GREEN),
        (256, 195, 340, 155, 375, RED),
        (384, 95, 255, 60, 295, GREEN),
    ]
    bw, ww = 74 * s, 16 * s
    for cx, bt, bb, wt, wb, c in candles:
        cx *= s
        rect(cx - ww / 2, wt * s, cx + ww / 2, wb * s, c)
        rect(cx - bw / 2, bt * s, cx + bw / 2, bb * s, c)
    # oranger Sockel unten
    rect(64 * s, 480 * s, 448 * s, 492 * s, ORANGE)
    with open(path, 'wb') as f:
        f.write(png_bytes(size, size, px))
    print('ok', path)

here = os.path.dirname(os.path.abspath(__file__))
for size, name in [(512, 'icon-512.png'), (192, 'icon-192.png'),
                   (180, 'apple-touch-icon.png'), (64, 'favicon.png')]:
    make(size, os.path.join(here, name))
