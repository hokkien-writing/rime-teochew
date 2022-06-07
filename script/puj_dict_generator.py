#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# 單韻母
vowel_dict = {
    'a': 'a', 'a2': 'á', 'a3': 'à', 'a5': 'â', 'a6': 'ã', 'a7': 'ā', 'a8': 'a̍',
    'e': 'e', 'e2': 'é', 'e3': 'è', 'e5': 'ê', 'e6': 'ẽ', 'e7': 'ē', 'e8': 'e̍',
    'i': 'i', 'i2': 'í', 'i3': 'ì', 'i5': 'î', 'i6': 'ĩ', 'i7': 'ī', 'i8': 'i̍',
    'o': 'o', 'o2': 'ó', 'o3': 'ò', 'o5': 'ô', 'o6': 'õ', 'o7': 'ō', 'o8': 'o̍',
    'u': 'u', 'u2': 'ú', 'u3': 'ù', 'u5': 'û', 'u6': 'ũ', 'u7': 'ū', 'u8': 'u̍',
    'ur': 'ṳ', 'ur2': 'ṳ́', 'ur3': 'ṳ̀', 'ur5': 'ṳ̂', 'ur6': 'ṳ̃', 'ur7': 'ṳ̄', 'ur8': 'ṳ̍',
    'ng': 'ng', 'ng2': 'ńg', 'ng3': 'ǹg', 'ng5': 'n̂g', 'ng6': 'ñg', 'ng7': 'n̄g', 'ng8': 'n̍g',
    'm': 'm', 'm2': 'ḿ', 'm3': 'm̀', 'm5': 'm̂', 'm6': 'm̃', 'm7': 'm̄',
    'nn': 'ⁿ',
}

head_list = [
    '',
    'p', 'ph', 'm', 'b',
    't', 'th', 'n', 'l',
    'k', 'kh', 'g', 'ng', 'h',
    'ts', 'tsh', 's', 'z',
    'ch', 'chh', 'j',
]

belly_list = [
    'a', 'e', 'i', 'o', 'u', 'ur',
    'ai', 'au', 'ia', 'ie', 'iu', 'oi', 'ou', 'ua', 'ue', 'ui',
    'iou', 'uai'
]

tail_list = [
    '',
    'nn', 'h', 'hnn', 'm', 'p', 'n', 't', 'ng', 'k'
]

tone_list = [
    '', '2', '3', '5', '6', '7', '8'
]


def generate():
    f = open('../teochew.dict.yaml', 'w')
    f.writelines('''# Rime dictionary
# encoding: utf-8
#
# Teochew PUJ 潮州白話字
#
---
name:	teochew
version:	"0.2"
sort:	by_weight
use_preset_vocabulary:	false
...
''')
    for head in head_list:
        for belly in belly_list:
            for tail in tail_list:
                for tone in tone_list:
                    if not exist(head, belly, tail, tone):
                        continue
                    l = head + add_tone(belly, tone)
                    if tail == 'nn':
                        l = l + vowel_dict['nn']
                    elif tail == 'hnn':
                        l = l + 'h' + vowel_dict['nn']
                    else:
                        l = l + tail
                    r = '%s%s%s%s' % (head, belly, tail, tone)
                    line = "%s\t%s\n" % (l, r)
                    line2 = "%s\t%s\n" % (l.capitalize(), r.capitalize())
                    f.write(line)
                    f.write(line2)
    # 補充 m,ng
    for tail in ['m', 'ng', 'M', 'Ng']:
        for tone in tone_list:
            r = tail + tone
            if r not in vowel_dict:
                continue
            l = vowel_dict[r]
            line = "%s\t%s\n" % (l, r)
            line2 = "%s\t%s\n" % (l.capitalize(), r.capitalize())
            f.write(line)
            f.write(line2)
    f.close()


def exist(head, belly, tail, tone):
    # ch,chh,j 只用於e，和i前面
    if head in ['ch', 'chh', 'j', 'Ch', 'Chh', 'J'] and not belly.startswith('e') and not belly.startswith('i'):
        return False
    # ts,tsh,z 只用於a、o、u、ur、m、ng前面
    if head in ['ts', 'tsh', 'z', 'Ts', 'Tsh', 'Z'] and not belly.startswith('a') and not belly.startswith(
            'o') and not belly.startswith('u') and not belly.startswith('ur') \
            and not belly.startswith('m') and not belly.startswith('ng'):
        return False
    # j,z 不用於三元音
    if head in ['j', 'z', "J", "Z"] and len(belly) == 3:
        return False

    # 促音結尾，tone只能是 '' 或 8
    if tail in ['h', 'hnn', 'p', 't', 'k'] and tone not in ['', '8']:
        return False
    if tail not in ['h', 'hnn', 'p', 't', 'k'] and tone == '8':
        return False
    # 三元音只有 ''、nn、h、hnn
    if len(belly) == 3 and tail not in ['', 'nn', 'h', 'hnn']:
        return False
    # uai 没有h
    if belly == 'uai' and tail == 'h':
        return False
    # ui 只有 '' 和 nn
    if belly == 'ui' and tail not in ['', 'nn']:
        return False
    # ue 不存在 m和p
    if belly == 'ue' and tail in ['m', 'p']:
        return False
    # ua 不存在 hnn, n, t
    if belly == 'ua' and tail in ['hnn', 'n', 't']:
        return False
    # ou only '' and nn
    if belly == 'ou' and tail not in ['', 'nn']:
        return False
    # oi only '',h and nn
    if belly == 'oi' and tail not in ['', 'h', 'nn']:
        return False
    # iu only '' and nn
    if belly == 'iu' and tail not in ['', 'nn']:
        return False
    # ia not hnn, m, p
    if belly in ['ia'] and tail in ['hnn', 'm', 'p', 'n', 't']:
        return False
    # ie not hnn,ng, k
    if belly == 'ie' and tail in ['hnn', 'ng', 'k']:
        return False
    # ai, au not m, p, t, n, ng, k
    if belly in ['ai', 'au'] and tail in ['m', 'p', 'n', 't', 'ng', 'k']:
        return False
    # u, ur not nn, hnn, m, p, ng, k
    if belly in ['u', 'ur'] and tail in ['nn', 'hnn', 'm', 'p', 'ng', 'k']:
        return False
    # o,e not n,t
    if belly in ['o', 'e'] and tail in ['m', 'p', 'n', 't']:
        return False
    # i not ng,k
    if belly == 'i' and tail in ['ng', 'k']:
        return False
    return True


def add_tone(belly, tone):
    if not belly:
        return ''
    if len(belly) == 1:
        return vowel_dict[belly + tone]
    # 注音優先級：a o u e i
    for v in ['a', 'o', 'ur', 'u', 'e', 'i']:
        pos = belly.find(v)
        if pos > -1:
            return belly[0:pos] + vowel_dict[v + tone] + belly[pos + len(v):len(belly)]


if __name__ == "__main__":
    generate()
    pass
