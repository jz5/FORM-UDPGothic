# 帳票 UDPゴシック (FORM UDPGothic)

**モリサワ [BIZ UDPゴシック](https://github.com/googlefonts/morisawa-biz-ud-gothic) (Version 1.051) の「1」と「１（全角）」の幅のみを変更し、数字（0〜9）を等幅にしたフォントです（※）。** 

「BIZ UDPゴシック」を使いたい！ でも、数字は等幅にしたい。でも、等幅の「BIZ UDゴシック」の数字は細すぎる！　というときに使えるフォントです。

「BIZ UDPゴシック」のグリフ数 13,932個のうち2個を変更し、残りの約 99.9856% のグリフは全く同じです。

※「BIZ UDPゴシック」は、0〜9 のうち 1 のみ幅（サイドベアリング）が異なる。

「[帳票 UDP明朝](https://github.com/jz5/FORM-UDPMincho)」も作りました。

![](image.png)

## 注意: Windows の BIZ UDPゴシックとの違い

「帳票 UDPゴシック」は、オープンソースライセンスの「[BIZ UDPゴシック](https://github.com/googlefonts/morisawa-biz-ud-gothic)(version 1.051)」を改変したフォントです（Google Fonts でも提供されているフォント）。

Windows で提供されている「[BIZ UDPゴシック](https://www.morisawa.co.jp/about/news/4010)(version 2.01)」と、「[BIZ UDPゴシック](https://github.com/googlefonts/morisawa-biz-ud-gothic)(version 1.051)」は、グリフの形状はほぼ同じようですが、パラメーター等に多数の差異があり、少なくとも Windows 10 でレンダリング結果が異なる場合があります。

そのため、「帳票 UDPゴシック」も、Windows の「BIZ UDPゴシック」とは、レンダリング結果が異なる場合があります。

||version 2.01|version 1.051|
| --- | --- | --- |
|グリフ数|12,691|13,932|
|U+005C|円記号|バックスラッシュ|

差分ツールによると [Combining character](https://en.wikipedia.org/wiki/Combining_character) 29個に差異がある（が、違い不明）。


## ダウンロード

[Release](https://github.com/jz5/FORM-UDPGothic/releases) から。

## Repository

* diff: [Diffenator 2](https://github.com/googlefonts/diffenator2) によるフォントの差分レポート
* original: [Morisawa BIZ UDGothic](https://github.com/googlefonts/morisawa-biz-ud-gothic) のコピー
* release: 帳票 UDPゴシック
* scripts: 生成スクリプトなど

## License

* フォント: [SIL Open Font License](https://openfontlicense.org/)
* scripts: [CC0](https://creativecommons.jp/sciencecommons/aboutcc0/)
