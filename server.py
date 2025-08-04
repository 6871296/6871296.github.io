import flask
app=flask.Flask()

err_causing='未知';err-page='未知'

@app.route('/')
def index():
    return flask.render_template('index.html',)

@app.route('/post-reader',methods=['post'])
def reader():
    #
    return flask.render_template(request.form['next-page'])

@app.route('/err')
def error():
    return flask.render_template('error.html',causing=err_causing)

@app.route('/err-catcher',methds=['post'])
def err_catch():
    return 