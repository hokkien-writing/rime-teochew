# rime-teochew（潮州話拍字方案）

![有閒來食茶](img/u-oinn-lai-chiah-te.gif)

```
【漢字】有閒來食茶
【PUJ】Ũ-ôiⁿ lâi chia̍h-tê
【拍字】uoinn lai chiahte
```

## 簡介

本潮州話拍字方案包含漢字佮白話字，建基於 Rime 輸入法引擎，可在全平台（包括 Windows, Mac, Linux, iPhone 佮 Android）上拍字。

## 緣起

Tsò-nī 需要此款方案呢？聽我款款呾來。

在我細時，學堂無教潮州話，雖然老師有用潮州話教學，但是潮州話無在語文之列。一度，我認爲漢字是普通話專用，潮州話無變寫出來，只能借用漢字其普通話音來將就。例如：表達「自己」哩用「膠己」，表達「不要」哩用「賣」，表達「你」哩用「魯」。好似只能向普通話借了字音正能表達。

實際上，漢字並毋是普通話專用，北方官話、吳語、閩南語、粵語、客語、湘語等等攏用漢字，甚至日本、韓國、新加坡等等國家都囉使用漢字。一個漢字在南北諸語中可能毋同音，但是意思攏差毋多，在日語、韓語、越南語中也是如此。漢字神奇之處是一個字寫出來，無論是南方還是北方，中國還是漢字圈內其它國家，儂有變睇會識（pat）。

但是大家儂攏知影，潮州話有簇字無變用漢字來寫。若是借用漢字音來表記此簇字，很容易破壞漢字原有其意思，造成睇無甚至錯解；若是特意造字來表記，又會出現新字其接受佮普及困難。

其實，差毋多一個半世紀前已經有了解決方案。

Hiá 就是[潮州白話字](https://zh.wikipedia.org/wiki/%E6%BD%AE%E5%B7%9E%E7%99%BD%E8%A9%B1%E5%AD%97)。

潮州白話字（Tiê-chiu Pe̍h-ūe-jī），簡稱 PUJ，是潮州話其羅馬字書寫系統，最早是 1875 年英國傳教士汲约翰佮卓威廉制定其「汕頭教會羅馬字」。之後出版了酷㩼《聖經》譯本。彼時陣，白話字在民間生了根，儂用伊來寫信傳書。

PUJ 今稀見囉，推薦大家儂透過[簡明潮州白話字](https://hokkien-writing.github.io/simple_puj/) 家己學習。

漢字適合表意，一字之間包含豐富其意思，有長久其傳承；白話字適合表音，也有上百年其歷史。對於無變寫其字，既可訓用漢字，也可直接用白話字，至切 mó用漢字音（無論是用普通話音還是潮州話音）來表記。此樣生正能各取其長，自由暢快正確其表達。

頭前呾其「自己」，若是汝會曉漢字，應寫作「家己」，若是毋曉，寫作「ka-kī」或者「ka-tī」也可；「不要」應寫作「勿」（訓用）或「mài」；「你」應寫作「汝」或「lṳ́」。書寫規則非常簡單，有變寫漢字哩寫漢字，無變哩訓用或者寫白話字。

## 安裝

安裝輸入法程序，全平台攏有，請訪問 [RIME | 中州韻輸入法引擎](https://rime.im/download/) 獲取對應平台程序並安裝先。

電腦端可使用 [東風破](https://github.com/rime/plum) 安裝，命令如下：

``` shell
bash rime-install hokkien-writing/rime-teochew
```

更通用其方法是直接克隆倉庫：

```bash
git clone https://github.com/hokkien-writing/rime-teochew.git
```

然後複製下底三個文件到用戶資料目錄：

1. `teochew.puj.dict.yaml`
2. `teochew.han.dict.yaml`
3. `teochew.schema.yaml` 

再來，照下底掠 `teochew` 加入文件 `default.custom.yaml` 中其 `schema_list`：

``` yaml
schema_list:
  - schema: luna_pinyin
  # 省略其他常用其輸入方案
  - schema: teochew # 添加潮州話
```

若是無 `default.custom.yaml` 此個文件，可照下底創建一個：

```yaml
# default.custom.yaml

patch:
  schema_list:
    - schema: luna_pinyin
    # 省略其他常用其輸入方案
    - schema: teochew # 添加潮州話
```

至此，安裝直。


## 使用

1. 本方案用字遵從 [hokkien-writing/teochew-character](https://github.com/hokkien-writing/teochew-character) 項目。
2. 聲調免拍。如愛拍出「來」，應拍 `lai` 而毋是 `lai5`。
2. 連字符免拍。如愛拍出「食茶」，應拍 `chiahte` 而毋是 `chiah-te`。
3. 拍 `ur` 出「ṳ」。如愛拍出「汝」或「lṳ́」，應拍 `lur`。
4. 拍 `nn` 出「ⁿ」。如愛拍出「愛」或「àiⁿ」，應拍 `ainn`。

## 相輔

若是汝有 Github 帳號，來做夥改進，讓伊用緊更加順手。

1. 對於輸入法方面，請直接修改 `*.schema.yaml` 文件並提交 PR。
2. 對於用字方面，請轉 [hokkien-writing/teochew-character](https://github.com/hokkien-writing/teochew-character) 項目進行修改後再提交 PR 修改 `*.dict.yaml` 文件。

## 參考

1. [中州韻輸入法引擎](https://rime.im/)
2. [簡明潮州白話字](https://hokkien-writing.github.io/simple_puj/)
3. [潮州白話字-維基百科](https://zh.wikipedia.org/wiki/%E6%BD%AE%E5%B7%9E%E7%99%BD%E8%A9%B1%E5%AD%97)
4. [MTR](http://tappcdn.resources.teochew.pw/files/20170114001.pdf)
5. [潮语拼音输入法](https://github.com/kahaani/dieghv)
6. [hokkien-writing/teochew-character](https://github.com/hokkien-writing/teochew-character)
