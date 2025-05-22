#!/bin/bash

python3 adjust_glyph_width.py ../original/BIZUDPGothic-Regular.ttf temp.ttf one 1556 uniFF11 1556
ttx -m temp.ttf tables-Regular.ttx -o ../release/FORMUDPGothic-Regular.ttf

python3 adjust_glyph_width.py ../original/BIZUDPGothic-Bold.ttf temp.ttf one 1556 uniFF11 1556
ttx -m temp.ttf tables-Bold.ttx -o ../release/FORMUDPGothic-Bold.ttf

rm temp.ttf
rm -rf /diff

diffenator2 diff -fb ../original/BIZUDPGothic-Regular.ttf -fa ../release/FORMUDPGothic-Regular.ttf -o ../diff/Regular
diffenator2 diff -fb ../original/BIZUDPGothic-Bold.ttf -fa ../release/FORMUDPGothic-Bold.ttf -o ../diff/Bold
