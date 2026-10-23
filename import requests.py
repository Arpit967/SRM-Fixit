import re
from urllib.request import urlopen
from html import unescape


def decode_message(url):
    page = urlopen(url).read().decode("utf-8")

    points = []
    for row in re.findall(r"<tr.*?</tr>", page, re.S):
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)
        cells = [unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in cells]
        if len(cells) == 3 and cells[0].isdigit() and cells[2].isdigit():
            points.append((int(cells[0]), cells[1], int(cells[2])))

    if not points:
        print("No data found")
        return

    max_x = max(p[0] for p in points)
    max_y = max(p[2] for p in points)

    grid = [[" "] * (max_x + 1) for _ in range(max_y + 1)]
    for x, ch, y in points:
        grid[y][x] = ch

    for row in reversed(grid):
        print("".join(row))


decode_message(
    "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
)