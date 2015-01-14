from flask import Flask, render_template


app = Flask(__name__)

from flask.ext.assets import Environment, Bundle
assets = Environment(app)

css_all = Bundle(
        'less/style.less',
        filters='less, cssmin',
        output='gen/min.css',
)

# assets get passed templates to be rendered
assets.register('css_all', css_all)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

