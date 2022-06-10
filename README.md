# rime-teochew（潮州話拍字方案）

```
【漢字】：各美其美，美美與共
【PUJ】：Kak múi khî múi, múi múi ṳ́-kāng
        Kak mí khî mí, mí mí ṳ́-kāng
```



本潮州話拍字方案包含漢字佮白話字，建基於 Rime 輸入法引擎，可在全平台（包括 Windows, Mac, Linux, iPhone 佮 Android）上拍字。

怎爾（tsò-nî）需要此款方案呢？聽我款爾（khuaⁿ-nî）道來。

在我細時，學堂無教潮州話，雖然老師有用潮州話教學，但是潮州話無在語文之列。一度，我認爲漢字是普通話專用，潮州話無便（bô-pièn）寫出來，只能借用漢字其普通話音來將就。例如：表達「自己」哩用「膠己」，表達「不要」哩用「賣」，表達「你」哩用「魯」。好似只能向普通話借了字音正能表達。

實際上，漢字並毋是普通話專用，北方官話、吳語、閩南語、粵語、客語、湘語等等攏用漢字，甚至日本、韓國、新加坡等等國家都囉使用漢字。一個漢字在南北諸語中可能毋同音，但是意思差毋多，在日語、韓語、越南語中也是如此。漢字神奇之處是一個字寫出來，不管是南方還是北方，中國還是其它漢字圈亓（āi）國家，儂能夠睇識（pat）。

但是大家儂攏知影，潮州話有簇字無便寫。若是用原有亓漢字來表記此簇字，很容易破壞漢字原有其意思，造成睇無甚至錯解；若是特意造字來表記，又會出現新造字其接受佮（kah）普及困難。

其實，147 年前已經有了解決方案。

遐（hiá）就是[潮州白話字](https://zh.wikipedia.org/wiki/%E6%BD%AE%E5%B7%9E%E7%99%BD%E8%A9%B1%E5%AD%97)。

潮州白話字（Tiê-chiu Pe̍h-ūe-jī）是潮州話亓羅馬字書寫系統， 從 1875 年英國傳教士汲约翰佮卓威廉制定「汕頭教會羅馬字」到今（taⁿ），已經有 147 年了。期間出版了酷㩼（hoh-tsōi）《聖經》譯本。彼（Hṳ́）時陣，白話字在民間生了根，儂用伊來寫信傳書。

現在稀罕了，也無儂教，建議大家儂通過[維基百科](https://zh.wikipedia.org/wiki/%E6%BD%AE%E5%B7%9E%E7%99%BD%E8%A9%B1%E5%AD%97)佮《[Handbook of the Swatow Vernacular](source/Handbook%20of%20the%20Swatow%20Vernacular.pdf)》家己學習，有其他資料補充更好。

漢字適合表意，一字之間包含豐富其意思，有長久亓傳承；白話字適合表音，也有上百年亓歷史。對於無便寫其字，既可訓用漢字，也可直接用白話字，至切莫用漢字音（無論是用普通話音還是潮州話音）來表記。此樣生正能各取其長，自由暢快正確亓表達。

頭前呾其「自己」，若是汝會曉漢字，應寫作「家己」，若是毋曉，寫作「ka-kī」或者「ka-tī」也可；「不要」應寫作「勿」（訓用）或「mài」；「你」應寫作「汝」或「lṳ́」。書寫規則非常簡單，有便寫漢字哩寫漢字，無便哩訓用或者寫白話字。

另外，爲了方便拍字，參照 [MTR](http://tappcdn.resources.teochew.pw/files/20170114001.pdf) 進行了以下調整：

1. 聲調採用數字輸入，但是1、4 調免拍，例如：拍「si3」會出現候選字「世 sì」；
2. 拍 ur 出 ṳ，例如：拍「lur2」出「汝 lṳ́」；
3. 拍 nn 出 ⁿ，例如：拍「ainn3」出「愛 àiⁿ」。

## 準備

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

下載直了後，汝再照下底掠 `teochew` 加入文件 `default.custom.yaml` 中亓 `schema_list` 哩算安裝好了。

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

## 參考

1. [潮州白話字-維基百科](https://zh.wikipedia.org/wiki/%E6%BD%AE%E5%B7%9E%E7%99%BD%E8%A9%B1%E5%AD%97)
2. [Handbook of the Swatow Vernacular](source/Handbook%20of%20the%20Swatow%20Vernacular.pdf)
