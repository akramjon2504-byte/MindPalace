import random
from typing import Dict, List, Optional

class WordsDatabase:
    """Database class for managing English-Uzbek word pairs"""
    
    def __init__(self):
        self.words = [
            {
                "english": "apple",
                "transcription": "[ˈæpəl]",
                "uzbek": "olma"
            },
            {
                "english": "book",
                "transcription": "[bʊk]",
                "uzbek": "kitob"
            },
            {
                "english": "house",
                "transcription": "[haʊs]",
                "uzbek": "uy"
            },
            {
                "english": "water",
                "transcription": "[ˈwɔːtər]",
                "uzbek": "suv"
            },
            {
                "english": "cat",
                "transcription": "[kæt]",
                "uzbek": "mushuk"
            },
            {
                "english": "dog",
                "transcription": "[dɔːɡ]",
                "uzbek": "it"
            },
            {
                "english": "car",
                "transcription": "[kɑːr]",
                "uzbek": "mashina"
            },
            {
                "english": "tree",
                "transcription": "[triː]",
                "uzbek": "daraxt"
            },
            {
                "english": "school",
                "transcription": "[skuːl]",
                "uzbek": "maktab"
            },
            {
                "english": "friend",
                "transcription": "[frend]",
                "uzbek": "do'st"
            },
            {
                "english": "family",
                "transcription": "[ˈfæməli]",
                "uzbek": "oila"
            },
            {
                "english": "food",
                "transcription": "[fuːd]",
                "uzbek": "ovqat"
            },
            {
                "english": "time",
                "transcription": "[taɪm]",
                "uzbek": "vaqt"
            },
            {
                "english": "money",
                "transcription": "[ˈmʌni]",
                "uzbek": "pul"
            },
            {
                "english": "work",
                "transcription": "[wɜːrk]",
                "uzbek": "ish"
            },
            {
                "english": "love",
                "transcription": "[lʌv]",
                "uzbek": "sevgi"
            },
            {
                "english": "happy",
                "transcription": "[ˈhæpi]",
                "uzbek": "baxtli"
            },
            {
                "english": "beautiful",
                "transcription": "[ˈbjuːtɪfəl]",
                "uzbek": "chiroyli"
            },
            {
                "english": "good",
                "transcription": "[ɡʊd]",
                "uzbek": "yaxshi"
            },
            {
                "english": "bad",
                "transcription": "[bæd]",
                "uzbek": "yomon"
            },
            {
                "english": "big",
                "transcription": "[bɪɡ]",
                "uzbek": "katta"
            },
            {
                "english": "small",
                "transcription": "[smɔːl]",
                "uzbek": "kichik"
            },
            {
                "english": "blue",
                "transcription": "[bluː]",
                "uzbek": "ko'k"
            },
            {
                "english": "red",
                "transcription": "[red]",
                "uzbek": "qizil"
            },
            {
                "english": "green",
                "transcription": "[ɡriːn]",
                "uzbek": "yashil"
            },
            {
                "english": "white",
                "transcription": "[waɪt]",
                "uzbek": "oq"
            },
            {
                "english": "black",
                "transcription": "[blæk]",
                "uzbek": "qora"
            },
            {
                "english": "table",
                "transcription": "[ˈteɪbəl]",
                "uzbek": "stol"
            },
            {
                "english": "chair",
                "transcription": "[tʃer]",
                "uzbek": "stul"
            },
            {
                "english": "window",
                "transcription": "[ˈwɪndoʊ]",
                "uzbek": "deraza"
            },
            # Body parts
            {
                "english": "head",
                "transcription": "[hed]",
                "uzbek": "bosh"
            },
            {
                "english": "eye",
                "transcription": "[aɪ]",
                "uzbek": "ko'z"
            },
            {
                "english": "ear",
                "transcription": "[ɪr]",
                "uzbek": "quloq"
            },
            {
                "english": "nose",
                "transcription": "[noʊz]",
                "uzbek": "burun"
            },
            {
                "english": "mouth",
                "transcription": "[maʊθ]",
                "uzbek": "og'iz"
            },
            {
                "english": "hand",
                "transcription": "[hænd]",
                "uzbek": "qo'l"
            },
            {
                "english": "foot",
                "transcription": "[fʊt]",
                "uzbek": "oyoq"
            },
            {
                "english": "leg",
                "transcription": "[leɡ]",
                "uzbek": "oyoq"
            },
            {
                "english": "arm",
                "transcription": "[ɑːrm]",
                "uzbek": "qo'l"
            },
            {
                "english": "finger",
                "transcription": "[ˈfɪŋɡər]",
                "uzbek": "barmoq"
            },
            # Numbers
            {
                "english": "one",
                "transcription": "[wʌn]",
                "uzbek": "bir"
            },
            {
                "english": "two",
                "transcription": "[tuː]",
                "uzbek": "ikki"
            },
            {
                "english": "three",
                "transcription": "[θriː]",
                "uzbek": "uch"
            },
            {
                "english": "four",
                "transcription": "[fɔːr]",
                "uzbek": "to'rt"
            },
            {
                "english": "five",
                "transcription": "[faɪv]",
                "uzbek": "besh"
            },
            {
                "english": "six",
                "transcription": "[sɪks]",
                "uzbek": "olti"
            },
            {
                "english": "seven",
                "transcription": "[ˈsevən]",
                "uzbek": "yetti"
            },
            {
                "english": "eight",
                "transcription": "[eɪt]",
                "uzbek": "sakkiz"
            },
            {
                "english": "nine",
                "transcription": "[naɪn]",
                "uzbek": "to'qqiz"
            },
            {
                "english": "ten",
                "transcription": "[ten]",
                "uzbek": "o'n"
            },
            # Days of the week
            {
                "english": "monday",
                "transcription": "[ˈmʌndeɪ]",
                "uzbek": "dushanba"
            },
            {
                "english": "tuesday",
                "transcription": "[ˈtuːzdeɪ]",
                "uzbek": "seshanba"
            },
            {
                "english": "wednesday",
                "transcription": "[ˈwenzdeɪ]",
                "uzbek": "chorshanba"
            },
            {
                "english": "thursday",
                "transcription": "[ˈθɜːrzdeɪ]",
                "uzbek": "payshanba"
            },
            {
                "english": "friday",
                "transcription": "[ˈfraɪdeɪ]",
                "uzbek": "juma"
            },
            {
                "english": "saturday",
                "transcription": "[ˈsætərdeɪ]",
                "uzbek": "shanba"
            },
            {
                "english": "sunday",
                "transcription": "[ˈsʌndeɪ]",
                "uzbek": "yakshanba"
            },
            # Months
            {
                "english": "january",
                "transcription": "[ˈdʒænjueri]",
                "uzbek": "yanvar"
            },
            {
                "english": "february",
                "transcription": "[ˈfebrueri]",
                "uzbek": "fevral"
            },
            {
                "english": "march",
                "transcription": "[mɑːrtʃ]",
                "uzbek": "mart"
            },
            {
                "english": "april",
                "transcription": "[ˈeɪprəl]",
                "uzbek": "aprel"
            },
            {
                "english": "may",
                "transcription": "[meɪ]",
                "uzbek": "may"
            },
            {
                "english": "june",
                "transcription": "[dʒuːn]",
                "uzbek": "iyun"
            },
            {
                "english": "july",
                "transcription": "[dʒuˈlaɪ]",
                "uzbek": "iyul"
            },
            {
                "english": "august",
                "transcription": "[ˈɔːɡəst]",
                "uzbek": "avgust"
            },
            {
                "english": "september",
                "transcription": "[sepˈtembər]",
                "uzbek": "sentyabr"
            },
            {
                "english": "october",
                "transcription": "[ɑːkˈtoʊbər]",
                "uzbek": "oktyabr"
            },
            {
                "english": "november",
                "transcription": "[noʊˈvembər]",
                "uzbek": "noyabr"
            },
            {
                "english": "december",
                "transcription": "[dɪˈsembər]",
                "uzbek": "dekabr"
            },
            # Food items
            {
                "english": "bread",
                "transcription": "[bred]",
                "uzbek": "non"
            },
            {
                "english": "meat",
                "transcription": "[miːt]",
                "uzbek": "go'sht"
            },
            {
                "english": "rice",
                "transcription": "[raɪs]",
                "uzbek": "guruch"
            },
            {
                "english": "milk",
                "transcription": "[mɪlk]",
                "uzbek": "sut"
            },
            {
                "english": "egg",
                "transcription": "[eɡ]",
                "uzbek": "tuxum"
            },
            {
                "english": "fish",
                "transcription": "[fɪʃ]",
                "uzbek": "baliq"
            },
            {
                "english": "chicken",
                "transcription": "[ˈtʃɪkən]",
                "uzbek": "tovuq"
            },
            {
                "english": "banana",
                "transcription": "[bəˈnænə]",
                "uzbek": "banan"
            },
            {
                "english": "orange",
                "transcription": "[ˈɔːrɪndʒ]",
                "uzbek": "apelsin"
            },
            {
                "english": "grape",
                "transcription": "[ɡreɪp]",
                "uzbek": "uzum"
            },
            {
                "english": "tomato",
                "transcription": "[təˈmeɪtoʊ]",
                "uzbek": "pomidor"
            },
            {
                "english": "potato",
                "transcription": "[pəˈteɪtoʊ]",
                "uzbek": "kartoshka"
            },
            {
                "english": "onion",
                "transcription": "[ˈʌnjən]",
                "uzbek": "piyoz"
            },
            {
                "english": "carrot",
                "transcription": "[ˈkærət]",
                "uzbek": "sabzi"
            },
            # Animals
            {
                "english": "cow",
                "transcription": "[kaʊ]",
                "uzbek": "sigir"
            },
            {
                "english": "horse",
                "transcription": "[hɔːrs]",
                "uzbek": "ot"
            },
            {
                "english": "sheep",
                "transcription": "[ʃiːp]",
                "uzbek": "qo'y"
            },
            {
                "english": "goat",
                "transcription": "[ɡoʊt]",
                "uzbek": "echki"
            },
            {
                "english": "pig",
                "transcription": "[pɪɡ]",
                "uzbek": "cho'chqa"
            },
            {
                "english": "bird",
                "transcription": "[bɜːrd]",
                "uzbek": "qush"
            },
            {
                "english": "lion",
                "transcription": "[ˈlaɪən]",
                "uzbek": "sher"
            },
            {
                "english": "tiger",
                "transcription": "[ˈtaɪɡər]",
                "uzbek": "yo'lbars"
            },
            {
                "english": "elephant",
                "transcription": "[ˈeləfənt]",
                "uzbek": "fil"
            },
            {
                "english": "bear",
                "transcription": "[ber]",
                "uzbek": "ayiq"
            },
            # Clothing
            {
                "english": "shirt",
                "transcription": "[ʃɜːrt]",
                "uzbek": "ko'ylak"
            },
            {
                "english": "pants",
                "transcription": "[pænts]",
                "uzbek": "shim"
            },
            {
                "english": "dress",
                "transcription": "[dres]",
                "uzbek": "ko'ylak"
            },
            {
                "english": "shoes",
                "transcription": "[ʃuːz]",
                "uzbek": "poyabzal"
            },
            {
                "english": "hat",
                "transcription": "[hæt]",
                "uzbek": "shlyapa"
            },
            {
                "english": "coat",
                "transcription": "[koʊt]",
                "uzbek": "palto"
            },
            {
                "english": "jacket",
                "transcription": "[ˈdʒækət]",
                "uzbek": "kurtka"
            },
            {
                "english": "sock",
                "transcription": "[sɑːk]",
                "uzbek": "paypoq"
            },
            # Household items
            {
                "english": "bed",
                "transcription": "[bed]",
                "uzbek": "karavot"
            },
            {
                "english": "pillow",
                "transcription": "[ˈpɪloʊ]",
                "uzbek": "yostiq"
            },
            {
                "english": "blanket",
                "transcription": "[ˈblæŋkət]",
                "uzbek": "adyol"
            },
            {
                "english": "door",
                "transcription": "[dɔːr]",
                "uzbek": "eshik"
            },
            {
                "english": "key",
                "transcription": "[kiː]",
                "uzbek": "kalit"
            },
            {
                "english": "lamp",
                "transcription": "[læmp]",
                "uzbek": "chiroq"
            },
            {
                "english": "mirror",
                "transcription": "[ˈmɪrər]",
                "uzbek": "oyna"
            },
            {
                "english": "clock",
                "transcription": "[klɑːk]",
                "uzbek": "soat"
            },
            # Transportation
            {
                "english": "bus",
                "transcription": "[bʌs]",
                "uzbek": "avtobus"
            },
            {
                "english": "train",
                "transcription": "[treɪn]",
                "uzbek": "poyezd"
            },
            {
                "english": "plane",
                "transcription": "[pleɪn]",
                "uzbek": "samolyot"
            },
            {
                "english": "bike",
                "transcription": "[baɪk]",
                "uzbek": "velosiped"
            },
            {
                "english": "boat",
                "transcription": "[boʊt]",
                "uzbek": "qayiq"
            },
            # Weather
            {
                "english": "sun",
                "transcription": "[sʌn]",
                "uzbek": "quyosh"
            },
            {
                "english": "moon",
                "transcription": "[muːn]",
                "uzbek": "oy"
            },
            {
                "english": "star",
                "transcription": "[stɑːr]",
                "uzbek": "yulduz"
            },
            {
                "english": "rain",
                "transcription": "[reɪn]",
                "uzbek": "yomg'ir"
            },
            {
                "english": "snow",
                "transcription": "[snoʊ]",
                "uzbek": "qor"
            },
            {
                "english": "wind",
                "transcription": "[wɪnd]",
                "uzbek": "shamol"
            },
            {
                "english": "cloud",
                "transcription": "[klaʊd]",
                "uzbek": "bulut"
            },
            # Actions/Verbs
            {
                "english": "go",
                "transcription": "[ɡoʊ]",
                "uzbek": "bormoq"
            },
            {
                "english": "come",
                "transcription": "[kʌm]",
                "uzbek": "kelmoq"
            },
            {
                "english": "eat",
                "transcription": "[iːt]",
                "uzbek": "yemoq"
            },
            {
                "english": "drink",
                "transcription": "[drɪŋk]",
                "uzbek": "ichmoq"
            },
            {
                "english": "sleep",
                "transcription": "[sliːp]",
                "uzbek": "uxlamoq"
            },
            {
                "english": "walk",
                "transcription": "[wɔːk]",
                "uzbek": "yurmoq"
            },
            {
                "english": "run",
                "transcription": "[rʌn]",
                "uzbek": "yugurmoq"
            },
            {
                "english": "read",
                "transcription": "[riːd]",
                "uzbek": "o'qimoq"
            },
            {
                "english": "write",
                "transcription": "[raɪt]",
                "uzbek": "yozmoq"
            },
            {
                "english": "speak",
                "transcription": "[spiːk]",
                "uzbek": "gapirmoq"
            },
            {
                "english": "listen",
                "transcription": "[ˈlɪsən]",
                "uzbek": "tinglamoq"
            },
            {
                "english": "look",
                "transcription": "[lʊk]",
                "uzbek": "qaramoq"
            },
            {
                "english": "see",
                "transcription": "[siː]",
                "uzbek": "ko'rmoq"
            },
            {
                "english": "buy",
                "transcription": "[baɪ]",
                "uzbek": "sotib olmoq"
            },
            {
                "english": "sell",
                "transcription": "[sel]",
                "uzbek": "sotmoq"
            },
            {
                "english": "give",
                "transcription": "[ɡɪv]",
                "uzbek": "bermoq"
            },
            {
                "english": "take",
                "transcription": "[teɪk]",
                "uzbek": "olmoq"
            },
            {
                "english": "open",
                "transcription": "[ˈoʊpən]",
                "uzbek": "ochmoq"
            },
            {
                "english": "close",
                "transcription": "[kloʊz]",
                "uzbek": "yopmoq"
            },
            # Adjectives
            {
                "english": "hot",
                "transcription": "[hɑːt]",
                "uzbek": "issiq"
            },
            {
                "english": "cold",
                "transcription": "[koʊld]",
                "uzbek": "sovuq"
            },
            {
                "english": "warm",
                "transcription": "[wɔːrm]",
                "uzbek": "iliq"
            },
            {
                "english": "cool",
                "transcription": "[kuːl]",
                "uzbek": "salqin"
            },
            {
                "english": "fast",
                "transcription": "[fæst]",
                "uzbek": "tez"
            },
            {
                "english": "slow",
                "transcription": "[sloʊ]",
                "uzbek": "sekin"
            },
            {
                "english": "new",
                "transcription": "[nuː]",
                "uzbek": "yangi"
            },
            {
                "english": "old",
                "transcription": "[oʊld]",
                "uzbek": "eski"
            },
            {
                "english": "young",
                "transcription": "[jʌŋ]",
                "uzbek": "yosh"
            },
            {
                "english": "tall",
                "transcription": "[tɔːl]",
                "uzbek": "baland"
            },
            {
                "english": "short",
                "transcription": "[ʃɔːrt]",
                "uzbek": "qisqa"
            },
            {
                "english": "long",
                "transcription": "[lɔːŋ]",
                "uzbek": "uzun"
            },
            {
                "english": "wide",
                "transcription": "[waɪd]",
                "uzbek": "keng"
            },
            {
                "english": "narrow",
                "transcription": "[ˈnæroʊ]",
                "uzbek": "tor"
            },
            {
                "english": "heavy",
                "transcription": "[ˈhevi]",
                "uzbek": "og'ir"
            },
            {
                "english": "light",
                "transcription": "[laɪt]",
                "uzbek": "engil"
            },
            {
                "english": "strong",
                "transcription": "[strɔːŋ]",
                "uzbek": "kuchli"
            },
            {
                "english": "weak",
                "transcription": "[wiːk]",
                "uzbek": "zaif"
            },
            {
                "english": "clean",
                "transcription": "[kliːn]",
                "uzbek": "toza"
            },
            {
                "english": "dirty",
                "transcription": "[ˈdɜːrti]",
                "uzbek": "iflos"
            },
            # Nature
            {
                "english": "mountain",
                "transcription": "[ˈmaʊntən]",
                "uzbek": "tog'"
            },
            {
                "english": "river",
                "transcription": "[ˈrɪvər]",
                "uzbek": "daryo"
            },
            {
                "english": "sea",
                "transcription": "[siː]",
                "uzbek": "dengiz"
            },
            {
                "english": "lake",
                "transcription": "[leɪk]",
                "uzbek": "ko'l"
            },
            {
                "english": "forest",
                "transcription": "[ˈfɔːrəst]",
                "uzbek": "o'rmon"
            },
            {
                "english": "flower",
                "transcription": "[ˈflaʊər]",
                "uzbek": "gul"
            },
            {
                "english": "grass",
                "transcription": "[ɡræs]",
                "uzbek": "o't"
            },
            {
                "english": "stone",
                "transcription": "[stoʊn]",
                "uzbek": "tosh"
            },
            {
                "english": "sand",
                "transcription": "[sænd]",
                "uzbek": "qum"
            },
            {
                "english": "fire",
                "transcription": "[ˈfaɪər]",
                "uzbek": "olov"
            },
            # Places
            {
                "english": "city",
                "transcription": "[ˈsɪti]",
                "uzbek": "shahar"
            },
            {
                "english": "village",
                "transcription": "[ˈvɪlɪdʒ]",
                "uzbek": "qishloq"
            },
            {
                "english": "street",
                "transcription": "[striːt]",
                "uzbek": "ko'cha"
            },
            {
                "english": "park",
                "transcription": "[pɑːrk]",
                "uzbek": "bog'"
            },
            {
                "english": "hospital",
                "transcription": "[ˈhɑːspɪtl]",
                "uzbek": "kasalxona"
            },
            {
                "english": "store",
                "transcription": "[stɔːr]",
                "uzbek": "do'kon"
            },
            {
                "english": "market",
                "transcription": "[ˈmɑːrkət]",
                "uzbek": "bozor"
            },
            {
                "english": "restaurant",
                "transcription": "[ˈrestrɑːnt]",
                "uzbek": "restoran"
            },
            {
                "english": "hotel",
                "transcription": "[hoʊˈtel]",
                "uzbek": "mehmonxona"
            },
            {
                "english": "bank",
                "transcription": "[bæŋk]",
                "uzbek": "bank"
            },
            # Professions
            {
                "english": "teacher",
                "transcription": "[ˈtiːtʃər]",
                "uzbek": "o'qituvchi"
            },
            {
                "english": "doctor",
                "transcription": "[ˈdɑːktər]",
                "uzbek": "shifokor"
            },
            {
                "english": "student",
                "transcription": "[ˈstuːdənt]",
                "uzbek": "talaba"
            },
            {
                "english": "worker",
                "transcription": "[ˈwɜːrkər]",
                "uzbek": "ishchi"
            },
            {
                "english": "driver",
                "transcription": "[ˈdraɪvər]",
                "uzbek": "haydovchi"
            },
            {
                "english": "farmer",
                "transcription": "[ˈfɑːrmər]",
                "uzbek": "fermer"
            },
            {
                "english": "cook",
                "transcription": "[kʊk]",
                "uzbek": "oshpaz"
            },
            {
                "english": "nurse",
                "transcription": "[nɜːrs]",
                "uzbek": "hamshira"
            },
            {
                "english": "police",
                "transcription": "[pəˈliːs]",
                "uzbek": "politsiya"
            },
            {
                "english": "artist",
                "transcription": "[ˈɑːrtəst]",
                "uzbek": "rassom"
            },
            # Technology
            {
                "english": "computer",
                "transcription": "[kəmˈpjuːtər]",
                "uzbek": "kompyuter"
            },
            {
                "english": "phone",
                "transcription": "[foʊn]",
                "uzbek": "telefon"
            },
            {
                "english": "television",
                "transcription": "[ˈteləvɪʒən]",
                "uzbek": "televizor"
            },
            {
                "english": "radio",
                "transcription": "[ˈreɪdioʊ]",
                "uzbek": "radio"
            },
            {
                "english": "camera",
                "transcription": "[ˈkæmərə]",
                "uzbek": "kamera"
            },
            {
                "english": "internet",
                "transcription": "[ˈɪntərnet]",
                "uzbek": "internet"
            },
            # Sports
            {
                "english": "football",
                "transcription": "[ˈfʊtbɔːl]",
                "uzbek": "futbol"
            },
            {
                "english": "tennis",
                "transcription": "[ˈtenəs]",
                "uzbek": "tennis"
            },
            {
                "english": "basketball",
                "transcription": "[ˈbæskətbɔːl]",
                "uzbek": "basketbol"
            },
            {
                "english": "swimming",
                "transcription": "[ˈswɪmɪŋ]",
                "uzbek": "suzish"
            },
            {
                "english": "running",
                "transcription": "[ˈrʌnɪŋ]",
                "uzbek": "yugurish"
            },
            # Music
            {
                "english": "music",
                "transcription": "[ˈmjuːzək]",
                "uzbek": "musiqa"
            },
            {
                "english": "song",
                "transcription": "[sɔːŋ]",
                "uzbek": "qo'shiq"
            },
            {
                "english": "guitar",
                "transcription": "[ɡəˈtɑːr]",
                "uzbek": "gitara"
            },
            {
                "english": "piano",
                "transcription": "[piˈænoʊ]",
                "uzbek": "pianino"
            },
            {
                "english": "dance",
                "transcription": "[dæns]",
                "uzbek": "raqs"
            },
            # Emotions
            {
                "english": "sad",
                "transcription": "[sæd]",
                "uzbek": "g'amgin"
            },
            {
                "english": "angry",
                "transcription": "[ˈæŋɡri]",
                "uzbek": "g'azabli"
            },
            {
                "english": "excited",
                "transcription": "[ɪkˈsaɪtəd]",
                "uzbek": "hayajonli"
            },
            {
                "english": "tired",
                "transcription": "[ˈtaɪərd]",
                "uzbek": "charchagan"
            },
            {
                "english": "hungry",
                "transcription": "[ˈhʌŋɡri]",
                "uzbek": "och"
            },
            {
                "english": "thirsty",
                "transcription": "[ˈθɜːrsti]",
                "uzbek": "chanqagan"
            },
            {
                "english": "scared",
                "transcription": "[skerd]",
                "uzbek": "qo'rqgan"
            },
            {
                "english": "surprised",
                "transcription": "[sərˈpraɪzd]",
                "uzbek": "hayron"
            },
            # Health
            {
                "english": "medicine",
                "transcription": "[ˈmedəsən]",
                "uzbek": "dori"
            },
            {
                "english": "healthy",
                "transcription": "[ˈhelθi]",
                "uzbek": "sog'lom"
            },
            {
                "english": "sick",
                "transcription": "[sɪk]",
                "uzbek": "kasal"
            },
            {
                "english": "pain",
                "transcription": "[peɪn]",
                "uzbek": "og'riq"
            },
            {
                "english": "exercise",
                "transcription": "[ˈeksərsaɪz]",
                "uzbek": "mashq"
            },
            # More numbers
            {
                "english": "eleven",
                "transcription": "[ɪˈlevən]",
                "uzbek": "o'n bir"
            },
            {
                "english": "twelve",
                "transcription": "[twelv]",
                "uzbek": "o'n ikki"
            },
            {
                "english": "twenty",
                "transcription": "[ˈtwenti]",
                "uzbek": "yigirma"
            },
            {
                "english": "thirty",
                "transcription": "[ˈθɜːrti]",
                "uzbek": "o'ttiz"
            },
            {
                "english": "forty",
                "transcription": "[ˈfɔːrti]",
                "uzbek": "qirq"
            },
            {
                "english": "fifty",
                "transcription": "[ˈfɪfti]",
                "uzbek": "ellik"
            },
            {
                "english": "hundred",
                "transcription": "[ˈhʌndrəd]",
                "uzbek": "yuz"
            },
            {
                "english": "thousand",
                "transcription": "[ˈθaʊzənd]",
                "uzbek": "ming"
            },
            # Education
            {
                "english": "lesson",
                "transcription": "[ˈlesən]",
                "uzbek": "dars"
            },
            {
                "english": "homework",
                "transcription": "[ˈhoʊmwɜːrk]",
                "uzbek": "uy vazifasi"
            },
            {
                "english": "test",
                "transcription": "[test]",
                "uzbek": "test"
            },
            {
                "english": "exam",
                "transcription": "[ɪɡˈzæm]",
                "uzbek": "imtihon"
            },
            {
                "english": "learn",
                "transcription": "[lɜːrn]",
                "uzbek": "o'rganmoq"
            },
            {
                "english": "study",
                "transcription": "[ˈstʌdi]",
                "uzbek": "o'qimoq"
            },
            {
                "english": "question",
                "transcription": "[ˈkwestʃən]",
                "uzbek": "savol"
            },
            {
                "english": "answer",
                "transcription": "[ˈænsər]",
                "uzbek": "javob"
            },
            {
                "english": "knowledge",
                "transcription": "[ˈnɑːlədʒ]",
                "uzbek": "bilim"
            },
            {
                "english": "language",
                "transcription": "[ˈlæŋɡwədʒ]",
                "uzbek": "til"
            },
            # Office/Work
            {
                "english": "office",
                "transcription": "[ˈɔːfəs]",
                "uzbek": "ofis"
            },
            {
                "english": "meeting",
                "transcription": "[ˈmiːtɪŋ]",
                "uzbek": "yig'ilish"
            },
            {
                "english": "paper",
                "transcription": "[ˈpeɪpər]",
                "uzbek": "qog'oz"
            },
            {
                "english": "pen",
                "transcription": "[pen]",
                "uzbek": "ruchka"
            },
            {
                "english": "pencil",
                "transcription": "[ˈpensəl]",
                "uzbek": "qalam"
            },
            {
                "english": "email",
                "transcription": "[ˈiːmeɪl]",
                "uzbek": "elektron pochta"
            },
            {
                "english": "letter",
                "transcription": "[ˈletər]",
                "uzbek": "xat"
            },
            {
                "english": "project",
                "transcription": "[ˈprɑːdʒekt]",
                "uzbek": "loyiha"
            },
            # Common phrases/words
            {
                "english": "hello",
                "transcription": "[həˈloʊ]",
                "uzbek": "salom"
            },
            {
                "english": "goodbye",
                "transcription": "[ɡʊdˈbaɪ]",
                "uzbek": "xayr"
            },
            {
                "english": "please",
                "transcription": "[pliːz]",
                "uzbek": "iltimos"
            },
            {
                "english": "thanks",
                "transcription": "[θæŋks]",
                "uzbek": "rahmat"
            },
            {
                "english": "sorry",
                "transcription": "[ˈsɑːri]",
                "uzbek": "kechirasiz"
            },
            {
                "english": "yes",
                "transcription": "[jes]",
                "uzbek": "ha"
            },
            {
                "english": "no",
                "transcription": "[noʊ]",
                "uzbek": "yo'q"
            },
            {
                "english": "maybe",
                "transcription": "[ˈmeɪbi]",
                "uzbek": "balki"
            },
            {
                "english": "help",
                "transcription": "[help]",
                "uzbek": "yordam"
            },
            {
                "english": "problem",
                "transcription": "[ˈprɑːbləm]",
                "uzbek": "muammo"
            },
            {
                "english": "idea",
                "transcription": "[aɪˈdiːə]",
                "uzbek": "g'oya"
            },
            {
                "english": "story",
                "transcription": "[ˈstɔːri]",
                "uzbek": "hikoya"
            },
            {
                "english": "news",
                "transcription": "[nuːz]",
                "uzbek": "yangilik"
            },
            {
                "english": "information",
                "transcription": "[ˌɪnfərˈmeɪʃən]",
                "uzbek": "ma'lumot"
            },
            # More foods
            {
                "english": "sugar",
                "transcription": "[ˈʃʊɡər]",
                "uzbek": "shakar"
            },
            {
                "english": "salt",
                "transcription": "[sɔːlt]",
                "uzbek": "tuz"
            },
            {
                "english": "tea",
                "transcription": "[tiː]",
                "uzbek": "choy"
            },
            {
                "english": "coffee",
                "transcription": "[ˈkɔːfi]",
                "uzbek": "qahva"
            },
            {
                "english": "juice",
                "transcription": "[dʒuːs]",
                "uzbek": "sharbat"
            },
            {
                "english": "cheese",
                "transcription": "[tʃiːz]",
                "uzbek": "pishloq"
            },
            {
                "english": "butter",
                "transcription": "[ˈbʌtər]",
                "uzbek": "sariyog'"
            },
            {
                "english": "soup",
                "transcription": "[suːp]",
                "uzbek": "sho'rva"
            },
            {
                "english": "salad",
                "transcription": "[ˈsæləd]",
                "uzbek": "salat"
            },
            {
                "english": "cake",
                "transcription": "[keɪk]",
                "uzbek": "tort"
            },
            # Time words
            {
                "english": "today",
                "transcription": "[təˈdeɪ]",
                "uzbek": "bugun"
            },
            {
                "english": "tomorrow",
                "transcription": "[təˈmɔːroʊ]",
                "uzbek": "erta"
            },
            {
                "english": "yesterday",
                "transcription": "[ˈjestərdeɪ]",
                "uzbek": "kecha"
            },
            {
                "english": "morning",
                "transcription": "[ˈmɔːrnɪŋ]",
                "uzbek": "ertalab"
            },
            {
                "english": "afternoon",
                "transcription": "[ˌæftərˈnuːn]",
                "uzbek": "tushdan keyin"
            },
            {
                "english": "evening",
                "transcription": "[ˈiːvnɪŋ]",
                "uzbek": "kechqurun"
            },
            {
                "english": "night",
                "transcription": "[naɪt]",
                "uzbek": "kecha"
            },
            {
                "english": "hour",
                "transcription": "[aʊər]",
                "uzbek": "soat"
            },
            {
                "english": "minute",
                "transcription": "[ˈmɪnət]",
                "uzbek": "daqiqa"
            },
            {
                "english": "second",
                "transcription": "[ˈsekənd]",
                "uzbek": "soniya"
            },
            {
                "english": "week",
                "transcription": "[wiːk]",
                "uzbek": "hafta"
            },
            {
                "english": "month",
                "transcription": "[mʌnθ]",
                "uzbek": "oy"
            },
            {
                "english": "year",
                "transcription": "[jɪr]",
                "uzbek": "yil"
            },
            # Direction words
            {
                "english": "left",
                "transcription": "[left]",
                "uzbek": "chap"
            },
            {
                "english": "right",
                "transcription": "[raɪt]",
                "uzbek": "o'ng"
            },
            {
                "english": "up",
                "transcription": "[ʌp]",
                "uzbek": "yuqori"
            },
            {
                "english": "down",
                "transcription": "[daʊn]",
                "uzbek": "pastga"
            },
            {
                "english": "front",
                "transcription": "[frʌnt]",
                "uzbek": "oldin"
            },
            {
                "english": "back",
                "transcription": "[bæk]",
                "uzbek": "orqa"
            },
            {
                "english": "inside",
                "transcription": "[ɪnˈsaɪd]",
                "uzbek": "ichida"
            },
            {
                "english": "outside",
                "transcription": "[aʊtˈsaɪd]",
                "uzbek": "tashqarida"
            },
            {
                "english": "near",
                "transcription": "[nɪr]",
                "uzbek": "yaqin"
            },
            {
                "english": "far",
                "transcription": "[fɑːr]",
                "uzbek": "uzoq"
            },
            # More verbs
            {
                "english": "think",
                "transcription": "[θɪŋk]",
                "uzbek": "o'ylamoq"
            },
            {
                "english": "know",
                "transcription": "[noʊ]",
                "uzbek": "bilmoq"
            },
            {
                "english": "understand",
                "transcription": "[ˌʌndərˈstænd]",
                "uzbek": "tushunmoq"
            },
            {
                "english": "remember",
                "transcription": "[rɪˈmembər]",
                "uzbek": "eslamoq"
            },
            {
                "english": "forget",
                "transcription": "[fərˈɡet]",
                "uzbek": "unutmoq"
            },
            {
                "english": "find",
                "transcription": "[faɪnd]",
                "uzbek": "topmoq"
            },
            {
                "english": "lose",
                "transcription": "[luːz]",
                "uzbek": "yo'qotmoq"
            },
            {
                "english": "win",
                "transcription": "[wɪn]",
                "uzbek": "yutmoq"
            },
            {
                "english": "play",
                "transcription": "[pleɪ]",
                "uzbek": "o'ynamoq"
            },
            {
                "english": "work",
                "transcription": "[wɜːrk]",
                "uzbek": "ishlamoq"
            },
            {
                "english": "rest",
                "transcription": "[rest]",
                "uzbek": "dam olmoq"
            },
            {
                "english": "travel",
                "transcription": "[ˈtrævəl]",
                "uzbek": "sayohat qilmoq"
            },
            {
                "english": "visit",
                "transcription": "[ˈvɪzət]",
                "uzbek": "tashrif buyurmoq"
            },
            {
                "english": "call",
                "transcription": "[kɔːl]",
                "uzbek": "qo'ng'iroq qilmoq"
            },
            {
                "english": "answer",
                "transcription": "[ˈænsər]",
                "uzbek": "javob bermoq"
            },
            {
                "english": "ask",
                "transcription": "[æsk]",
                "uzbek": "so'ramoq"
            },
            {
                "english": "tell",
                "transcription": "[tel]",
                "uzbek": "aytmoq"
            },
            {
                "english": "show",
                "transcription": "[ʃoʊ]",
                "uzbek": "ko'rsatmoq"
            },
            {
                "english": "teach",
                "transcription": "[tiːtʃ]",
                "uzbek": "o'rgatmoq"
            },
            {
                "english": "learn",
                "transcription": "[lɜːrn]",
                "uzbek": "o'rganmoq"
            },
            {
                "english": "try",
                "transcription": "[traɪ]",
                "uzbek": "harakat qilmoq"
            },
            {
                "english": "help",
                "transcription": "[help]",
                "uzbek": "yordam bermoq"
            },
            {
                "english": "stop",
                "transcription": "[stɑːp]",
                "uzbek": "to'xtatmoq"
            },
            {
                "english": "start",
                "transcription": "[stɑːrt]",
                "uzbek": "boshlamoq"
            },
            {
                "english": "finish",
                "transcription": "[ˈfɪnɪʃ]",
                "uzbek": "tugatmoq"
            },
            {
                "english": "continue",
                "transcription": "[kənˈtɪnjuː]",
                "uzbek": "davom etmoq"
            },
            {
                "english": "change",
                "transcription": "[tʃeɪndʒ]",
                "uzbek": "o'zgartirmoq"
            },
            {
                "english": "choose",
                "transcription": "[tʃuːz]",
                "uzbek": "tanlamoq"
            },
            {
                "english": "decide",
                "transcription": "[dɪˈsaɪd]",
                "uzbek": "qaror qilmoq"
            },
            {
                "english": "agree",
                "transcription": "[əˈɡriː]",
                "uzbek": "rozi bo'lmoq"
            },
            {
                "english": "disagree",
                "transcription": "[ˌdɪsəˈɡriː]",
                "uzbek": "rozi bo'lmaslik"
            },
            # Final additions
            {
                "english": "hope",
                "transcription": "[hoʊp]",
                "uzbek": "umid"
            },
            {
                "english": "dream",
                "transcription": "[driːm]",
                "uzbek": "tush"
            },
            {
                "english": "smile",
                "transcription": "[smaɪl]",
                "uzbek": "tabassum"
            },
            {
                "english": "laugh",
                "transcription": "[læf]",
                "uzbek": "kulmoq"
            },
            {
                "english": "cry",
                "transcription": "[kraɪ]",
                "uzbek": "yig'lamoq"
            },
            {
                "english": "birthday",
                "transcription": "[ˈbɜːrθdeɪ]",
                "uzbek": "tug'ilgan kun"
            },
            {
                "english": "gift",
                "transcription": "[ɡɪft]",
                "uzbek": "sovg'a"
            },
            {
                "english": "party",
                "transcription": "[ˈpɑːrti]",
                "uzbek": "ziyofat"
            },
            {
                "english": "holiday",
                "transcription": "[ˈhɑːlədeɪ]",
                "uzbek": "bayram"
            },
            {
                "english": "wedding",
                "transcription": "[ˈwedɪŋ]",
                "uzbek": "to'y"
            }
        ]
    
    def get_random_word(self) -> Dict[str, str]:
        """Get a random word from the database"""
        return random.choice(self.words)
    
    def get_quiz_question(self) -> Dict:
        """Generate a quiz question with one correct and three incorrect answers"""
        correct_word = random.choice(self.words)
        
        # Get three random incorrect answers
        incorrect_words = [word for word in self.words if word != correct_word]
        incorrect_answers = random.sample(incorrect_words, 3)
        
        # Create options list and shuffle
        options = [correct_word["uzbek"]] + [word["uzbek"] for word in incorrect_answers]
        random.shuffle(options)
        
        return {
            "english": correct_word["english"],
            "transcription": correct_word["transcription"],
            "correct_answer": correct_word["uzbek"],
            "options": options
        }
    
    def get_all_words(self) -> List[Dict[str, str]]:
        """Get all words from the database"""
        return self.words.copy()

# Global instance
words_db = WordsDatabase()
