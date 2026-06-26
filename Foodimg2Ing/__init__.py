from flask import Flask

app = Flask(__name__,template_folder='Templates')
app.secret_key = "recipegpt-secret-key"


from Foodimg2Ing import routes