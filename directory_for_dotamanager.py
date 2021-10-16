from typing import Dict, Union, Any, List

LuckyTeam = ['-', 'sleepylyana', 'm00dy', 'cupervladik', 'pudGG', 'vangeron']
Napalm = ['-', 'kuokuo', 'YC', 'Cveen', 'RaGen', 'MTD']
Bibisi = ['-', 'yabuki', 'light', 'muslimshady', 'bibis', 'пажылойлизгин']
TeamSincere = ['-', '野比大熊猫', '咩撒嘎', '爱赢不赢', '迪士尼在逃丑大鸭', '天气好热']
depressedteam = ['-', '17', 'backpack of pain', 'boogi', 'iamfear', 'vxrvdx']
UFO = ['-', 'top1mider', 'тыконечнонефильм', 'speaker', 'white322', 'мастершифу']
Nasos = ['-', 'lovemydaughter', 'neymexa', 'DDDDDD', 'CR7', 'Yeljke']
oy_dyad = ['-', 'taketheelevator', 'July', 'orphan of kos', 'руинер и весельчак', 'shkolnikterrorist']
Spark = ['-', 'warcry', 'андрейэтоя', 'Path', 'dc', 'NIRVANA']
M_and_Ms = ['-', 'Pushistik', '2', 'El Capone', 'sad sad sad', 'играю до 1 луза']
AnimeSquad = ['-', '1 or feed', 'Mell', 'be my dog', 'DLC', 'blu3']
KompasGaming = ['-', 'chacha', 'смотрю на тебя', 'dir', '321', 'sup']
zerokgaming = ['-', 'trollge', 'fsd', 'mzs', 'shadow', 'Karma']
ferzee = ['-', 'qwe', 'blink', 'qq wp', 'pepe', 'Mikasa']
SeaTide = ['-', '?', 'cat', 'JIM', 'Pier', 'Atlas']
DX = ['-', 'idinahui', 'trash', 'mistadream', 'j1o', 'the enjoyer']
ghoul = ['-', 'nove', 'luck', 'misuqi', 'onlydrinkcoffee', 'wolfy!']
CrowCrowd = ['-', 'hemeow', 'an.apple', 'marz', 'pichu', 'False Promise']
Digital_Company = ['-', "it's ok", 'qod', 'crazykiller', 'EMP', 'coffeems']
SeaOne = ['-', 'odhako', 'reality', 'shifear', 'ByeTheCore', 'tibosha']
Quantic_Lucky = ['-', 'у моей охраны есть охрана', 'therion', 'Lfor', 'Disaster', 'Q.Yo(retrostyle)']
onepercent = ['-', 'stoneremnant', 'Sherk', 'bonchinche', 'поцелуйвгузно', 'подруга подруг']
Quantic_Young = ['-', 'valvarn', 'maslenok', 'iequa', 'denjke', 'Q.Yo']
KirieshkaTeam = ['-', 'username', '?emptember', 'psibladeheaven', 'dodik', 'player']
Sixty = ['-', 'hanaye', 'madara', '2ez4me', 'karma', 'bOy!']
Velum = ['-', 'skvermas', 'Oleja', 'AemTheBest', 'DreamKG', 'Kutbic']
Tidehunterdamage = ['-', 'areyoudeadyet?', 'донная мощь', 'grievous', 'otlichnik', 'tokyorudge']
OverKek = ['-', 'chevo', 'fucktwelve', 'тюбикмамкин', '95_gungster_95', 'lul kek']

