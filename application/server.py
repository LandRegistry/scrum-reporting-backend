from application import app, db
from flask import request, render_template, request, redirect, url_for, session, flash, jsonify, Response
from application.models import programmes, projects, sprints, burndown

import json

@app.route('/')
def login():
    return '6'

### Programme ###

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

            sprint_res_sub = sprints.query.filter(sprints.project_id == row_sub.id).order_by(sprints.sprint_number.desc()).first()

            cur_sprint_number = ''
            cur_sprint_end_date = ''
            cur_sprint_rag = ''
            cur_sprint_id = ''
            if sprint_res_sub:
                cur_sprint_number = sprint_res_sub.sprint_number
                cur_sprint_end_date = sprint_res_sub.end_date
                cur_sprint_rag = sprint_res_sub.sprint_rag
                cur_sprint_id = sprint_res_sub.id

            project_array.append({'name': row_sub.project_name, 'id': row_sub.id, 'product_owner': row_sub.product_owner, 'scrum_master': row_sub.scrum_master, 'last_rag': cur_sprint_rag, 'last_sprint': cur_sprint_number, 'last_end_date': cur_sprint_end_date, 'last_sprint_id': cur_sprint_id, 'project_description': row_sub.project_description})
        res2.append({'name': row.programme_name, 'id': row.id, 'programme_manager': row.programme_manager, 'service_manager': row.service_manager, 'projects': project_array})
    return Response(json.dumps(res2),  mimetype='application/json')

@app.route('/get/programme/<programme_id>')
def get_programme(programme_id):
    res = programmes.query.filter(programmes.id == programme_id).order_by(programmes.programme_name).all()
    for row in res:
        res_sub = projects.query.filter(projects.programme_id == row.id).order_by(projects.project_name).all()
        project_array = []
        for row_sub in res_sub:

            sprint_res_sub = sprints.query.filter(sprints.project_id == row_sub.id).order_by(sprints.sprint_number.desc()).first()

            cur_sprint_number = ''
            cur_sprint_end_date = ''
            cur_sprint_rag = ''
            cur_sprint_id = ''
            if sprint_res_sub:
                cur_sprint_number = sprint_res_sub.sprint_number
                cur_sprint_end_date = sprint_res_sub.end_date
                cur_sprint_rag = sprint_res_sub.sprint_rag
                cur_sprint_id = sprint_res_sub.id

            project_array.append({'name': row_sub.project_name, 'id': row_sub.id, 'product_owner': row_sub.product_owner, 'scrum_master': row_sub.scrum_master, 'last_rag': cur_sprint_rag, 'last_sprint': cur_sprint_number, 'last_end_date': cur_sprint_end_date, 'last_sprint_id': cur_sprint_id, 'project_description': row_sub.project_description})
        res2 = {'name': row.programme_name, 'id': row.id, 'programme_manager': row.programme_manager, 'service_manager': row.service_manager, 'projects': project_array}
    return Response(json.dumps(res2),  mimetype='application/json')


@app.route('/update/programme/<programme_id>', methods=['POST'])
def update_programme(programme_id):
    programme_request = request.get_json(force=True)
    res = programmes.query.filter(programmes.id == programme_id).order_by(programmes.programme_name).all()
    if (len(res) == 1):
        res[0].programme_name = programme_request['programme_name']
        res[0].programme_manager = programme_request['programme_manager']
        res[0].service_manager = programme_request['service_manager']
        db.session.commit()
        return Response(json.dumps({'status': 'updated'}),  mimetype='application/json')
    return Response(json.dumps({'status': 'not updated'}),  mimetype='application/json')

### Project ###

@app.route('/add/project', methods=['POST'])
def add_project():
    project_request = request.get_json(force=True)
    db.session.add(projects(project_request['programme_id'], project_request['project_name'], project_request['product_owner'], project_request['scrum_master'], project_request['project_description']))
    db.session.commit()
    return Response(json.dumps({'status': 'ok'}),  mimetype='application/json')

