from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def analyze_submission(task, submission):

    texts = [task, submission]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    match_score = round(similarity * 100)

    # simple quality estimation
    length_score = min(len(submission.split()) * 2, 100)

    # originality (simple heuristic)
    originality = 100 - abs(match_score - length_score)

    decision = "APPROVED" if match_score > 40 else "REVIEW REQUIRED"

    return {
        "requirement_match": match_score,
        "quality_score": length_score,
        "originality": originality,
        "decision": decision
    }