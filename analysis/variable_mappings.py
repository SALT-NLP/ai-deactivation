import numpy as np

EMO_SCORE_MAP = {
    "all the time": 6, 
    "all of the time": 6,
    "very often": 5,
    "often": 4, 
    "some of the time": 3, 
    "rarely": 2, 
    "very rarely": 1,
    "none of the time": 0}
EMO_REVERSE_MAP = {
    0: 6, 
    1: 5, 
    2: 4, 
    3: 3, 
    4: 2, 
    5: 1, 
    6: 0}
EMO_REVERSED = {"depressed", "anxious"}

# Well-being: Well-being Survey
WB_COLS = [f"Well-being survey_{i}" for i in range(1, 7)]
WB_REVERSED = {"Well-being survey_3", "Well-being survey_4"}
WB_SCORE_MAP = {
    "strongly disagree": 0, 
    "disagree": 1, 
    "somewhat disagree": 2,
    "neither agree nor disagree": 3, 
    "somewhat agree": 4,
    "agree": 5, 
    "strongly agree": 6,
}

# ── BPNSFS (baseline & midpoint: 1-25, skip 17; dairy: 1-24, no skip) ───────
BPNSFS_REVERSED = {f"BPNSFS_{n}" for n in [2,4,6,8,10,12,14,16,19, 21, 23, 25]}
BPNSFS_REVERSED_DIARY = {f"BPNSFS_{n}" for n in range(2, 25, 2)}
BPNSFS_REVERSE_MAP = {
    0: 6,
    1: 5,
    2: 4,
    3: 3,
    4: 2,
    5: 1,
    6: 0,
}
BPNSFS_SCORE_MAP = {
    "not true at all": 0,
    "untrue": 1,
    "somewhat untrue": 2,
    "neither true or untrue": 3,
    "neither true nor untrue": 3,
    "somewhat true": 4,
    "true": 5,
    "completely true": 6,
}

NEEDS_BASE = {
    "Autonomy":    [1, 7, 13, 20, 2, 8, 14, 21],
    "Autonomy_Satisfaction": [1, 7, 13, 19],
    "Autonomy_Frustration": [2, 8, 14, 21],
    "Relatedness": [3, 9, 15, 22, 4, 10, 16, 23],
    "Relatedness_Satisfaction": [3, 9, 15, 22],
    "Relatedness_Frustration": [4, 10, 16, 23],
    "Competence":  [5, 11, 18, 24, 6, 12, 19, 25],
    "Competence_Satisfaction": [5, 11, 18, 24],
    "Competence_Frustration": [6, 12, 19, 25],
}
NEEDS_DIARY_COLUMNS = {
    "Autonomy":    [1, 7, 13, 19, 2, 8, 14, 20],
    "Autonomy_Satisfaction": [1, 7, 13, 19],
    "Autonomy_Frustration": [2, 8, 14, 20],
    "Relatedness": [3, 9, 15, 21, 4, 10, 16, 22],
    "Relatedness_Satisfaction": [3, 9, 15, 21],
    "Relatedness_Frustration": [4, 10, 16, 22],
    "Competence":  [5, 11, 17, 23, 6, 12, 18, 24],
    "Competence_Satisfaction": [5, 11, 17, 23],
    "Competence_Frustration": [6, 12, 18, 24],
}

LONELINESS_MAP = {
    "none of the time": 0,
    "very rarely": 1,
    "rarely": 2,
    "some of the time": 3,
    "often": 4,
    "very often": 5,
    "all the time": 6,
}

# Social satisfaction: Social Satisfaction Scale
SOCIAL_SATISFACTION_MAP = {
    "extremely dissatisfied": -3,
    "moderately dissatisfied": -2,
    "slightly dissatisfied": -1,
    "neither satisfied nor dissatisfied": 0,
    "slightly satisfied": 1,
    "moderately satisfied": 2,
    "extremely satisfied": 3,
}

TIME_SOCIAL_MAP = {
    "less than 10 minutes per day": 0,
    "10–30 minutes per day": 1,
    "31–60 minutes per day": 2,
    "1–2 hours per day": 3,
    "2–3 hours per day": 4,
    "3+ hours per day": 5,
}

EOD_TIME_MAP = {
    "<10 minutes": 0,
    "10-30 minutes": 1,
    "31-60 minutes": 2,
    "1-2hrs": 3,
    "2-4hrs": 4,
    "4-8hrs": 5,
    "8+ hrs": 6,
}

INPERSON_MEET_MAP = {
    "None": 0,
    "none": 0,
    "1-2": 1,
    "3-4": 2,
    "5-6": 3, 
    "7-8": 4,
    "9-10": 5,
    "more than 10": 6,
}

LUBBEN_MAP = {
    "none": 0,
    "one": 1,
    "two": 2,    
    "three or four": 3,
    "five to eight": 4,
    "nine or more": 5,
}

