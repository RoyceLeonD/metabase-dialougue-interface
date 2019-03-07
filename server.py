#Setting up the imports for the application
from handler import *

#Setting up the flask server
app = Flask(__name__)

#Refresing the render_templates
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def index_post():
    login_username = request.form['username']
    login_password = request.form['password']

    response = login(login_username, login_password)

    print(response.json())


