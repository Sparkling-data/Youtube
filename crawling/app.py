from flask.json import jsonify
from flask import Flask, render_template, request
from buttoncrawling import SuperChat

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index_view():

    return render_template('prototype.html')


@app.route('/supercraw', methods=["get"])
def supercraw_view():

    return SuperChat().supercraw()


@app.route('/supercraw_week', methods=["get"])
def supercraw_weekview():

    return SuperChat().supercraw_week()


@app.route('/LiveRank', methods=["get"])
def LiveRank_view():

    return SuperChat().LiveRank()


@app.route('/LiveRank_week', methods=["get"])
def LiveRank_week_view():

    return SuperChat().LiveRank_week()


@app.route('/mostviewvideo', methods=["get"])
def mostviewvideo_view():

    return SuperChat().mostviewvideo()


@app.route('/mostviewvideoweek', methods=["get"])
def mostviewvideoweekview():

    return SuperChat().mostviewvideoweek()


@app.route('/subsoaring', methods=["get"])
def subsoaring_view():

    return SuperChat().subsoaring()


@app.route('/subsoaring_week', methods=["get"])
def subsoaring_week_view():

    return SuperChat().subsoaring_week()


@app.route('/mostview', methods=["get"])
def mostview_view():

    return SuperChat().mostview()


@app.route('/mostview_week', methods=["get"])
def smostview_week_view():

    return SuperChat().mostview_week()


@app.route('/mostviewad', methods=["get"])
def mostviewad_view():

    return SuperChat().mostviewad()


@app.route('/mostviewad_week', methods=["get"])
def mostviewad_week_view():

    return SuperChat().mostviewad_week()



if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")