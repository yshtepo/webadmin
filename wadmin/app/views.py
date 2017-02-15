from flask import render_template, flash, redirect
from app import app
from .forms import InfoForm, LoginInfoForm, AktForm
from .db_select import *
from shutil import copyfile

@app.route('/')
@app.route('/index')
def index():
    count_ik = get_active_ik()
    count_bk = get_active_bk()
    return render_template('index.html',
        title = 'WebAdmin',
        info = info,
        count_ik = count_ik,
        count_bk = count_bk)


@app.route('/info', methods = ['GET', 'POST'])
def info():
    form = InfoForm()
    if form.validate_on_submit():
        name = get_client_name(form.inn.data)
        if len(name) == 0:
            name.append("Клиент не найден")
            return render_template('info.html',
                name1 = name[0],
                form = form)
        else:
            arm = get_client_arm(form.inn.data)
            fenabled = get_client_fenabled(form.inn.data)
            startdate = get_client_start_date(form.inn.data)
            finishdate = get_client_finish_date(form.inn.data)
            return render_template('info.html',
                arm = int(arm[0]),
                name = name[0],
                fenabled = fenabled,
                sd = str(startdate[0]),
                fd = str(finishdate[0]),
                form = form)
    return render_template('info.html',
        title = 'Info',
        form = form)

@app.route('/akt', methods = ['GET', 'POST'])
def akt():
    form = AktForm()
    if form.validate_on_submit():
        akt = get_akt(form.inn.data)
        if str(akt) != "Нет запроса":
            copyfile('path_to_file' + str(akt), 'path_to_new_file'+ str(akt))
            return render_template('akt.html',
                title = 'akt',
                download = 'cкачать',
                akt = '/static/akt/' + str(akt),
                form = form)
        else:
            return render_template('akt.html',
                title = 'akt',
                download = 'нет запроса',
                akt = str(akt),
                form = form)
    return render_template('akt.html',
        title = 'akt',
        form = form)
