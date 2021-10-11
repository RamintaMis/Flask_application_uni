from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# blueprints
from users.views import users_blueprint
from blog.views import blog_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(blog_blueprint)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
