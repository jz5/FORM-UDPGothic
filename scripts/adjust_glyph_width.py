import sys
from fontTools.ttLib import TTFont
from pathlib import Path

def adjust_glyph_width(input_path, output_path, glyph_names, target_widths):
    """
    指定されたグリフの幅を調整し、新たなフォントを出力する。
    元の LSB と RSB の比率を維持しながら余白を追加する。

    :param input_path: 入力フォントファイルのパス
    :param output_path: 出力フォントファイルのパス
    :param glyph_names: 幅を調整するグリフの名前リスト（例: ["one", "two"]）
    :param target_widths: 各グリフの目標とする幅リスト
    """
    # フォントを読み込む
    font = TTFont(input_path)

    # hmtxテーブル（水平メトリック）と glyf テーブルを取得
    hmtx_table = font['hmtx']
    glyf_table = font['glyf']

    for glyph_name, target_width in zip(glyph_names, target_widths):
        # 現在の幅を取得
        current_width, lsb = hmtx_table[glyph_name]
        glyph = glyf_table[glyph_name]

        if not glyph.isComposite():
            rsb = current_width - (lsb + glyph.xMax - glyph.xMin)  # RSB (右側ベアリング) を計算

            # 現在の LSB と RSB の比率を計算
            total_margin = lsb + rsb
            if total_margin == 0:
                left_ratio = 0.5
                right_ratio = 0.5
            else:
                left_ratio = lsb / total_margin
                right_ratio = rsb / total_margin

            # 幅差分を計算
            diff = target_width - current_width
            if diff < 0:
                raise ValueError(f"目標幅 {target_width} は現在の幅 {current_width} より小さいため、縮小はサポートされていません。")

            # 余白を比率に基づいて計算
            left_space = int(diff * left_ratio)
            right_space = diff - left_space  # 残りを右側に

            # LSB（左側のベアリング）を更新
            new_lsb = lsb + left_space
            hmtx_table[glyph_name] = (target_width, new_lsb)

            # グリフの座標を調整
            glyph.xMin -= left_space
            glyph.xMax += right_space

            # すべての輪郭の座標をシフト
            coordinates = glyph.coordinates
            for i in range(len(coordinates)):
                x, y = coordinates[i]
                coordinates[i] = (x + left_space, y)

    # フォントを保存
    font.save(output_path)

if __name__ == "__main__":
    # コマンドライン引数を取得
    if len(sys.argv) < 5 or (len(sys.argv) - 3) % 2 != 0:
        print("Usage: python3 adjust_glyph_width.py <input_ttf> <output_ttf> <glyph_name1> <target_width1> [<glyph_name2> <target_width2> ...]")
        sys.exit(1)

    input_ttf = Path(sys.argv[1])
    output_ttf = Path(sys.argv[2])
    glyph_names = sys.argv[3::2]  # 奇数番目の引数
    target_widths = list(map(int, sys.argv[4::2]))  # 偶数番目の引数

    try:
        adjust_glyph_width(input_ttf, output_ttf, glyph_names, target_widths)
        print(f"以下のグリフの幅を調整しました: {dict(zip(glyph_names, target_widths))}")
    except KeyError as e:
        print(f"エラー: グリフが見つかりません: {e}")
    except ValueError as e:
        print(f"エラー: {e}")