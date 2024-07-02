from flask import Flask, request, render_template
import SQLAlchemy
app = Flask("Appli de ouf")
@app.route("/")
def page_daccueil():
    context = {
        "name": "Flask",
        "data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return render_template("index.html", **context)
@app.route("/test")
def page_test():
    name = request.args.get("name","No name")
    nickname = request.args.get("nickname","No nickname")
    return f"<h1>Test {name} {nickname}</h1>"
@app.route("/titre")
def page_niveau4():
    level = int(request.args.get("level","No level"))
    return f"<h{level}>Titre de niveau {level}</h{level}>"
@app.route("/titre/<int:level>/<string:texte>")
def page_niveau5(level, texte):
    return f"<h{level}>{texte}</h{level}><a href='/'>Menu</a>"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return f'<User {self.username}>'

db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.add(User(username="bob", email="bob.leponge@maison-ananas.com"))
    db.session.add(User(username="patrick", email="patrick.etoile@maison-ananas.com"))
    db.session.commit()

@app.route("/users")
def page_users():
    users = User.query.all()
    return render_template("users.html", users=users)
    


app.run(debug=True, port=3001)

