# rime-teochew-puj

Rime / Teochew PUJ 潮州白話字拍字

[潮州白話字](https://zh.wikipedia.org/wiki/%E6%BD%AE%E5%B7%9E%E7%99%BD%E8%A9%B1%E5%AD%97) (Tiê-chiu Pe̍h-ūe-jī) 是潮州話 āi 羅馬字書寫系統， 從 1875 年英國傳教士汲约翰  kah 卓威廉制定「汕頭教會羅馬字」到 taⁿ，已經有 147 年了。期間出版了 hoh tsōi 《聖經》譯本。Hṳ́ 時陣，白話字在民間生了根，儂用伊來寫信傳書。

之後，電腦時代來了。白話字 oh 寫，儂哩想著改造，出現了各種版本。在我睇來，nán 免改換，原因如下：

一、應該讓電腦來拍出我想拍 āi 字，而不是削足適履。本來雅雅好好 āi 字，無必要改來改去。例如：taⁿ 就是 taⁿ，無必要改作 tann、dan。再如：ũ 就是 ũ，無必要改作 ǔ、u6。

二、chí 是文字，毋是拼音，拼音常變，文字不改。就像英文 hièⁿ-seⁿ，各個地方有各個地方 āi 方音，但是寫出來是平樣 āi 文字。

現此時，我採用漢羅混寫，即漢字 kah 白話字混寫 kāi 形式。因爲潮州話是古漢語化石，伊存古 āi 另一面是長期脫離主流，乞視爲土話，不登大雅之堂，致使一寡字無規範漢字可寫。有儂用同音字、僻字、正字還有拼音來寫，我攏寫毋順，毋是毋雅觀，就是過 oh 寫，還有更致命 āi 是讓儂誤解。Chí-miá nán 有白話字，用漢字寫毋順時用白話字來寫，毋是更好？

## 前提

安裝輸入法程序，全平台 tsoh ũ，請訪問 [RIME | 中州韻輸入法引擎](https://rime.im/download/) 獲取對應平台程序並安裝先。

## 安裝

電腦端可使用 [東風破](https://github.com/rime/plum) 安裝：

``` shell
bash rime-install tsunhua/rime-teochew-puj
```

更通用 āi 方法是直接克隆倉庫，複製文件  `teochew_puj.dict.yaml` kah `teochew_puj.schema.yaml` 到用戶資料目錄下底。克隆倉庫命令：

```bash
git clone https://github.com/tsunhua/rime-teochew-puj.git
```

下載直了後，lṳ́ 再掠 `teochew-puj` 加入文件 `default.custom.yaml` 中 āi  `schema_list` 哩算安裝好了。照下底：

``` yaml
schema_list:
  - schema: luna_pinyin
  # 省略其他常用 āi 輸入方案
  - schema: teochew-puj # 添加潮州白話字
```

Nāⁿ-sĩ 無 `default.custom.yaml`  chí-kâi 文件，可照下底創建一個：

```yaml
# default.custom.yaml

patch:
  schema_list:
    - schema: luna_pinyin
    # 省略其他常用 āi 輸入方案
    - schema: teochew_puj # 添加潮州白話字
```

## 改進

Nāⁿ-sĩ lṳ́ 有 Github 帳號，來做夥改進，讓伊用緊更加順手。
