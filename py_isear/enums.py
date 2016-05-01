"""
Isear : Constants
This file will incorporate all needed constants in the first time
"""

"""
Here are the ISEAR codes explained

ID : identifier of the subject
CITY : city in which lives the subject

COUN : country of the subject
1 "SWEDEN" 
2 "NORWAY" 
3 "F.R.G." 
4 "FINLAND" 
5 "GREECE" 
6 "HONG KONG" 
7 "LEBANON" 
8 "AUSTRIA" 
9 "AUSTRALIA" 
10 "BRAZIL" 
11 "BOTSWANA" 
12 "BULGARIA" 
13 "FRANCE" 
14 "ITALY" 
15 "JAPAN" 
16 "NEW ZEALAND" 
17 "NETHERLANDS" 
18 "PORTUGAL" 
19 "SPAIN" 
20 "ZAMBIA" 
21 "ZIMBABWE" 
22 "USA" 
23 "POLAND" 
24 "NIGERIA" 
25 "ISRAEL" 
26 "INDIA" 
27 "MALAWI" 
28 "SWITZERLAND" 
29 "CHILE" 
30 "CHINA MAINLAND" 
31 "YUGOSLAVIA" 
32 "COSTA RICA" 
33 "HONDURAS" 
34 "MEXICO" 
35 GUATEMALA" 
36 "VENEZUELA" 
37 "EL SALVADOR"

SUBJ :

SEX : the sex of the subject
1 MALE
2 FEMALE

AGE : the age of the subject

RELI : the religion of the subject
1 "PROTESTANT" 
2 "CATHOLIC" 
3 "JEWISH" 
4 "HINDU" 
5 "BUDDHIST" 
6 "NATIVE" 
7 "OTHERS" 
8 "ARELIGIOUS"

PRAC : is subject practising religion
1 TRUE
2 FALSE

FOCC & MOCC : Father and Mother occupation
1 "HOUSEWIFE" 2 "UNEMPLOYED" 3 "STUDENT" 4 "BLUE COLLAR UNTRAINED" 5 "BLUE COLLAR TRAINED" 6 "WHITE COLLAR NONACADEMIC" 7 "WHITE COLLAR ACADEMIC" 8 "SELF-EMPLOYED NONACADEMIC" 9 "SELF-EMPLOYED ACADEMIC"

FIEL : subject's field of study
1 "PSYCHOLOGY" 2 "SOCIAL SCIENCES" 3 "LANGUAGES" 4 "FINE ARTS" 5 "LAW" 6 "NATURAL SCIENCE" 7 "ENGINEERING" 8 "MEDICAL" 9 "OTHER"

EMOT : subject's main emotion
1 JOY
2 FEAR
3 ANGER 
4 SADNESS
5 DISGUST
6 SHAME
7 GUILT

SIT : free text description (core of training)

-------------------- 
Event Quantification
--------------------
WHEN : when did that happen
1 DAYS AGO 2 WEEKS AGO 3 MONTHS AGO 4 YEARS AGO

LONG : how long did it last
1 MINUTES 2 HOUR 3 HOURS 4 DAY OR MORE

INTS : intensity score from 1 to 4

--------------------
Reaction
--------------------
ERGO : Ergotropic arousal (breathing, heart beat, etc) from 0 to 4

TROPHO : Trophophic arousal (lump, stomach, crying...) from 0 to 3

TEMPER : Felt temperature (-1 to 2)

--------------------
Expressive behaviour
--------------------
MOVE : from -1 (withdrawing) to +1 (forward)

EXPRES : nonverbal activity, from 0 to 6

PARAL : speech melody and tempo change from 0 to 3

EXP1 : if laughing/smilig 1, else 0
EXP2 : if sobbing/Crying
EXP10 : if moving against

CON : subject efforts to control
1 NONE 2 A LITTLE 3 VERY MUCH 0 NA

EXPC : situation expected to occur
0 NA 1 NOT 2 A LITTLE 3 VERY MUCH

PLEA : situation is pleasant

FAIR : fairness of the situation

MORL : morality of the situation

SELF : consequence on self estime

RELA : consequence on relationship with persons involved
1 NEGATIVE 2 NONE 3 POSITIVE 0 NA

PLAN : situation hindered current plans
0 HELPED 2 NO MATTER 3 HINDERED 0 NA

CAUS : who caused the situation
O NA 1 SELF 2 CLOSE 3 OTHER 4 IMPERSONNAL

COPING : ability to cope
1 NO ACTION NECESSARY
2 MANAGEABLE
3 ESCAPABLE SITUATION
4 DENIAL
5 DOMINATED
 
"""

# ID : identifier of the subject
# CITY : city in which lives the subject

