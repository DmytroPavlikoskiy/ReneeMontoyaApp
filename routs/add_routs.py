from flask import Flask, redirect, url_for, render_template, request
from app import app, api, db
from framework.models import Employees


@app.route("/Home", methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/EmployeePost", methods=['GET', 'POST'])
def empost():
    employee = Employees.query.all()
    return render_template('emGET.html', employee=employee)


@app.route("/Employees", methods=['GET', 'POST'])
def add_employees():
    if request.method == 'POST':
        employee = Employees(name=request.form['name'],
                             email=request.form['email'],
                             department_type=request.form['department_type'],
                             department_id=request.form['department_id'])
        db.session.add(employee)
        db.session.commit()
        return redirect("/EmployeePost")
    else:
        print("Warning: Failed to add Employee")
    return render_template('emPost.html')


@app.route("/Employees/<int:id>/update", methods=['POST', 'GET'])
def update(id):
    employee = Employees.query.get(id)
    if request.method == 'POST':
        employee.name = request.form['name'],
        employee.email = request.form['email'],
        employee.department_type = request.form['department_type'],
        employee.department_id = request.form['department_id']
        try:
            db.session.commit()
            return redirect('/EmployeePost')
        except:
            return "Warning!: There is no worker you want to update"
    else:
        return render_template('update.html', employee=employee)


@app.route("/EmployeePost/<int:id>/delete", methods=['POST', 'GET'])
def delete(id):
    employee = Employees.query.get_or_404(id)
    try:
        db.session.delete(employee)
        db.session.commit()
        return redirect("/EmployeePost")
    except:
        return "Warning!: There is no worker you want to delete"


@app.route("/EmployeePost/<int:id>/<name>/selected", methods=['GET', 'POST'])
def selected(id, name):
    employee = Employees.query.get(id)
    return render_template("selected.html", employee=employee, name=name)

