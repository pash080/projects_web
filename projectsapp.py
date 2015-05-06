from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setupDB import Base, Project, Category, Entry

engine = create_engine('sqlite:///projects.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/projects/')
def projects():
	projects = session.query(Project).all()
	print(projects)
	return render_template('projectsShow.html', projects = projects )

@app.route('/projects/new/', methods = ['POST', 'GET'])
def projects_new():
	if request.method == 'GET':
		return render_template('projectsNew.html')

	if request.method == 'POST':
		return redirect(url_for("projects"))
	

@app.route('/projects/edit/<int:project_id>/', methods = ['POST', 'GET'])
def projects_edit(project_id):
	if request.method == 'GET':
		return render_template('projectsEdit.html',  project_id = project_id)

	if request.method == 'POST':
		return redirect(url_for("projects",))

@app.route('/projects/delete/<int:project_id>/', methods = ['POST', 'GET'])
def projects_delete(project_id):
	if request.method == 'GET':
		return render_template('projectsDelete.html',  project_id = project_id)

	if request.method == 'POST':
		return redirect(url_for("projects",))



if __name__ == '__main__':
    app.secret_key = "somesecretkey"
    app.debug = True
    app.run(host = '0.0.0.0', port = 50000)

