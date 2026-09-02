import os
from flask import Flask, request, jsonify
import replicate

app = Flask(__name__)

@app.route('/')
def home():
    return "Multi-Model AI Video Backend (Wan 2.1, Hunyuan, LTX) is running!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json or {}
    prompt = data.get("prompt", "Default Prompt")
    
    # يمكنك إرسال اسم النموذج من الfrontend، وإذا لم يُرسل نحدد Wan 2.1 كافتراضي
    model_choice = data.get("model", "wan-2.1")
    
    # خريطة تربط اسم النموذج بالـ ID الخاص به على Replicate
    models_map = {
        "wan-2.1": "wavespeedai/wan-2.1-t2v-480p",
        "hunyuan": "tencent/hunyuan-video",  # مثال لنموذج Hunyuan Video على Replicate
        "ltx-video": "lightricks/ltx-video"    # مثال لنموذج LTX-Video على Replicate
    }
    
    # اختيار النموذج المطلوب، أو استخدام Wan 2.1 كافتراضي إن لم يُعرف
    model_id = models_map.get(model_choice, "wavespeedai/wan-2.1-t2v-480p")
    
    print(f"Received prompt: {prompt} | Using Model: {model_choice} ({model_id})")
    
    try:
        # تشغيل النموذج عبر Replicate API
        output = replicate.run(
            model_id,
            input={"prompt": prompt}
        )
        
        video_url = output if isinstance(output, str) else output[0]
        
        return jsonify({
            "status": "success",
            "model_used": model_choice,
            "video_url": video_url
        })
    except Exception as e:
        print(f"Error generating video with {model_choice}: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
