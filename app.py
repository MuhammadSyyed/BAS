from flask import Flask
import time
from datetime import datetime
from flask import Flask, render_template, request
from database_func import check_arrival, mark_attendance, mark_departure, get_student_data_by_id,get_presents,get_absents

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET', 'POST'])
def main():
    date = request.form.get('date')
    if date:
        day=datetime.strptime(date,"%Y-%m-%d").strftime("%A")
        repre_date = datetime.strptime(date, "%Y-%m-%d").strftime("%B %d, %Y")
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%m/%d/%Y")
    else:
        day=datetime.now().strftime("%A")
        repre_date = datetime.now().strftime("%B %d, %Y")
        date = datetime.now().strftime("%m/%d/%Y")
    
    columns = ['ROLL NO.','STUDENT','DATE','REPORTING TIME','DEPARTURE TIME','STATUS']
    presents = get_presents(date=date)
    absents = get_absents(presents)
    return render_template('index.html', columns=columns,date=date,presents=presents,absents=absents,count_present=len(presents),count_absents=len(absents),day=day,date_time=repre_date)

@app.route('/mark/<id>')
def mark(id):
    try:
        id = int(id)
        roll_no, name = get_student_data_by_id(id)
        date = datetime.now().strftime("%m/%d/%Y")
        present = check_arrival(roll_no, date)
        if present:
            if present["DEPARTURE_TIME"] == "":
                mark_departure(roll_no, date, time.strftime("%I:%M %p"))
                return {"id": id, "departure-marked": True}
            else:
                return {"id": id, "departure-marked": "already"}
        else:
            mark_attendance(roll_no, name, date, time.strftime("%I:%M %p"))
            return {"id": id, "arrival-marked": True}
    except:
        return {"error": "invalid id"}
