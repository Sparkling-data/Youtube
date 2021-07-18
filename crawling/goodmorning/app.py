from flask.json import jsonify
from flask import Flask, render_template, request
from buttoncrawling import SuperChat
from chart import googlechart

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


@app.route('/mostviewvideo_week', methods=["get"])
def mostviewvideo_week_view():

    return SuperChat().mostviewvideo_week()


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
def mostview_week_view():

    return SuperChat().mostview_week()


@app.route('/mostviewad', methods=["get"])
def mostviewad_view():

    return SuperChat().mostviewad()


@app.route('/mostviewad_week', methods=["get"])
def mostviewad_week_view():

    return SuperChat().mostviewad_week()







@app.route('/supercraw_chart', methods=["post"])
def superchat_chart():

    return googlechart().superchat(request.form.get("chart_num"),request.form.get("chart_date"))


@app.route('/LiveRank_chart', methods=["post"])
def LiveRank_chart():


    return googlechart().LiveRank(request.form.get("chart_num"),request.form.get("chart_date"))

@app.route('/mostviewvideo_chart', methods=["post"])
def mostviewvideo_chart():



    return googlechart().mostviewvideo(request.form.get("chart_num"),request.form.get("chart_date"))

@app.route('/subsoaring_chart', methods=["post"])
def subsoaring_chart():



    return googlechart().subsoaring(request.form.get("chart_num"),request.form.get("chart_date"))

@app.route('/mostview_chart', methods=["post"])
def mostview_chart():


    return googlechart().mostview(request.form.get("chart_num"),request.form.get("chart_date"))


@app.route('/mostviewad_chart', methods=["post"])
def mostviewad_chart():



    return googlechart().mostviewad(request.form.get("chart_num"),request.form.get("chart_date"))


@app.route('/supercraw_chart_week', methods=["post"])
def superchat_chart_week():

    # print(request.form.get("chart_num2"))
    # print(request.form.get("chart_date2"))

    return googlechart().superchat_week(request.form.get("chart_num2"),request.form.get("chart_date2"))



if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
