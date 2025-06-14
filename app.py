from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.json['topic']
    prompt = f"Create 5 multiple choice quiz questions with 4 options each on the topic: {topic}. Label the correct option."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        ai_text = response['choices'][0]['message']['content']
        return jsonify({'questions': ai_text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

