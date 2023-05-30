from flask import Flask,render_template,request
import json_utilies
import register
import update

app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def flask():
    if request.method=="POST":
        print(request.form["books"],request.form["courses"])
        register.register(request.form["books"],request.form["courses"])
    data=json_utilies.student("data/student.json")
    return render_template("main.html",course1=data["students"])

    
if __name__=="__main__":
    app.run(debug=True)
    
    