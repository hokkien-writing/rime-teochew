# rime-teochew

Rime / Teochew 潮州話拍字

本潮州話輸入方案包含漢字佮白話字，此兩者對於潮州話書寫都酷有幫助。

首先，漢字是表意文字，識別度很懸(kûiⁿ/kuâiⁿ)，有上千年其(kāi)傳承，一度中日韓越都用漢字交流。漢字其生命力在於其意涵，一字之間包含豐富其意思。若是用漢字來表音，實在是踏錯了步、行錯了路，白白糟蹋了漢字。

雖呾是漢字，有簇漢字其意思佮普通話其用法毋相同，例如：「生理」比之「生意」，「愛」比之「要」，者是正常其，敢敢去用，切莫妥協。妥協是一門語言行衰路其標誌，一直妥協一直衰。對於文字佮語言毋正確其認識愛糾正，漢字佮普通話愛解綁，漢字是漢字，普通話是普通話。漢字可以在普通話中用，也可以在潮州話中用，也可以在日語中用，還可以在韓語中用；普通話可以用漢字書寫，也可以用羅馬字書寫，甚至可以改用韓文書寫。各種語言對漢字其運用有所不同，平樣豐富着漢字生態。

呾(tàⁿ)到表音，白話字（羅馬字）最擅長了。乜其啊，汝無聽過白話字？來，容我來介紹下。

[潮州白話字](https://zh.wikipedia.org/wiki/%E6%BD%AE%E5%B7%9E%E7%99%BD%E8%A9%B1%E5%AD%97) (Tiê-chiu Pe̍h-ūe-jī) 是潮州話亓(āi)羅馬字書寫系統， 從 1875 年英國傳教士汲约翰佮卓威廉制定「汕頭教會羅馬字」到今(taⁿ)，已經有 147 年了。期間出版了酷㩼(hoh-tsōi)《聖經》譯本。Hṳ́時陣，白話字在民間生了根，儂用伊來寫信傳書。之後，因爲各種原因，用白話字其儂逐漸稀罕了。

既然如此，做呢咱愛來學習伊呢？頭前呾過，各取所長。

現此時，我採用漢羅混寫，即漢字佮白話字混寫亓形式來寫潮州話，原則是能用漢字表達清楚其哩用漢字，無便其哩用白話字。

```
【漢字】：各美其美，美美與共，毋是更好？
【PUJ】：Kak múi khî múi, múi múi ṳ́-kāng, m̃-sĩ kèng-hó?
        Kak mí khî mí, mí mí ṳ́-kāng, m̃-sĩ kèng-hó?
```

## 前提

安裝輸入法程序，全平台攏有，請訪問 [RIME | 中州韻輸入法引擎](https://rime.im/download/) 獲取對應平台程序並安裝先。

## 安裝

電腦端可使用 [東風破](https://github.com/rime/plum) 安裝：

``` shell
bash rime-install tsunhua/rime-teochew
```

更通用亓方法是直接克隆倉庫，複製文件  `teochew_puj.dict.yaml` kah `teochew_puj.schema.yaml` 到用戶資料目錄下底。克隆倉庫命令：

```bash
git clone https://github.com/tsunhua/rime-teochew.git
```

下載直了後，汝再掠 `teochew` 加入文件 `default.custom.yaml` 中亓 `schema_list` 哩算安裝好了。照下底：

``` yaml
schema_list:
  - schema: luna_pinyin
  # 省略其他常用亓輸入方案
  - schema: teochew # 添加潮州話
```

若是無 `default.custom.yaml` 此個文件，可照下底創建一個：

```yaml
# default.custom.yaml

patch:
  schema_list:
    - schema: luna_pinyin
    # 省略其他常用亓輸入方案
    - schema: teochew # 添加潮州話
```

## 改進

若是汝有 Github 帳號，來做夥改進，讓伊用緊更加順手。

## 致謝

1. [中州韻輸入法引擎](https://rime.im/)
2. [潮语拼音输入法](https://github.com/kahaani/dieghv)