# Характеристики игроков
team_playing = {'sleepylyana': 18, 'm00dy': 84, 'cupervladik': 95, 'pudGG': 94, 'vangeron': 36,
                'kuokuo': 42, 'YC': 42, 'Cveen': 40, 'RaGen': 67, 'MTD': 51,
                'yabuki': 93, 'light': 98, 'muslimshady': 54, 'bibis': 91, 'пажылойлизгин': 13,
                '野比大熊猫': 19, '咩撒嘎': 64, '爱赢不赢': 78, '迪士尼在逃丑大鸭': 4, '天气好热': 98,
                '17': 34, 'backpack of pain': 73, 'boogi': 98, 'iamfear': 58, 'vxrvdx': 24,
                'top1mider': 51, 'тыконечнонефильм': 89, 'speaker': 60, 'white322': 10, 'мастершифу': 82,
                'lovemydaughter': 96, 'neymexa': 90, 'DDDDDD': 1, 'CR7': 24, 'Yeljke': 54,
                'taketheelevator': 45, 'July': 55, 'orphan of kos': 3, 'руинер и весельчак': 73,
                'shkolnikterrorist': 55,
                'warcry': 68, 'андрейэтоя': 69, 'Path': 48, 'dc': 25, 'NIRVANA': 78,
                'Pushistik': 58, '2': 57, 'El Capone': 47, 'sad sad sad': 2, 'играю до 1 луза': 55,
                '1 or feed': 22, 'Mell': 12, 'be my dog': 85, 'DLC': 88, 'blu3': 61,
                'chacha': 64, 'смотрю на тебя': 63, 'dir': 69, '321': 14, 'sup': 7,
                'trollge': 76, 'fsd': 26, 'mzs': 79, 'shadow': 51, 'Karma': 79,
                'qwe': 75, 'blink': 33, 'qq wp': 20, 'pepe': 28, 'Mikasa': 52,
                '?': 72, 'cat': 24, 'JIM': 22, 'Pier': 33, 'Atlas': 60,
                'idinahui': 51, 'trash': 90, 'mistadream': 74, 'j1o': 46, 'the enjoyer': 54,
                'nove': 89, 'luck': 65, 'misuqi': 35, 'onlydrinkcoffee': 74, 'wolfy!': 45,
                'hemeow': 82, 'an.apple': 3, 'marz': 82, 'pichu': 49, 'False Promise': 53,
                "it's ok": 33, 'qod': 85, 'crazykiller': 31, 'EMP': 69, 'coffeems': 18,
                'odhako': 51, 'reality': 61, 'shifear': 82, 'ByeTheCore': 92, 'tibosha': 56,
                'у моей охраны есть охрана': 15, 'therion': 65, 'Lfor': 77, 'Disaster': 23, 'Q.Yo(retrostyle)': 40,
                'stoneremnant': 95, 'Sherk': 10, 'bonchinche': 45, 'поцелуйвгузно': 8, 'подруга подруг': 17,
                'valvarn': 76, 'maslenok': 49, 'iequa': 22, 'denjke': 34, 'Q.Yo': 33,
                'username': 70, '?emptember': 86, 'psibladeheaven': 58, 'dodik': 85, 'player': 47,
                'hanaye': 98, 'madara': 73, '2ez4me': 22, 'karma': 20, 'bOy!': 13,
                'skvermas': 55, 'Oleja': 37, 'AemTheBest': 44, 'DreamKG': 92, 'Kutbic': 31,
                'areyoudeadyet?': 57, 'донная мощь': 62, 'grievous': 87, 'otlichnik': 87, 'tokyorudge': 22,
                'chevo': 15, 'fucktwelve': 100, 'тюбикмамкин': 23, '95_gungster_95': 69, 'lul kek': 36}
