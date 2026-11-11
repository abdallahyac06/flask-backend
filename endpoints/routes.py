from flask import Blueprint, jsonify


api_bp = Blueprint("api", __name__)


@api_bp.get("/api/data")
def get_sample_data():
    return jsonify(
        {
            "first_name": "Abdallah",
            "last_name": "Yacine",
            "age": 20,
            "hobbies": ["Mobile Development", "Software Engineering"]
        }
    )


@api_bp.get("/api/items/<int:item_id>")
def get_item(item_id: int):
    return jsonify(
        {
            "item": {
                "id": item_id,
                "name": f"Sample Item {item_id}",
                "value": item_id * 100,
            },
            "timestamp": "2024-01-01T00:00:00Z",
        }
    )
