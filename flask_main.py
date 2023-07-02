from flask import Flask,render_template,request, redirect
import json_utilies
import register
import update
import delete

app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def flask():
    if request.method=="POST":
        print(request.form["books"],request.form["courses"])
        register.register(request.form["books"],request.form["courses"])
    data=json_utilies.student("data/student.json")
    return render_template("main.html",course1=data["students"])

@app.route("/update/<int:id>",methods=["POST","GET"])
def update_stud(id):
    if request.method=="GET":
        data=json_utilies.student("data/student.json")
        stud_data={}
        for stud in data['students']:
            if stud["sno"]==int(id):
                stud_data=stud
        print(stud_data)
        return render_template("update.html",stud_data=stud_data)
    elif request.method=="POST":
        user_name=request.form["stud_name"]
        course=request.form["stud_course"]
        status=request.form["stud_status"]
        data=json_utilies.student("data/student.json")
        for stud in data['students']:
            if stud["sno"]==int(id):
                stud["student_name"]=user_name
                stud["student_course"]=course
                stud["student_status"]=status
        json_utilies.write("data/student.json",data)
        return redirect("/")

@app.route("/delete/<int:id>",methods=["POST","GET"])
def delete_stud(id):
    if request.method=="GET":
        delete.delete(int(id))
    return redirect('/')

    
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
    
    
