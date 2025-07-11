from collections import defaultdict
pillar_melody_dic = {
    '甲子' : '海中金',
    '乙丑' : '海中金',
    '丙寅' : '炉中火',
    '丁卯' : '炉中火',
    '戊辰' : '大林木',
    '己巳' : '大林木',
    '庚午' : '路旁土',
    '辛未' : '路旁土',
    '壬申' : '剑锋金',
    '癸酉' : '剑锋金',
    '甲戌' : '山头火',
    '乙亥' : '山头火',
    '丙子' : '涧下水',
    '丁丑' : '涧下水',
    '戊寅' : '城墙土',
    '己卯' : '城墙土',
    '庚辰' : '白蜡金',
    '辛巳' : '白蜡金',
    '壬午' : '杨柳木',
    '癸未' : '杨柳木',
    '甲申' : '泉中水',
    '乙酉' : '泉中水',
    '丙戌' : '屋上土',
    '丁亥' : '屋上土',
    '戊子' : '霹雳火',
    '己丑' : '霹雳火',
    '庚寅' : '松柏木',
    '辛卯' : '松柏木',
    '壬辰' : '长流水',
    '癸巳' : '长流水',
    '甲午' : '沙中金',
    '乙未' : '沙中金',
    '丙申' : '山下火',
    '丁酉' : '山下火',
    '戊戌' : '平地木',
    '己亥' : '平地木',
    '庚子' : '壁上土',
    '辛丑' : '壁上土',
    '壬寅' : '金箔金',
    '癸卯' : '金箔金',
    '甲辰' : '佛灯火',
    '乙巳' : '佛灯火',
    '丙午' : '天河水',
    '丁未' : '天河水',
    '戊申' : '大驿土',
    '己酉' : '大驿土',
    '庚戌' : '钗钏金',
    '辛亥' : '钗钏金',
    '壬子' : '桑松木',
    '癸丑' : '桑松木',
    '甲寅' : '大溪水',
    '乙卯' : '大溪水',
    '丙辰' : '沙中土',
    '丁巳' : '沙中土',
    '戊午' : '天上火',
    '己未' : '天上火',
    '庚申' : '石榴木',
    '辛酉' : '石榴木',
    '壬戌' : '大海水',
    '癸亥' : '大海水'
}

melody_pillar_dic = defaultdict(list)
for pillar, melody in pillar_melody_dic.items():
    #if melody not in melody_pillar_dic:
    #    melody_pillar_dic[melody] = [pillar]
    #else:
    melody_pillar_dic[melody].append(pillar)

pillar = list(pillar_melody_dic.keys())
melody = list(melody_pillar_dic.keys())

nobel_man_forward = {
    "甲":["丑", "未"],
    "乙":["子", "申"],
    "丙":["亥", "酉"],
    "丁":["亥", "酉"],
    "戊":["丑", "未"],
    "己":["子", "申"],
    "庚":["寅", "午"],
    "辛":["寅", "午"],
    "壬":["卯", "巳"],
    "癸":["卯", "巳"]
}

nobel_man_backward = {
    "寅":["庚", "辛"],
    "卯":["壬", "癸"],
    "巳":["壬", "癸"],
    "午":["庚", "辛"],
    "未":["甲", "戊"],
    "申":["乙", "己"],
    "酉":["丙", "丁"],
    "亥":["丙", "丁"],
    "子":["乙", "己"],
    "丑":["甲", "戊"],
}

sky = list(nobel_man_forward.keys())
ground = list(nobel_man_backward.keys())

color_dic = {
    "甲":'<span style="color:green">甲</span>',
    "乙":'<span style="color:green">乙</span>',
    "丙":'<span style="color:red">丙</span>',
    "丁":'<span style="color:red">丁</span>',
    "戊":'<span style="color:brown">戊</span>',
    "己":'<span style="color:brown">己</span>',
    "庚":'<span style="color:yellow">庚</span>',
    "辛":'<span style="color:yellow">辛</span>',
    "壬":'<span style="color:blue">壬</span>',
    "癸":'<span style="color:blue">癸</span>',
    "寅":'<span style="color:green">寅</span>',
    "卯":'<span style="color:green">卯</span>',
    "辰":'<span style="color:brown">辰</span>',
    "巳":'<span style="color:red">巳</span>',
    "午":'<span style="color:red">午</span>',
    "未":'<span style="color:brown">未</span>',
    "申":'<span style="color:yellow">申</span>',
    "酉":'<span style="color:yellow">酉</span>',
    "戌":'<span style="color:brown">戌</span>',
    "亥":'<span style="color:blue">亥</span>',
    "子":'<span style="color:blue">子</span>',
    "丑":'<span style="color:brown">丑</span>',
}

