from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Wan 2.1 Backend is running successfully!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "Default Prompt")
    print(f"Received prompt: {prompt}")
    
    # رابط فيديو تجريبي مؤكد للربط والتأكد من عمل الواجهة
    return jsonify({
        "status": "success",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
