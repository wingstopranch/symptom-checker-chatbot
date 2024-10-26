from flask import Flask, request, jsonify, render_template
import symptom_analyzer
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    # Simulate a delay to show the typing indicator
    time.sleep(1)  # This can be adjusted or removed based on real-time processing needs
    response = symptom_analyzer.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
