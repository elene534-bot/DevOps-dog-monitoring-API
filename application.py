from flask import Flask, jsonify

app = Flask(__name__)

# ძაღლების მონაცემთა ბაზა (სიმულაცია)
DOGS_DATABASE = [
    {
        "id": 1,
        "type": "ქუჩის",
        "breed": "შერეული",
        "color": "ყავისფერი",
        "size": "საშუალო",
        "health_issue": "კოჭლობს მარჯვენა ფეხზე",
        "aggression_level": 2,
        "location": "ვაკის პარკის მიმდებარედ",
        "caretaker": "გიორგი",
        "caretaker_phone": "599112233"
    },
    {
        "id": 2,
        "type": "შინაური",
        "breed": "გერმანული ნაგაზი",
        "color": "შავ-ყავისფერი",
        "size": "დიდი",
        "health_issue": "ჯანმრთელი",
        "aggression_level": 7,
        "location": "დიდუბე, კერძო ეზო",
        "caretaker": "ნინო",
        "caretaker_phone": "598445566"
    }
]

@app.route('/')
def home():
    return jsonify({"status": "healthy", "service": "Dog Monitoring System API"}), 200

# ყველა ძაღლის სიის წამოღება
@app.route('/dogs', methods=['GET'])
def get_all_dogs():
    return jsonify({"total": len(DOGS_DATABASE), "dogs": DOGS_DATABASE}), 200

# მაღალი აგრესიის მქონე ძაღლების ფილტრი (> 5)
@app.route('/dogs/high-aggression', methods=['GET'])
def get_high_aggression_dogs():
    dangerous_dogs = [dog for dog in DOGS_DATABASE if dog["aggression_level"] > 5]
    return jsonify({"count": len(dangerous_dogs), "dogs": dangerous_dogs}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)