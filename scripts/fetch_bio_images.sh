#!/bin/bash
# Biology-themed replacements via Unsplash (free license)
set -euo pipefail
IMG="/Users/namasiahongkong/HTML/images"
PROJ="$IMG/projects"

resize() {
  local f="$1" w="$2" h="$3"
  sips -z "$h" "$w" "$f" --out "$f" >/dev/null 2>&1
}

dl() {
  local id="$1" out="$2" w="$3" h="$4"
  local path="$out"
  [[ "$out" != /* ]] && { [[ "$out" == projects/* ]] && path="$PROJ/${out#projects/}" || path="$IMG/$out"; }
  curl -sfL "https://images.unsplash.com/${id}?auto=format&fit=crop&w=${w}&h=${h}&q=85" -o "$path"
  resize "$path" "$w" "$h"
  echo "OK $out (${w}x${h})"
}

# Heroes 1920x1281
dl "photo-1581094794329-c8112a89af12" "01hero.jpg" 1920 1281   # lab scientist
dl "photo-1559757175-5700a38864a9"   "02hero.jpg" 1920 1281   # DNA
dl "photo-1628595352115-8e8cbeb1985b" "03hero.jpg" 1920 1281 # molecular
dl "photo-1576086213869-424bfef7f999" "04hero.jpg" 1920 1281 # microscope
dl "photo-1532187863486-abf9cb431c77" "05hero.jpg" 1920 1281 # lab glassware
dl "photo-1617791160505-62b99327e72f" "06hero.jpg" 1920 1281 # cells/microscopy
dl "photo-1582719478250-2a5ebb8c16ca" "07hero.jpg" 1920 1281 # researcher
dl "photo-1667972458132-06d341a7a939" "08hero.jpg" 1920 1281 # modern lab

dl "photo-1581091226035-4d83ed2c2a4a" "about.jpg" 1920 1081    # lab interior wide

# Research focus thumbs
dl "photo-1576086213869-424bfef7f999" "aw01.jpg" 560 560
dl "photo-1559757175-5700a38864a9"   "aw02.jpg" 560 560
dl "photo-1628595352115-8e8cbeb1985b" "aw03.jpg" 560 560
dl "photo-1532187863486-abf9cb431c77" "aw04.jpg" 560 560
dl "photo-1617791160505-62b99327e72f" "aw05.jpg" 560 560
dl "photo-1581094794329-c8112a89af12" "aw06.jpg" 560 560

# project01 liners
dl "photo-1582719478250-2a5ebb8c16ca" "projects/liners01.jpg" 687 990
dl "photo-1576086213869-424bfef7f999" "projects/liners02.jpg" 687 990
dl "photo-1667972458132-06d341a7a939"   "projects/liners03.jpg" 1920 1380
dl "photo-1581094794329-c8112a89af12" "projects/liners04.jpg" 1400 963
dl "photo-1532187863486-abf9cb431c77" "projects/liners05.jpg" 1400 963
dl "photo-1559757175-5700a38864a9"   "projects/liners06.jpg" 1400 963

# project02 green
dl "photo-1617791160505-62b99327e72f" "projects/green01.jpg" 687 990
dl "photo-1576086213869-424bfef7f999" "projects/green02.jpg" 687 990
dl "photo-1628595352115-8e8cbeb1985b" "projects/green03.jpg" 628 749

# project03 nano
dl "photo-1628348068343-d5e109ddb32e" "projects/nano01.jpg" 632 372
dl "photo-1559757175-5700a38864a9"   "projects/nano02.jpg" 632 372
dl "photo-1628595352115-8e8cbeb1985b" "projects/nano03.jpg" 632 372

# project04 dude
dl "photo-1581091226035-4d83ed2c2a4a" "projects/dude01.jpg" 1920 1281

# project05 storm
dl "photo-1582719478250-2a5ebb8c16ca" "projects/storm01.jpg" 1920 1280
dl "photo-1532187863486-abf9cb431c77" "projects/storm02.jpg" 1920 1280
dl "photo-1667972458132-06d341a7a939"   "projects/storm03.jpg" 1920 1280

# project06 chair (structural / protein imagery)
dl "photo-1628595352115-8e8cbeb1985b" "projects/chair01.jpg" 959 965
dl "photo-1559757175-5700a38864a9"   "projects/chair02.jpg" 959 965
dl "photo-1576086213869-424bfef7f999" "projects/chair03.jpg" 959 965
dl "photo-1617791160505-62b99327e72f" "projects/chair04.jpg" 959 965

# team (researcher portraits / lab people)
dl "photo-1582719478250-2a5ebb8c16ca" "team1.jpg" 800 1000
dl "photo-1581094794329-c8112a89af12" "team2.jpg" 800 1000
dl "photo-1579154204638-d690001cded9" "team3.jpg" 800 1000
dl "photo-1560250097-0b93528c311a"   "team4.jpg" 800 1000
dl "photo-1573496359142-b8d87734a5a2" "team5.jpg" 800 1000

echo "All downloads complete."
