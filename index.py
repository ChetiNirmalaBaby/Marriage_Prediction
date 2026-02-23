from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

# --------------------------
# Telugu Astrology Personality
# --------------------------
def telugu_prediction(raasi):
    predictions = {
        "Mesha (Aries)": "శక్తివంతమైన, ధైర్యవంతుడైన, ఆత్మవిశ్వాసం ఎక్కువ",
        "Vrishabha (Taurus)": "సహనశీలి, భద్ర, ప్రేమలో స్థిరమైన వ్యక్తి",
        "Mithuna (Gemini)": "తెలివైన, అనువైన, సామాజికతలో చురుకైన",
        "Karka (Cancer)": "భావోద్వేగాలు ఎక్కువ, కుటుంబం పై ప్రేమ",
        "Simha (Leo)": "నాయకత్వ లక్షణాలు, అహంకారం కొంత ఎక్కువ",
        "Kanya (Virgo)": "వివేకవంతులు, నిష్టావంతులు, విశ్లేషకులు",
        "Tula (Libra)": "సహజసిద్ధమైన, సౌందర్యరుచితో, న్యాయపరులు",
        "Vrischika (Scorpio)": "ఆకర్షణ, స్థిరత్వం, సంకల్పవంతులు",
        "Dhanu (Sagittarius)": "ఆవేశవంతులు, మార్గదర్శకత్వ లక్షణాలు",
        "Makara (Capricorn)": "పనిమీద దృష్టి, సాధారణంగా ఆత్మవిశ్వాసం",
        "Kumbha (Aquarius)": "సృజనాత్మక, స్వతంత్ర, మానవతా భావన",
        "Meena (Pisces)": "సున్నితమైన, కల్పనాశక్తి, మానసిక సహనం"
    }
    return predictions.get(raasi, "")

# --------------------------
# Marriage Year Prediction
# --------------------------
def predict_marriage_year(dob_str, raasi, gender="male"):
    dt = datetime.strptime(dob_str, "%Y-%m-%d")
    birth_year = dt.year

    if gender.lower() == "male":
        start_age, end_age = 23, 30
    else:
        start_age, end_age = 20, 27

    raasi_shift = {
        "Mesha (Aries)": 1, "Vrishabha (Taurus)": 2, "Mithuna (Gemini)": 1,
        "Karka (Cancer)": 2, "Simha (Leo)": 1, "Kanya (Virgo)": 2,
        "Tula (Libra)": 1, "Vrischika (Scorpio)": 2, "Dhanu (Sagittarius)": 1,
        "Makara (Capricorn)": 2, "Kumbha (Aquarius)": 1, "Meena (Pisces)": 2
    }
    shift = raasi_shift.get(raasi, 1)

    return [birth_year + age + shift for age in range(start_age, end_age + 1)]

# --------------------------
# HTML Template
# --------------------------
page = """
<html>
<head>
<title>Telugu Astrology Marriage Predictor</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {background: linear-gradient(135deg,#0d0f19,#1f2a44); color:white; font-family:Arial,sans-serif; text-align:center; margin:0; padding:0;}
.container {padding:20px;}
input,select,button {padding:12px; margin:8px; border-radius:8px; border:none; font-size:16px; width:80%; max-width:300px;}
button {background:#ffcc00; font-weight:bold; cursor:pointer;}
.result-box {background:#1a1f33; padding:20px; border-radius:12px; margin-top:20px; max-width:450px; margin:auto;}
.card {background:#2c3e50; padding:15px; border-radius:10px; margin:10px 0;}
.card p {margin:5px 0; font-size:16px;}
h1 {margin-bottom:20px;}
ul {list-style:none; padding:0;}
li {margin:4px 0; padding:4px 0; background:#34495e; border-radius:6px;}
@media screen and (max-width:480px) {input,button,select {width:90%;}}
</style>
</head>
<body>
<div class="container">
<h1>💍 Telugu Astrology Marriage Predictor</h1>

<form method="POST">
<input type="text" name="name" placeholder="Enter Name" required><br>
<input type="date" name="dob" required><br>
<input type="time" name="tob" required><br>
<select name="raasi" required>
<option value="">Select Raasi</option>
<option>Mesha (Aries)</option><option>Vrishabha (Taurus)</option>
<option>Mithuna (Gemini)</option><option>Karka (Cancer)</option>
<option>Simha (Leo)</option><option>Kanya (Virgo)</option>
<option>Tula (Libra)</option><option>Vrischika (Scorpio)</option>
<option>Dhanu (Sagittarius)</option><option>Makara (Capricorn)</option>
<option>Kumbha (Aquarius)</option><option>Meena (Pisces)</option>
</select><br>
<select name="nakshatra" required>
<option value="">Select Nakshatra</option>
<option>Ashwini</option><option>Bharani</option><option>Krittika</option><option>Rohini</option>
<option>Mrigashira</option><option>Ardra</option><option>Punarvasu</option><option>Pushya</option>
<option>Ashlesha</option><option>Magha</option><option>Purva Phalguni</option><option>Uttara Phalguni</option>
<option>Hasta</option><option>Chitra</option><option>Swati</option><option>Vishakha</option>
<option>Anuradha</option><option>Jyeshta</option><option>Mula</option><option>Purva Ashadha</option>
<option>Uttara Ashadha</option><option>Shravana</option><option>Dhanishta</option><option>Shatabhisha</option>
<option>Purva Bhadrapada</option><option>Uttara Bhadrapada</option><option>Revati</option>
</select><br>
<select name="pada" required>
<option value="">Select Pada</option>
<option>1</option><option>2</option><option>3</option><option>4</option>
</select><br>
<select name="gender" required>
<option value="male">Male</option>
<option value="female">Female</option>
</select><br>
<button type="submit">Predict Marriage Year</button>
</form>

{% if result %}
<div class="result-box">
<h2>{{result.name}}</h2>
<div class="card"><p>🌙 Raasi: {{result.raasi}}</p></div>
<div class="card"><p>🌟 Nakshatra: {{result.nakshatra}}</p></div>
<div class="card"><p>🪐 Pada: {{result.pada}}</p></div>
<div class="card"><p>📝 Telugu Astrology: {{result.prediction}}</p></div>
<div class="card"><p>💍 Possible Marriage Years:</p>
<ul>
{% for y in result.marriage_years %}
<li>{{y}}</li>
{% endfor %}
</ul></div>
</div>
{% endif %}

</div>
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    result = None
    if request.method == "POST":
        name = request.form["name"]
        dob = request.form["dob"]
        tob = request.form["tob"]
        raasi = request.form["raasi"]
        nakshatra = request.form["nakshatra"]
        pada = request.form["pada"]
        gender = request.form["gender"]

        prediction = telugu_prediction(raasi)
        marriage_years = predict_marriage_year(dob, raasi, gender)

        result = {
            "name": name,
            "raasi": raasi,
            "nakshatra": nakshatra,
            "pada": pada,
            "prediction": prediction,
            "marriage_years": marriage_years
        }

    return render_template_string(page, result=result)

if __name__ == "__main__":
    app.run(debug=True)

