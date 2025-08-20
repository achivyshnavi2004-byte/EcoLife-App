from flask import Flask, render_template, request

app = Flask(__name__)
def calculate_carbon(electricity, travel_km, meat_meals):
    co2_electricity = electricity * 0.233     
    co2_travel = travel_km * 0.21              
    co2_meat = meat_meals * 5                 
    total = co2_electricity + co2_travel + co2_meat
    return total

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            electricity = float(request.form["electricity"])
            travel = float(request.form["travel"])
            meat = int(request.form["meat"])
            total_co2 = calculate_carbon(electricity, travel, meat)
            
            if total_co2 < 200:
                advice = "Great! Your lifestyle is relatively eco-friendly 🌱"
            elif total_co2 < 500:
                advice = "Average footprint. Consider small changes to reduce CO2."
            else:
                advice = "High footprint. Take steps to live more sustainably!"
                
            result = f"{total_co2:.2f} kg CO2 - {advice}"
        except:
            result = "Invalid input. Please enter numbers only."
    return render_template("index.html", result=result)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