solo_skill = {'sleepylyana': 6, 'm00dy': 99, 'cupervladik': 56, 'pudGG': 58, 'vangeron': 56,
              'kuokuo': 28, 'YC': 85, 'Cveen': 72, 'RaGen': 16, 'MTD': 36,
              'yabuki': 72, 'light': 8, 'muslimshady': 36, 'bibis': 82, 'пажылойлизгин': 63,
              '野比大熊猫': 54, '咩撒嘎': 80, '爱赢不赢': 63, '迪士尼在逃丑大鸭': 54, '天气好热': 80,
              '17': 77, 'backpack of pain': 91, 'boogi': 84, 'iamfear': 99, 'vxrvdx': 19,
              'top1mider': 89, 'тыконечнонефильм': 7, 'speaker': 61, 'white322': 9, 'мастершифу': 96,
              'lovemydaughter': 94, 'neymexa': 2, 'DDDDDD': 79, 'CR7': 23, 'Yeljke': 88,
              'taketheelevator': 61, 'July': 42, 'orphan of kos': 32, 'руинер и весельчак': 63, 'shkolnikterrorist': 57,
              'warcry': 12, 'андрейэтоя': 37, 'Path': 41, 'dc': 31, 'NIRVANA': 71,
              'Pushistik': 45, '2': 84, 'El Capone': 95, 'sad sad sad': 67, 'играю до 1 луза': 11,
              '1 or feed': 14, 'Mell': 11, 'be my dog': 83, 'DLC': 82, 'blu3': 47,
              'chacha': 34, 'смотрю на тебя': 49, 'dir': 5, '321': 13, 'sup': 17,
              'trollge': 53, 'fsd': 47, 'mzs': 54, 'shadow': 59, 'Karma': 27,
              'qwe': 5, 'blink': 12, 'qq wp': 40, 'pepe': 30, 'Mikasa': 24,
              '?': 42, 'cat': 4, 'JIM': 26, 'Pier': 13, 'Atlas': 54,
              'idinahui': 55, 'trash': 62, 'mistadream': 71, 'j1o': 57, 'the enjoyer': 52,
              'nove': 79, 'luck': 46, 'misuqi': 18, 'onlydrinkcoffee': 99, 'wolfy!': 3,
              'hemeow': 76, 'an.apple': 20, 'marz': 52, 'pichu': 90, 'False Promise': 33,
              "it's ok": 93, 'qod': 9, 'crazykiller': 11, 'EMP': 34, 'coffeems': 57,
              'odhako': 82, 'reality': 82, 'shifear': 2, 'ByeTheCore': 16, 'tibosha': 3,
              'у моей охраны есть охрана': 63, 'therion': 80, 'Lfor': 91, 'Disaster': 15, 'Q.Yo(retrostyle)': 36,
              'stoneremnant': 20, 'Sherk': 89, 'bonchinche': 74, 'поцелуйвгузно': 69, 'подруга подруг': 63,
              'valvarn': 80, 'maslenok': 7, 'iequa': 68, 'denjke': 96, 'Q.Yo': 21,
              'username': 96, '?emptember': 29, 'psibladeheaven': 49, 'dodik': 2, 'player': 88,
              'hanaye': 5, 'madara': 95, '2ez4me': 8, 'karma': 13, 'bOy!': 8,
              'skvermas': 50, 'Oleja': 27, 'AemTheBest': 54, 'DreamKG': 95, 'Kutbic': 79,
              'areyoudeadyet?': 10, 'донная мощь': 54, 'grievous': 36, 'otlichnik': 47, 'tokyorudge': 11,
              'chevo': 95, 'fucktwelve': 61, 'тюбикмамкин': 29, '95_gungster_95': 1, 'lul kek': 18}
