from flask import Flask, render_template, request
import marks as m

app = Flask(__name__, template_folder=r"D:\ML Course\After_Lecture11")

@app.route("/", methods=["GET", "POST"])
def home():
    y_pred = None
    if request.method == 'POST':
        x_value = request.form['x-value']
        y_pred = m.marks_prediction(x_value)
        print("Predicted Score:", y_pred)
    return render_template("index.html", prediction=y_pred)

if __name__ == "__main__":
    app.run(debug=True)