@app.route('/get/project/<project_id>')
def get_projects(project_id):
    res = projects.query.filter(projects.id == project_id).order_by(projects.project_name).all()

    res2 = {}
    for row in res:

        sprint_res_sub = sprints.query.filter(sprints.project_id == row.id).order_by(sprints.sprint_number.desc()).first()

        cur_sprint_number = ''
        cur_sprint_end_date = ''
        cur_sprint_rag = ''
        cur_sprint_id = ''
        if sprint_res_sub:
            cur_sprint_number = sprint_res_sub.sprint_number
            cur_sprint_end_date = sprint_res_sub.end_date
            cur_sprint_rag = sprint_res_sub.sprint_rag
            cur_sprint_id = sprint_res_sub.id


        res_programme = programmes.query.filter(programmes.id == str(row.programme_id)).order_by(programmes.programme_name).all()

        res_sub = sprints.query.filter(sprints.project_id == row.id).order_by(sprints.sprint_number).all()
        sprint_array = []
        for row_sub in res_sub:


            sprint_array.append({'id': row_sub.id, 'project_id': row_sub.project_id, 'start_date': row_sub.start_date, 'end_date': row_sub.end_date, 'sprint_number': row_sub.sprint_number, 'sprint_rag': row_sub.sprint_rag, 'sprint_goal': row_sub.sprint_goal, 'sprint_deliverables': row_sub.sprint_deliverables, 'sprint_challenges': row_sub.sprint_challenges, 'delivered_points': row_sub.delivered_points, 'started_points': row_sub.started_points, 'agreed_points': row_sub.agreed_points, 'sprint_issues': row_sub.sprint_issues, 'sprint_risks': row_sub.sprint_risks, 'sprint_dependencies': row_sub.sprint_dependencies, 'sprint_days': row_sub.sprint_days })
        res2 = {'name': row.project_name, 'programme_id': row.programme_id, 'id': row.id, 'product_owner': row.product_owner, 'scrum_master': row.scrum_master, 'sprint_array': sprint_array, 'project_description': row.project_description, 'programme_name': res_programme[0].programme_name, 'programme_manager': res_programme[0].programme_manager, 'service_manager': res_programme[0].service_manager, 'last_rag': cur_sprint_rag, 'last_sprint': cur_sprint_number, 'last_end_date': cur_sprint_end_date, 'last_sprint_id': cur_sprint_id}
    return Response(json.dumps(res2),  mimetype='application/json')


@app.route('/update/project/<project_id>', methods=['POST'])
def update_project(project_id):
    project_request = request.get_json(force=True)
    res = projects.query.filter(projects.id == project_id).order_by(projects.project_name).all()
    if (len(res) == 1):
        res[0].programme_id = project_request['programme_id']
        res[0].project_name = project_request['project_name']
        res[0].product_owner = project_request['product_owner']
        res[0].scrum_master = project_request['scrum_master']
        res[0].project_description = project_request['project_description']
        db.session.commit()
        return Response(json.dumps({'status': 'updated'}),  mimetype='application/json')
    return Response(json.dumps({'status': 'not updated'}),  mimetype='application/json')

### Sprints ###

@app.route('/add/sprint', methods=['POST'])
def add_sprint():
    sprint_request = request.get_json(force=True)
    sprint_row = sprints(sprint_request['project_id'], sprint_request['start_date'], sprint_request['end_date'], sprint_request['sprint_number'], sprint_request['sprint_rag'], sprint_request['sprint_goal'], sprint_request['sprint_deliverables'], sprint_request['sprint_challenges'], sprint_request['agreed_points'], sprint_request['delivered_points'], sprint_request['started_points'], sprint_request['sprint_issues'], sprint_request['sprint_risks'], sprint_request['sprint_dependencies'], sprint_request['sprint_days'])
    db.session.add(sprint_row)
    db.session.commit()
    return Response(json.dumps({'status': 'ok', 'id': sprint_row.id}),  mimetype='application/json')


