#!/bin/bash

# Regular フォントのテーブルを抽出
ttx -t name -t OS/2 -t head -o tables-Regular.ttx ../original/BIZUDPGothic-Regular.ttf
# Bold フォントのテーブルを抽出
ttx -t name -t OS/2 -t head -o tables-Bold.ttx ../original/BIZUDPGothic-Bold.ttf 

# MEMO: 出力された ttx を編集して、adjust_and_merge_fonts.sh でフォントに変更内容を組み込む。