TIME_USE_MAP = {
    '< 10 min': 0,
    '10-30 min': 1,
    '31-60 min': 2,
    '1hr-2hr': 3,
    '2-3hr': 4,
    '3+ hrs': 5,
}

LUBBEN_ALT_MAP = {
    "none": 0,
    "1": 1,
    "2": 2,    
    "3 or 4": 3,
    "5 to 8": 4,
    "9 or more": 5,
}

PRODUCTIVITY_LIKELIHOOD_MAP = {
    "never": -3,
    "very unlikely": -2,
    "unlikely": -1,
    "neither likely nor unlikely": 0,
    "likely": 1,
    "very likely": 2,
    "definitely": 3,
    "i don't do this task": np.nan
}

PRODUCTIVITY_QUALITY_MAP = {
    "not at all": -3,
    "very poorly": -2,
    "poorly": -1,
    "moderately": 0,
    "well": 1,
    "very well": 2,
    "extremely well": 3,
    "i don't do this task": np.nan
}

TIME_USE_MAP = {
    "< 10 min": 0,
    "10-30 min": 1,
    "31-60 min": 2,
    "1hr-2hr": 3,
    "2-3hr": 4,
    "3+ hrs": 5,
}

ATUS_MAP = {
    "none": 0,
    "< 30min": 1,
    "30min-1hr": 2,
    "1hr-2hr": 3,
    "2hr-4hr": 4,
    "4-6hr": 5,
    ">6hr": 6,
}

AGREEMENT_7_MAP = {
    "strongly disagree": -3,
    "disagree": -2,
    "somewhat disagree": -1,
    "neither agree nor disagree": 0,
    "somewhat agree": 1,
    "agree": 2,
    "strongly agree": 3,
}

AGREEMENT_5_MAP = {
    "strongly disagree": -2,
    "somewhat disagree": -1,
    "neither agree nor disagree": 0,
    "somewhat agree": 1,
    "agree": 2,
}

BEHAVIOR_CHANGE_MAP = {
    "a lot less": -2,
    "a little less": -1,
    "same": 0,
    "a little more": 1,
    "a lot more": 2,
}

CHAT_USAGE_MAP = {
    "< 15 minutes per day": 0,
    "15–30 minutes per day": 1,
    "31–60 minutes per day": 2,
    "1–2 hours per day": 3,
    "more than 2 hours per day": 4,
}

PURPOSE_MAP = {
    "never": 0,
    "less than once a month": 1,
    "once a month": 2,
    "a few times a month": 3,
    "a few times a week": 4,
    "about once a day": 5,
    "multiple times per day": 6,
}

PURPOSE_COL_NAMES = {
    "Purpose_1": "Productivity",
    "Purpose_2": "Entertainment",
    "Purpose_3": "Social",
    "Purpose_4": "Novelty",
}

TENURE_MAP = {
    "less than 1 year": 0,
    "1–6 months": 1,
    "6–12 months": 2,
    "1–2 years": 3,
    "more than 2 years": 4,
}

GENDER_MAP = {
    "male": 0,
    "female": 1,
    "non-binary / third gender": 2,
    "prefer to self-describe": 2,
    "prefer not to say": 4,
}

AGE_MAP = {
    "18-24 years old": 0,
    "25-34 years old": 1,
    "35-44 years old": 2,
    "45-54 years old": 3,
    "55-64 years old": 4,
    "65+ years old": 5,
}

RACE_MAP = {
    "white or caucasian": 0,
    "black or african american": 1,
    "asian": 2,
    "american indian/native american or alaska native": 3,
    "native hawaiian or other pacific islander": 4,
    "other": 5,
    "prefer not to say": 6,
    "mixed race": 7,
}

EDUCATION_MAP = {
    "some high school or less": 0,
    "high school diploma or ged": 1,
    "some college, but no degree": 2,
    "associates or technical degree": 3,
    "bachelor’s degree": 4,
    "graduate or professional degree (ma, ms, mba, phd, jd, md, dds etc.)": 5,
    "prefer not to say": 6,
}

INCOME_MAP = {
    "less than $25,000": 0,
    "$25,000-$49,999": 1,
    "$50,000-$74,999": 2,
    "$75,000-$99,999": 3,
    "$100,000-$149,999": 4,
    "$150,000 or more": 5,
    "prefer not to say": 6,
}

RELATIONSHIP_MAP = {
    "single (never married/not in a relationship)": 0,
    "in a relationship / dating": 1,
    "married": 2,
    "in a domestic partnership / civil union": 3,
    "separated": 4,
    "widowed": 5,
    "divorced": 6,
    "prefer not to disclose": 7,
}

SURVEY2DAY = {
    "baseline": 0,
    "diary1": 3,
    "midline": 7,
    "diary2": 10,
    "endline": 14,
}