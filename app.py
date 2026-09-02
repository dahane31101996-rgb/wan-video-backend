@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "Default Prompt")
    
    return jsonify({
        "status": "success",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
    })
