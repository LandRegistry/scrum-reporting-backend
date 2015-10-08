from application import app, db
from flask import request, render_template, request, redirect, url_for, session, flash, jsonify, Response
from application.models import programmes, projects

import json

@app.route('/')
def login():
    return 'ok'

@app.route('/add/programme', methods=['POST'])
def add_programme():
    programme_request = request.get_json(force=True)
    db.session.add(programmes(programme_request['programme_name'], programme_request['programme_manager'], programme_request['service_manager']))
    db.session.commit()

    return Response(json.dumps({'status': 'ok'}),  mimetype='application/json')

@app.route('/get/programmes')
def get_programmes():
    res = programmes.query.filter().order_by(programmes.programme_name).all()
    res2 = []
    for row in res:
        res_sub = projects.query.filter(projects.programme_id == row.id).order_by(projects.project_name).all()
        project_array = []
        for row_sub in res_sub:
            project_array.append({'name': row_sub.project_name, 'id': row_sub.id, 'product_owner': row_sub.product_owner, 'scrum_master': row_sub.scrum_master, 'last_rag': 'a', 'last_sprint': '4', 'last_end_date': '01-01-2015'})

        res2.append({'name': row.programme_name, 'id': row.id, 'programme_manager': row.programme_manager, 'service_manager': row.service_manager, 'projects': project_array})

    return Response(json.dumps(res2),  mimetype='application/json')


@app.route('/add/project', methods=['POST'])
def add_project():
    project_request = request.get_json(force=True)
    db.session.add(projects(project_request['programme_id'], project_request['project_name'], project_request['product_owner'], project_request['scrum_master']))
    db.session.commit()
    return Response(json.dumps({'status': 'ok'}),  mimetype='application/json')

@app.route('/get/projects')
def get_projects():
    res = projects.query.filter().order_by(projects.project_name).all()
    res2 = []
    for row in res:
        res2.append({'name': row.project_name, 'programme_id': row.programme_id, 'id': row.id, 'product_owner': row.product_owner, 'scrum_master': row.scrum_master})
    return Response(json.dumps(res2),  mimetype='application/json')
