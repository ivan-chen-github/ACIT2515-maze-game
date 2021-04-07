from flask import Flask

app = Flask(__name__)

@app.route("/")
def highscores():
    return """
<!DOCTYPE html>
<html>

<head>
<style>
body {background-color: #99ccff}
h1 {text-align: center}
h2 {text-align: center}
</style>
</head>

<body>
<h1>Maze Demo</h1>
<h2>Highscores<h2>
</body>

</html>
"""

if __name__ == "__main__":
    app.run()