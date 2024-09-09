import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(user_id, user_type, n=10):
    # Load user data
    users = pd.read_csv('users.csv')
    
    # Separate investors and founders
    investors = users[users['user_type'] == 'investor']
    founders = users[users['user_type'] == 'founder']
    
    # Choose the appropriate dataset based on user type
    if user_type == 'investor':
        target_users = founders
    else:
        target_users = investors
    
    # Create TF-IDF vectorizer
    tfidf = TfidfVectorizer(stop_words='english')
    
    # Fit and transform the bio text
    tfidf_matrix = tfidf.fit_transform(target_users['bio'])
    
    # Get the user's bio
    user_bio = users[users['user_id'] == user_id]['bio'].iloc[0]
    
    # Transform the user's bio
    user_tfidf = tfidf.transform([user_bio])
    
    # Calculate cosine similarity
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    
    # Get top N similar users
    similar_users = target_users.iloc[cosine_similarities.argsort()[-n:][::-1]]
    
    return similar_users['user_id'].tolist()