@app.route('/update/sprint/<sprint_id>', methods=['POST'])
def update_sprint(sprint_id):
    sprint_request = request.get_json(force=True)
    res = sprints.query.filter(sprints.id == sprint_id).order_by(sprints.start_date).all()
    if (len(res) == 1):
        res[0].project_id = sprint_request['project_id']
        res[0].start_date = sprint_request['start_date']
        res[0].end_date = sprint_request['end_date']
        res[0].sprint_number = sprint_request['sprint_number']
        res[0].sprint_rag = sprint_request['sprint_rag']
        res[0].sprint_goal = sprint_request['sprint_goal']
        res[0].sprint_deliverables = sprint_request['sprint_deliverables']
        res[0].sprint_challenges = sprint_request['sprint_challenges']
        res[0].delivered_points = sprint_request['delivered_points']
        res[0].started_points = sprint_request['started_points']
        res[0].agreed_points = sprint_request['agreed_points']
        res[0].sprint_issues = sprint_request['sprint_issues']
        res[0].sprint_risks = sprint_request['sprint_risks']
        res[0].sprint_dependencies = sprint_request['sprint_dependencies']
        res[0].sprint_days = sprint_request['sprint_days']
        db.session.commit()
        return Response(json.dumps({'status': 'updated'}),  mimetype='application/json')
    return Response(json.dumps({'status': 'not updated'}),  mimetype='application/json')


@app.route('/get/project/<project_id>/<sprint_id>')
def get_projectsprint(project_id,sprint_id):
    res = projects.query.filter(projects.id == project_id).order_by(projects.project_name).all()
    if (len(res) == 1):
        res_sub = sprints.query.filter(sprints.id == sprint_id and sprint.project_id == project_id).order_by(sprints.sprint_number).all()
        if (len(res_sub) == 1):
            res_sub2 = burndown.query.filter(burndown.sprint_id == sprint_id).order_by(burndown.sprint_day).all()
            burndown_array = []
            for row_sub2 in res_sub2:
                burndown_array.append({'sprint_day': row_sub2.sprint_day, 'sprint_done': row_sub2.sprint_done})
            res2 = {'name': res[0].project_name, 'programme_id': res[0].programme_id, 'project_id': res[0].id, 'product_owner': res[0].product_owner, 'scrum_master': res[0].scrum_master, 'sprint_id': res_sub[0].id, 'start_date': res_sub[0].start_date, 'end_date': res_sub[0].end_date, 'sprint_number': res_sub[0].sprint_number, 'sprint_rag': res_sub[0].sprint_rag, 'sprint_goal': res_sub[0].sprint_goal, 'sprint_deliverables': res_sub[0].sprint_deliverables, 'sprint_challenges': res_sub[0].sprint_challenges, 'delivered_points': res_sub[0].delivered_points, 'started_points': res_sub[0].started_points, 'agreed_points': res_sub[0].agreed_points, 'sprint_issues': res_sub[0].sprint_issues, 'sprint_risks': res_sub[0].sprint_risks, 'sprint_dependencies': res_sub[0].sprint_dependencies, 'sprint_days': res_sub[0].sprint_days, 'burndown': burndown_array, 'project_description': res[0].project_description}
            return Response(json.dumps(res2),  mimetype='application/json')
        return Response(json.dumps({'status': 'Sprint not found'}),  mimetype='application/json')
    return Response(json.dumps({'status': 'Project not found'}),  mimetype='application/json')


@app.route('/update/burn_down', methods=['POST'])
def update_burndown():
    burndown_request = request.get_json(force=True)
    db.session.query(burndown).filter(burndown.sprint_id == burndown_request['sprint_id']).delete()
    #db.session.commit()

    for row in burndown_request['sprint_days']:
        db.session.add(burndown(burndown_request['sprint_id'], row['sprint_day'], row['sprint_done']))
    db.session.commit()

    return Response(json.dumps({'status': 'ok'}),  mimetype='application/json')


@app.route('/delete/programme/<programme_id>', methods=['GET'])
def delete_programme(programme_id):
    db.session.query(programmes).filter(programmes.id == programme_id).delete()
    db.session.commit()
    return Response(json.dumps({'status': 'ok'}),  mimetype='application/json')

@app.route('/delete/project/<project_id>', methods=['GET'])
def delete_project(project_id):
    db.session.query(projects).filter(projects.id == project_id).delete()
    db.session.commit()
    return Response(json.dumps({'status': 'ok'}),  mimetype='application/json')

@app.route('/delete/sprint/<sprint_id>', methods=['GET'])
def delete_sprint(sprint_id):
    db.session.query(sprints).filter(sprints.id == sprint_id).delete()
    db.session.commit()
    return Response(json.dumps({'status': 'ok'}),  mimetype='application/json')
