# score_calculator.py

def calculate_match_score(resume_text, jd_text):
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    matched_keywords = resume_words.intersection(jd_words)
    score = (len(matched_keywords) / len(jd_words)) * 100 if jd_words else 0
    return round(score, 2)
