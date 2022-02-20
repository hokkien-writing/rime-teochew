# rime-teochew-puj

Rime / Teochew PUJ 潮州白話字拍字

[潮州白話字](https://zh.wikipedia.org/wiki/%E6%BD%AE%E5%B7%9E%E7%99%BD%E8%A9%B1%E5%AD%97) (Tiê-chiu Pe̍h-ūe-jī) 是潮州話 āi 羅馬字書寫系統， 從 1875 年英國傳教士汲约翰  kah 卓威廉制定「汕頭教會羅馬字」到 taⁿ，已經有 147 年了。期間出版了 hoh tsōi 《聖經》譯本。民間也有儂用白話字來書寫。

之後，電腦時代來了，白話字 oh 寫，進行改造，出現了各種版本。在我睇來，免改換，原因如下：

一、應該讓電腦來拍出我想拍 āi 字，而不是削足適履。本來雅雅好好 āi 字，無必要改來改去。例如：taⁿ 就是 taⁿ，無必要改作 tann、dan。再例如：ũ 就是 ũ，無必要改作 ǔ、u7。

二、這是文字，不是拼音，拼音常變，文字不改。就像英文 hièⁿ-seⁿ，各個地方有各個地方 āi 方音，但是寫出來是平樣 āi 文字。

漢字 kah 白話字 tsô-chet 是先人留落來 kāi 遺產，àiⁿ 好好珍惜 kah 運用，mó 捨掉任何一個。

## 前提

安裝輸入法程序，全平台 tsoh ũ，請訪問 [RIME | 中州韻輸入法引擎](https://rime.im/download/) 獲取對應平台程序並安裝先。

## 安裝

電腦端可使用 [東風破](https://github.com/rime/plum) 安裝：

``` shell
bash rime-install tsunhua/rime-teochew-poj
```

更通用 āi 方法是直接克隆倉庫，複製文件  `teochew_puj.dict.yaml` kah `teochew_puj.schema.yaml` 到用戶資料目錄下底。克隆倉庫命令：

```bash
git clone https://github.com/tsunhua/rime-teochew-poj.git
```

下載直了後，lṳ́ 再掠 `teochew-poj` 加入文件 `default.custom.yaml` 中 āi  `schema_list` 哩算安裝好了。照下底：

``` yaml
schema_list:
  - schema: luna_pinyin
  # 省略其他常用 āi 輸入方案
  - schema: teochew-poj # 添加潮語白話字
```

Nāⁿ-sĩ 無 `default.custom.yaml`  chí-kâi 文件，可照下底創建一個：

```yaml
# default.custom.yaml

patch:
  schema_list:
    - schema: luna_pinyin
    # 省略其他常用 āi 輸入方案
    - schema: teochew_puj # 添加潮語白話字
```

## 改進

Nāⁿ-sĩ lṳ́ 有 Github 帳號，來做夥改進，讓伊用緊更加順手。
