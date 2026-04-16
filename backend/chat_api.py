from flask import Blueprint, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

chat_bp = Blueprint("chat_bp", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        return jsonify({"error": "GEMINI_API_KEY not set"}), 500

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

    payload = {
        "contents": [
            {"parts": [{"text": user_message}]}
        ]
    }

    try:
        response = requests.post(
            url,
            params={"key": gemini_api_key},
            json=payload,
            timeout=30
        )

        result = response.json()

        if "candidates" not in result:
            return jsonify({"error_from_gemini": result}), 500

        reply = result["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"response": reply}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