skill_on_his_pose = {'sleepylyana': 93, 'm00dy': 77, 'cupervladik': 93, 'pudGG': 65, 'vangeron': 91,
                     'kuokuo': 71, 'YC': 51, 'Cveen': 54, 'RaGen': 64, 'MTD': 71,
                     'yabuki': 84, 'light': 96, 'muslimshady': 72, 'bibis': 99, 'пажылойлизгин': 56,
                     '野比大熊猫': 77, '咩撒嘎': 81, '爱赢不赢': 58, '迪士尼在逃丑大鸭': 70, '天气好热': 67,
                     '17': 73, 'backpack of pain': 71, 'boogi': 76, 'iamfear': 66, 'vxrvdx': 83,
                     'top1mider': 65, 'тыконечнонефильм': 76, 'speaker': 100, 'white322': 71, 'мастершифу': 95,
                     'lovemydaughter': 85, 'neymexa': 35, 'DDDDDD': 50, 'CR7': 11, 'Yeljke': 53,
                     'taketheelevator': 62, 'July': 94, 'orphan of kos': 91, 'руинер и весельчак': 73,
                     'shkolnikterrorist': 83,
                     'warcry': 61, 'андрейэтоя': 92, 'Path': 79, 'dc': 93, 'NIRVANA': 84,
                     'Pushistik': 94, '2': 93, 'El Capone': 94, 'sad sad sad': 67, 'играю до 1 луза': 85,
                     '1 or feed': 62, 'Mell': 72, 'be my dog': 78, 'DLC': 62, 'blu3': 77,
                     'chacha': 96, 'смотрю на тебя': 55, 'dir': 80, '321': 63, 'sup': 55,
                     'trollge': 56, 'fsd': 67, 'mzs': 57, 'shadow': 76, 'Karma': 64,
                     'qwe': 88, 'blink': 67, 'qq wp': 81, 'pepe': 100, 'Mikasa': 88,
                     '?': 63, 'cat': 73, 'JIM': 52, 'Pier': 61, 'Atlas': 67,
                     'idinahui': 55, 'trash': 70, 'mistadream': 86, 'j1o': 73, 'the enjoyer': 52,
                     'nove': 71, 'luck': 96, 'misuqi': 97, 'onlydrinkcoffee': 85, 'wolfy!': 88,
                     'hemeow': 65, 'an.apple': 86, 'marz': 74, 'pichu': 61, 'False Promise': 90,
                     "it's ok": 100, 'qod': 74, 'crazykiller': 57, 'EMP': 81, 'coffeems': 58,
                     'odhako': 51, 'reality': 69, 'shifear': 87, 'ByeTheCore': 82, 'tibosha': 93,
                     'у моей охраны есть охрана': 96, 'therion': 52, 'Lfor': 61, 'Disaster': 63, 'Q.Yo(retrostyle)': 82,
                     'stoneremnant': 86, 'Sherk': 65, 'bonchinche': 64, 'поцелуйвгузно': 60, 'подруга подруг': 82,
                     'valvarn': 83, 'maslenok': 59, 'iequa': 64, 'denjke': 73, 'Q.Yo': 55,
                     'username': 68, '?emptember': 96, 'psibladeheaven': 57, 'dodik': 77, 'player': 69,
                     'hanaye': 94, 'madara': 50, '2ez4me': 51, 'karma': 73, 'bOy!': 73,
                     'skvermas': 60, 'Oleja': 59, 'AemTheBest': 68, 'DreamKG': 66, 'Kutbic': 68,
                     'areyoudeadyet?': 56, 'донная мощь': 99, 'grievous': 56, 'otlichnik': 63, 'tokyorudge': 100,
                     'chevo': 60, 'fucktwelve': 65, 'тюбикмамкин': 90, '95_gungster_95': 67, 'lul kek': 98}
