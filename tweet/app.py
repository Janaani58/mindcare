from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load CSV dataset
csv_path = os.path.join(os.path.dirname(__file__), 'sentiment_tweets3.csv')
try:
    df = pd.read_csv(csv_path)
    print(f"✅ Dataset loaded: {len(df)} tweets")
except Exception as e:
    print(f"❌ Error loading CSV: {e}")
    df = None

# Comprehensive Emotion Keywords Dictionary
emotion_keywords = {
    "sad": ["sad", "depressed", "unhappy", "miserable", "down", "blue", "gloomy", "sorrowful", "tears", "crying", "cried", "weeping", "melancholy", "dejected", "downhearted"],
    "happy": ["happy", "joy", "love", "great", "wonderful", "amazing", "awesome", "excellent", "delighted", "thrilled", "blessed", "grateful", "smile", "laughing", "cheerful", "bright", "radiant"],
    "lonely": ["lonely", "alone", "isolated", "abandoned", "miss", "missing", "solitude", "lonesome", "forsaken", "unwanted", "neglected", "disconnected"],
    "excited": ["excited", "thrilled", "fantastic", "anticipation", "can't wait", "pumped", "energetic", "enthusiastic", "eager", "exhilarated"],
    "anxious": ["worried", "anxious", "nervous", "scared", "afraid", "stressed", "panic", "tension", "dread", "uneasy", "distressed", "overwhelmed", "apprehensive"],
    "angry": ["angry", "hate", "furious", "pissed", "rage", "mad", "livid", "resentment", "bitter", "outraged", "aggressive", "irritated"],
    "pain": ["pain", "hurt", "ache", "suffering", "agony", "torment", "anguish", "distress", "misery", "wounded", "grieving", "heartache"],
    "heartbreak": ["heartbreak", "heartbroken", "broken heart", "betrayed", "cheated", "rejected", "dumped", "shattered", "crushed", "loss", "lost you", "devastated"],
    "depression": ["depression", "depressed", "suicidal", "suicide", "hopeless", "worthless", "useless", "pointless", "empty", "numb", "dead inside", "giving up", "want to die"],
    "fear": ["fear", "terrified", "terror", "petrified", "horrified", "dread", "frightened", "trembling", "shaking", "phobia"],
    "guilt": ["guilty", "guilt", "regret", "shame", "ashamed", "remorse", "blame", "fault", "sorry", "apologize"],
    "betrayal": ["betrayed", "betrayal", "liar", "lie", "deceived", "manipulated", "fooled", "used", "fake", "untrustworthy"],
    "exhaustion": ["tired", "exhausted", "worn out", "drained", "fatigued", "burned out", "weary", "lifeless", "zombie"],
    "frustration": ["frustrated", "frustration", "annoyed", "irritated", "exasperated", "fed up", "sick of", "can't take it"],
    "low_esteem": ["worthless", "useless", "loser", "failure", "stupid", "dumb", "ugly", "weak", "pathetic", "not good enough"]
}

def analyze_sentiment(text):
    text_lower = text.lower()
    emotions = {}
    detected_keywords = {}
    
    # Count keywords for each emotion and track detected keywords
    for emotion, keywords in emotion_keywords.items():
        detected = [keyword for keyword in keywords if keyword in text_lower]
        emotions[emotion] = len(detected)
        if detected:
            detected_keywords[emotion] = detected
    
    # Find all emotions with detections (sorted by count)
    detected_emotions = {k: v for k, v in sorted(emotions.items(), key=lambda x: x[1], reverse=True) if v > 0}
    
    if not detected_emotions:
        dominant_emotion = "Neutral"
        risk_score = "✅ Low Risk - Positive Mindset"
        risk_color = "success"
        all_emotions = emotions
    else:
        dominant_emotion = max(detected_emotions, key=detected_emotions.get)
        
        # Calculate overall risk based on detected emotions
        high_risk_emotions = ["depression", "pain", "heartbreak", "suicidal", "fear", "guilt"]
        moderate_risk_emotions = ["sad", "anxious", "lonely", "betrayal", "low_esteem", "exhaustion"]
        
        dominant_upper = dominant_emotion.lower()
        
        if dominant_upper in ["depression", "pain", "suicidal"]:
            risk_score = "🔴 HIGH RISK - Serious Mental Health Concerns"
            risk_color = "danger"
        elif dominant_upper in ["heartbreak", "fear", "guilt", "betrayal"]:
            risk_score = "🟠 MODERATE-HIGH RISK - Significant Emotional Distress"
            risk_color = "warning"
        elif dominant_upper in ["sad", "anxious", "lonely", "low_esteem", "exhaustion", "frustration"]:
            risk_score = "🟡 MODERATE RISK - Emotional Concerns Detected"
            risk_color = "warning"
        elif dominant_upper in ["happy", "excited"]:
            risk_score = "✅ Low Risk - Positive Sentiment"
            risk_color = "success"
        else:
            risk_score = "✅ Low Risk"
            risk_color = "success"
        
        dominant_emotion = dominant_emotion.replace('_', ' ').title()
        all_emotions = emotions
    
    return {
        "dominant_emotion": dominant_emotion,
        "risk_score": risk_score,
        "risk_color": risk_color,
        "detected_emotions": detected_emotions,
        "detected_keywords": detected_keywords,
        "all_emotions": all_emotions,
        "text": text
    }

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html', dataset_loaded=(df is not None))

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form.get('text', '')
    if not user_input:
        return render_template('predict.html', error="Please enter some text", dataset_loaded=(df is not None))
    
    result = analyze_sentiment(user_input)
    return render_template('predict.html', 
                          prediction=result['risk_score'],
                          emotion=result['dominant_emotion'],
                          risk_color=result['risk_color'],
                          detected_emotions=result['detected_emotions'],
                          detected_keywords=result['detected_keywords'],
                          all_emotions=result['all_emotions'],
                          text=user_input,
                          dataset_loaded=(df is not None))

if __name__ == '__main__':
    app.run(debug=True)
