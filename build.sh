rm -rf build
mkdir -p build/teochew
cd build || return
git clone --depth 1 https://github.com/rime/rime-luna-pinyin.git
cd teochew || return
cp ../rime-luna-pinyin/*.yaml .
cp ../../*.yaml .
zip -r teochew.zip ./*
cp teochew.zip ../
