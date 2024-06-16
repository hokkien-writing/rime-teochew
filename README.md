# rime-teochew（潮州話拍字方案）

![拍字效果](assets/u-oinn-lai-chiah-te.GIF)

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

潮州白話字（Tiê-chiu Pe̍h-ūe-jī），簡稱 PUJ，是潮州話其羅馬字書寫系統，最早是 1875
年英國傳教士汲约翰佮卓威廉制定其「汕頭教會羅馬字」。之後出版了酷㩼《聖經》譯本。彼時陣，白話字在民間生了根，儂用伊來寫信傳書。

PUJ 今罕見囉，推薦大家儂透過[簡明潮州白話字](https://hokkien-writing.github.io/simple_puj/) 家己學習。

漢字適合表意，一字之間包含豐富其意思，有長久其傳承；白話字適合表音，也有上百年其歷史。對於無變寫其字，既可訓用漢字，也可直接用白話字，至切
mó用漢字音（無論是用普通話音還是潮州話音）來表記。此樣生正能各取其長，自由暢快正確其表達。

頭前呾其「自己」，若是汝會曉漢字，應寫作「家己」，若是毋曉，寫作「ka-kī」或者「ka-tī」也可；「不要」應寫作「勿」（訓用）或「mài」；「你」應寫作「汝」或「lṳ́」。書寫規則非常簡單，有變寫漢字哩寫漢字，無變哩訓用或者寫白話字。

## 安裝

### 在電腦上

若電腦是視窗系統(Windows)，推薦「[小狼毫](https://rime.im/download/)」，請使用默認軟件目錄，安裝了後在終端執行下底命令快速配置：

```bash
# 下載潮州話拍字方案
curl -LO https://github.com/hokkien-writing/rime-teochew/archive/master.zip
# 解壓並複製方案到鼠鬚管配置目錄
unzip master.zip
cp -f rime-teochew-master/*.yaml %APPDATA%\Rime
```

然後點擊 `開始菜單` > `【小狼毫】重新部署`。

若是蘋果系統(MacOS)，推薦「[鼠鬚管](https://rime.im/download/)」，安裝了後在終端執行下底命令快速配置：

```bash
# 下載潮州話拍字方案
curl -LO https://github.com/hokkien-writing/rime-teochew/archive/master.zip
# 解壓並複製方案到鼠鬚管配置目錄
unzip master.zip
cp -f rime-teochew-master/*.yaml ~/Library/Rime
# 重新部署
/Library/Input\ Methods/Squirrel.app/Contents/MacOS/Squirrel --reload
```

Linux系統其就免加句囉，參考 [RIME官網](https://rime.im/download/) 來安裝。

### 在手機上

若手機是蘋果系統(IOS)，推薦「[倉輸入法](https://apps.apple.com/cn/app/仓输入法/id6446617683)」，安裝後按照下底視頻配置。

📀 視頻可往 [微軟雲盤](https://1drv.ms/f/s!AgqX3Jd3VLa4gS3ujqPC7hpY4lKt?e=Wc8xvk) | [阿里雲盤](https://www.alipan.com/s/UpgDQ19iLSi)  查睇。

若是不便，也可微信掃碼關注下底視頻號來睇。

> 微信視頻號-不輟集：
> ![微信視頻號-不輟集](assets/微信視頻號-不輟集.jpeg)

若是安卓系統(Android)，推薦「[同文輸入法]((https://f-droid.org/packages/com.osfans.trime/) )」。

> 📌 頭頂軟件及拍字方案爲方便取用，已另存到了 [微軟雲盤](https://1drv.ms/f/s!AgqX3Jd3VLa4gS3ujqPC7hpY4lKt?e=Wc8xvk) | [阿里雲盤](https://www.alipan.com/s/UpgDQ19iLSi) ，可作爲備用。

## 使用

1. 本方案用字遵從 [潮州話詞庫](https://github.com/hokkien-writing/teochew-lexicon) 項目。
2. 聲調免拍。如欲拍出「來」，應拍 `lai` 而毋是 `lai5`。
3. 連字符免拍。如欲拍出「食茶」，應拍 `chiahte` 而毋是 `chiah-te`。 
4. 拍 `ur` 出「ṳ」。如欲拍出「汝」或「lṳ́」，應拍 `lur`。 
5. 拍 `nn` 出「ⁿ」。如欲拍出「愛」或「àiⁿ」，應拍 `ainn`。 
6. 默認顯示 8 個詞候選，按左右中括號（`[`、`]`）可以掀來掀去。 
7. 支持**潮州音查詢**，按一下 ` f `  鍵，接落輸入普通話拼音就可以睇着潮州音啦。 
8. 支持**地道用詞查詢**，按一下 ` v `  鍵，接落輸入普通話拼音就可以睇着潮州話其地道用詞啦。
9. 支持簡拼，拍 `lh` 出「汝好」。
10. 電腦上按 `F4` 鍵選擇各款輸入方案，可切換到**純PUJ**，或配置簡體、西文標點、全角等。

> 📌若是有字顯示袂出，請參考[閩語參考資料-字體](https://hokkien-writing.github.io/#%F0%9F%88%9A%EF%B8%8F-%E5%AD%97%E9%AB%94)安裝擴展字體。

> 潮州音查詢效果：
> ![潮州音查詢效果](assets/tiechiuim.GIF)

> 地道用詞查詢效果：
> ![地道用詞查詢效果](assets/titau.GIF)

## 相輔

若是汝有 Github 帳號，來做夥改進，讓伊用緊更加順手如意。

1. 對於輸入法方面，請直接修改 `*.schema.yaml` 文件並提交 PR。
2. 對於用字方面，請轉 [潮州話詞庫](https://github.com/hokkien-writing/teochew-lexicon) 項目進行修改。

## 參考

1. [簡明潮州白話字](https://hokkien-writing.github.io/simple_puj/)
2. [潮州話詞庫](https://github.com/hokkien-writing/teochew-lexicon)
3. [潮州白話字-維基百科](https://zh.wikipedia.org/wiki/%E6%BD%AE%E5%B7%9E%E7%99%BD%E8%A9%B1%E5%AD%97)
4. [MTR](http://tappcdn.resources.teochew.pw/files/20170114001.pdf)
5. [潮语拼音输入法](https://github.com/kahaani/dieghv)
6. [中州韻輸入法引擎](https://rime.im/)
