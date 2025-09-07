import math

# Define positive/negative word sets
positive_words = {"good", "great", "amazing", "enjoyable", "nice", "fantastic", "love", "excellent", "wonderful", "best"}
negative_words = {"bad", "worst", "boring", "terrible", "awful", "poor", "hate", "2nd grade", "waste", "disappointing"}
pronouns = {"i", "me", "my", "you", "your"}

# Feature extraction function (same as before)
def analyze_review(review):
    review_lower = review.lower()
    words = review_lower.split()

    pos_count = 0
    neg_count = 0
    pronoun_count = 0
    contains_no = 1 if "no" in words else 0
    exclamation_count = review.count("!")
    total_words = len(words)

    for word in words:
        word_clean = word.strip(".,!?")
        if word_clean in positive_words:
            pos_count += 1
        elif word_clean in negative_words:
            neg_count += 1
        if word_clean in pronouns:
            pronoun_count += 1

    return [pos_count, neg_count, contains_no, pronoun_count, exclamation_count, total_words]

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Prediction function using sigmoid
def predict_sentiment(features, weights, bias):
    # Weighted sum: z = w1*x1 + w2*x2 + ... + wn*xn + b
    z = sum(f * w for f, w in zip(features, weights)) + bias
    prob = sigmoid(z)
    return prob

# Example weights (chosen manually for demo — normally learned from training data)
weights = [1.2, -1.5, -0.5, 0.3, 0.8, 0.1]  # weights for features
bias = 0.0  # threshold shift

# Input review
review_text = input("Enter a review: ")
features = analyze_review(review_text)

# Predict probability
prob = predict_sentiment(features, weights, bias)

# Final classification
if prob >= 0.5:
    print(f"\nReview classified as POSITIVE (probability = {prob:.4f})")
else:
    print(f"\nReview classified as NEGATIVE (probability = {prob:.4f})")