logic = {'sleepylyana': 28, 'm00dy': 68, 'cupervladik': 22, 'pudGG': 44, 'vangeron': 3,
         'kuokuo': 8, 'YC': 76, 'Cveen': 3, 'RaGen': 85, 'MTD': 6,
         'yabuki': 13, 'light': 97, 'muslimshady': 23, 'bibis': 13, 'пажылойлизгин': 29,
         '野比大熊猫': 42, '咩撒嘎': 10, '爱赢不赢': 41, '迪士尼在逃丑大鸭': 25, '天气好热': 80,
         '17': 23, 'backpack of pain': 13, 'boogi': 40, 'iamfear': 56, 'vxrvdx': 80,
         'top1mider': 100, 'тыконечнонефильм': 16, 'speaker': 56, 'white322': 62, 'мастершифу': 74,
         'lovemydaughter': 62, 'neymexa': 99, 'DDDDDD': 90, 'CR7': 1, 'Yeljke': 35,
         'taketheelevator': 74, 'July': 30, 'orphan of kos': 19, 'руинер и весельчак': 3, 'shkolnikterrorist': 80,
         'warcry': 40, 'андрейэтоя': 60, 'Path': 42, 'dc': 60, 'NIRVANA': 61,
         'Pushistik': 38, '2': 22, 'El Capone': 97, 'sad sad sad': 84, 'играю до 1 луза': 71,
         '1 or feed': 96, 'Mell': 78, 'be my dog': 88, 'DLC': 28, 'blu3': 100,
         'chacha': 15, 'смотрю на тебя': 18, 'dir': 87, '321': 2, 'sup': 75,
         'trollge': 82, 'fsd': 62, 'mzs': 65, 'shadow': 85, 'Karma': 97,
         'qwe': 93, 'blink': 28, 'qq wp': 98, 'pepe': 20, 'Mikasa': 84,
         '?': 42, 'cat': 27, 'JIM': 46, 'Pier': 15, 'Atlas': 95,
         'idinahui': 25, 'trash': 91, 'mistadream': 52, 'j1o': 55, 'the enjoyer': 72,
         'nove': 96, 'luck': 98, 'misuqi': 46, 'onlydrinkcoffee': 32, 'wolfy!': 67,
         'hemeow': 81, 'an.apple': 90, 'marz': 27, 'pichu': 84, 'False Promise': 37,
         "it's ok": 1, 'qod': 83, 'crazykiller': 10, 'EMP': 98, 'coffeems': 38,
         'odhako': 88, 'reality': 86, 'shifear': 81, 'ByeTheCore': 3, 'tibosha': 92,
         'у моей охраны есть охрана': 18, 'therion': 8, 'Lfor': 40, 'Disaster': 24, 'Q.Yo(retrostyle)': 65,
         'stoneremnant': 80, 'Sherk': 57, 'bonchinche': 18, 'поцелуйвгузно': 59, 'подруга подруг': 47,
         'valvarn': 65, 'maslenok': 57, 'iequa': 91, 'denjke': 60, 'Q.Yo': 59,
         'username': 21, '?emptember': 32, 'psibladeheaven': 20, 'dodik': 10, 'player': 74,
         'hanaye': 84, 'madara': 89, '2ez4me': 66, 'karma': 55, 'bOy!': 20,
         'skvermas': 81, 'Oleja': 26, 'AemTheBest': 17, 'DreamKG': 82, 'Kutbic': 64,
         'areyoudeadyet?': 67, 'донная мощь': 63, 'grievous': 21, 'otlichnik': 76, 'tokyorudge': 40,
         'chevo': 7, 'fucktwelve': 49, 'тюбикмамкин': 25, '95_gungster_95': 74, 'lul kek': 22}

teams_names = ['-', 'LuckyTeam', 'Napalm', 'Bibisi', 'Team Sincere(China)', 'depressedteam',
               'UFO', 'Nasos', 'ОУ Дядь', 'Spark', 'M and Ms', 'Anime Squad', 'KompasGaming', '0k_Gaming',
               'ferzee', 'SeaTide', 'DX', 'ghoul', 'CrowCrowd', 'Digital Company', 'SeaOne',
               'Quantic.Lucky', '1%', 'Quantic.Young', 'KirieshkaTeam', 'Sixty', 'Velum',
               'Tidehunterdamage', 'OverKek']

teams_players: dict[Union[str, Any], Union[list[str], Any]] = {'LuckyTeam': LuckyTeam, 'Napalm': Napalm,
                                                               'Bibisi': Bibisi, 'Team Sincere(China)': TeamSincere,
                                                               'depressedteam': depressedteam, 'UFO': UFO,
                                                               'Nasos': Nasos, 'ОУ Дядь': oy_dyad, 'Spark': Spark,
                                                               'M and Ms': M_and_Ms, 'Anime Squad': AnimeSquad,
                                                               'KompasGaming': KompasGaming,
                                                               '0k_Gaming': zerokgaming,
                                                               'ferzee': ferzee, 'SeaTide': SeaTide, 'DX': DX,
                                                               'ghoul': ghoul, 'CrowCrowd': CrowCrowd,
                                                               'Digital_Company': Digital_Company, 'SeaOne': SeaOne,
                                                               'Quantic.Lucky': Quantic_Lucky,
                                                               '1%': onepercent, 'Quantic.Young': Quantic_Young,
                                                               'KirieshkaTeam': KirieshkaTeam,
                                                               'Sixty': Sixty, 'Velum': Velum,
                                                               'Tidehunterdamage': Tidehunterdamage, 'OverKek': OverKek}

