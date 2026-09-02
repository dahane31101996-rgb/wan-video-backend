from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Wan 2.1 Backend is running successfully!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json or {}
    prompt = data.get("prompt", "Default Prompt")
    print(f"Received prompt: {prompt}")
    
    return jsonify({
        "status": "success",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