# COUN : country of the subject
COUN = ["SWEDEN", "NORWAY", "F.R.G.", "FINLAND",
        "GREECE", "HONG KONG", "LEBANON", "AUSTRIA",
        "AUSTRALIA", "BRAZIL", "BOTSWANA", "BULGARIA",
        "FRANCE", "ITALY", "JAPAN", "NEW ZEALAND",
        "NETHERLANDS", "PORTUGAL", "SPAIN",
        "ZAMBIA", "ZIMBABWE", "USA", "POLAND", "NIGERIA",
        "ISRAEL", "INDIA", "MALAWI", "SWITZERLAND", "CHILE",
        "CHINA MAINLAND", "YUGOSLAVIA", "COSTA RICA", "HONDURAS",
        "MEXICO", "GUATEMALA", "VENEZUELA", "EL SALVADOR"]

# SUBJ : Identifier of the subject

# SEX : the sex of the subject
SEX = ["MALE", "FEMALE"]

# AGE : the age of the subject

# RELI : the religion of the subject
RELI = ["PROTESTANT", "CATHOLIC", "JEWISH", "HINDU",
        "BUDDHIST", "NATIVE", "OTHERS", "ARELIGIOUS"]

# PRAC : is subject practising religion
PRAC = ["TRUE", "FALSE"]

# FOCC & MOCC : Father and Mother occupation
POCC = ["HOUSEWIFE", "UNEMPLOYED", "STUDENT",
        "BLUE COLLAR UNTRAINED", "BLUE COLLAR TRAINED",
        "WHITE COLLAR NONACADEMIC", "WHITE COLLAR ACADEMIC",
        "SELF-EMPLOYED NONACADEMIC", "SELF-EMPLOYED ACADEMIC"]

# FIEL : subject's field of study
FIEL = ["PSYCHOLOGY", "SOCIAL SCIENCES", "LANGUAGES", "FINE ARTS",
        "LAW", "NATURAL SCIENCE", "ENGINEERING", "MEDICAL", "OTHER"]

# EMOT : subject's main emotion
EMOT = ["JOY", "FEAR", "ANGER", "SADNESS", "DISGUST", "SHAME", "GUILT"]

# SIT : free text description (core of training)

# --------------------
# Event Quantification
# --------------------
# WHEN : when did that happen
WHEN = ["DAYS AGO", "WEEKS AGO", "MONTHS AGO", "YEARS AGO"]

# LONG : how long did it last
LONG = ["MINUTES", "HOUR", "HOURS", "DAY OR MORE"]

# INTS : intensity score from 1 to 4

# --------------------
# Reaction
# --------------------
# ERGO : Ergotropic arousal (breathing, heart beat, etc) from 0 to 4

# TROPHO : Trophophic arousal (lump, stomach, crying...) from 0 to 3

# TEMPER : Felt temperature (-1 to 2)

# --------------------
# Expressive behaviour
# --------------------
# MOVE : from -1 (withdrawing) to +1 (forward)

# EXPRES : nonverbal activity, from 0 to 6

# PARAL : speech melody and tempo change from 0 to 3

# EXP1 : if laughing/smilig 1, else 0
# EXP2 : if sobbing/Crying
# EXP10 : if moving against

# CON : subject efforts to control
CON = ["NA", "NONE", "A LITTLE", "VERY MUCH"]

# EXPC : situation expected to occur
EXPC = CON
# PLEA : situation is pleasant
PLEA = CON
# FAIR : fairness of the situation
FAIR = CON
# MORL : morality of the situation
MORL = CON
# SELF : consequence on self estime
SELF = CON

# RELA : consequence on relationship with persons involved
RELA = ["NA", "NEGATIVE", "NONE", "POSITIVE"]

# PLAN : situation hindered current plans
PLAN = ["NA", "HELPED", "NO_MATTER", "HINDERED"]

# CAUS : who caused the situation
CAUS = ["NA", "SELF", "CLOSE", "OTHER", "IMPERSONNAL"]

# COPING : ability to cope
COPING = ["NO ACTION NECESSARY", "MANAGEABLE",
          "ESCAPABLE SITUATION", "DENIAL", "DOMINATED"]

# ---------------------------------------
# LIST OF AVAILABLE FIELDS/ATTRIBUTES
# ---------------------------------------
CONST_ISEAR_CODES = ["ID", "CITY", "COUN", "SUBJ", "SEX",
                     "AGE", "RELI", "PRAC", "FOCC", "MOCC",
                     "FIEL", "EMOT", "WHEN", "LONG", "INTS",
                     "ERGO", "TROPHO", "TEMPER", "EXPRES",
                     "MOVE", "EXP1", "EXP2", "EXP10", "PARAL",
                     "CON", "EXPC", "PLEA", "PLAN", "FAIR",
                     "CAUS", "COPING", "MORL", "SELF", "RELA",
                     "VERBAL", "NEUTRO", "Field1", "Field3",
                     "Field2", "MYKEY", "SIT", "STATE"]
