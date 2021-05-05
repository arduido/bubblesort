from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

def bubble_sort(input_list):
    # range len parameter is how we determine the number of times to go through the list
    for i in range(len(input_list)):
        # make the last pair of adjacent elements n-2, n-1
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j+1]:
                # this will swap if the condition is met
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        numbs = request.form['nums']
        numbers = list(numbs.split())
        bubble_sort(numbers)
        return redirect(url_for("numbers", nums=numbers))
    return render_template("index.html")

@app.route("/<nums>")
def numbers(nums):
    
    return f"<p>{nums}</p>"

if __name__ == "__main__":
    app.run(debug=True)