from flask import Flask, render_template

from controllers.class_controller import class_blueprint
# from controllers.member_controller import member_blueprint

app = Flask(__name__)

app.register_blueprint(class_blueprint)
# app.register_blueprint(member_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')