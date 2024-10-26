def get_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "fever": "It sounds like you may have a fever. Please consult with a healthcare provider for further assistance.",
        "headache": "I'm sorry to hear that. A headache could be caused by various reasons, like dehydration, stress, or even migraines. Consider resting, drinking water, or consulting a healthcare provider if it persists.",
        "cough": "A cough can be due to a common cold, allergies, respiratory infections, or even smoking. If it persists or is severe, you should seek medical advice.",
        "stomach ache": "Stomach aches can be caused by indigestion, stress, infections, or even food poisoning. Try resting and drinking plenty of fluids. If the pain is severe, please consult a doctor.",
        "sore throat": "A sore throat could be caused by an infection like a cold, strep throat, or allergies. Stay hydrated and consider seeing a healthcare provider if it doesn't improve in a few days.",
        "rash": "Rashes can have many causes, including allergies, infections, heat, or certain medications. It's best to see a healthcare professional for an accurate diagnosis.",
        "nausea": "Nausea can occur for various reasons including motion sickness, food poisoning, pregnancy, or anxiety. Rest and stay hydrated. If it persists, consult a healthcare provider.",
        "shortness of breath": "Shortness of breath can be a sign of a serious condition such as asthma, heart problems, or anxiety. Please seek medical attention immediately if you're experiencing this.",
        "chest pain": "Chest pain can be serious and may indicate a heart problem, pneumonia, or gastrointestinal issues. Please seek emergency medical care immediately.",
        "dizziness": "Dizziness can be caused by dehydration, low blood sugar, ear infections, or anemia. Sit down, rest, and consult a healthcare provider if it continues.",
        "fatigue": "Fatigue can be caused by lack of sleep, stress, anemia, or other underlying conditions. Ensure you are getting enough rest, and if it persists, consult a healthcare provider.",
        "vomiting": "Vomiting can occur due to stomach infections, food poisoning, or motion sickness. Stay hydrated and rest. If it persists or is severe, see a healthcare professional.",
        "diarrhea": "Diarrhea can be caused by infections, food intolerance, or digestive disorders. Stay hydrated and consult a healthcare provider if it lasts more than a couple of days.",
        "back pain": "Back pain could be due to muscle strain, poor posture, or a more serious condition like a herniated disc. Rest, avoid heavy lifting, and consult a healthcare provider if it persists.",
        "joint pain": "Joint pain can result from arthritis, injury, or overuse. Rest the joint, apply ice, and consult a healthcare provider if the pain is ongoing.",
        "ear pain": "Ear pain could be caused by an ear infection, sinus congestion, or even jaw problems. If the pain is severe or persistent, consult a healthcare professional.",
        "eye pain": "Eye pain can result from strain, infection, or injury. If you experience severe pain or vision changes, please see an eye specialist immediately.",
        "abdominal pain": "Abdominal pain can be caused by indigestion, gas, appendicitis, or other digestive issues. If the pain is severe or does not improve, seek medical advice.",
        "allergies": "Allergies can cause symptoms like sneezing, itching, and rashes. Avoid known allergens and consider taking antihistamines. If symptoms are severe, consult a healthcare provider.",
        "burning sensation": "A burning sensation could be due to acid reflux, nerve damage, or skin irritation. Consult a healthcare provider if this persists or worsens.",
        "palpitations": "Palpitations can be caused by anxiety, caffeine, or heart problems. If they are frequent or accompanied by other symptoms, seek medical attention.",
        "constipation": "Constipation can result from a lack of fiber, dehydration, or inactivity. Increase your water and fiber intake, and consult a healthcare provider if it persists.",
        "blurred vision": "Blurred vision could be due to eye strain, dehydration, or a more serious condition like diabetes. If it persists, consult an eye specialist.",
        "muscle cramps": "Muscle cramps can be caused by dehydration, overuse, or a lack of minerals. Stretch gently and stay hydrated. If cramps are frequent, consult a healthcare provider.",
        "tingling sensation": "Tingling could be caused by poor circulation, nerve damage, or anxiety. If it persists, consult a healthcare professional.",
        "sweating": "Excessive sweating could be caused by anxiety, heat, or a medical condition like hyperthyroidism. Consult a healthcare provider if it is affecting your daily life."
    }

    for symptom, response in responses.items():
        if symptom in user_input:
            return response

    return "I'm not sure about that. Could you please provide more details?"

# Add more symptoms and detailed responses here as needed.
