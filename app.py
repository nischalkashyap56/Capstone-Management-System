from flask import Flask, request, render_template, redirect, url_for, flash, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "b'\xefn\xc58\xbd-U\xe7\x92\xa8i\xe0\x88Q\x85y@'\xb9\xa9op$\xac\x8a\x90\tQ&\x05\xdb\x16"

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="capstone"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Main Page
@app.route('/', methods=['GET'])
def mainpage():
    return render_template('mainpage.html')

# Team Signup Page
@app.route('/team_signup', methods=['GET', 'POST'])
def team_signup():
    if request.method == 'POST':
        cursor = db.cursor()

        # Insert data for Student 1
        student1_srn = request.form.get('student1_srn')
        student1_cgpa = request.form.get('student1_cgpa')
        student1_first_name = request.form.get('student1_first_name')
        student1_last_name = request.form.get('student1_last_name')
        student1_department = request.form.get('student1_department')
        student1_email = request.form.get('student1_email')
        student1_phone = request.form.get('student1_phone')

        cursor.execute("INSERT INTO student (srn, cgpa, first_name, last_name, department, stud_email, stud_phone) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (student1_srn, student1_cgpa, student1_first_name, student1_last_name, student1_department, student1_email, student1_phone))

        # Insert data for Student 2
        student2_srn = request.form.get('student2_srn')
        student2_cgpa = request.form.get('student2_cgpa')
        student2_first_name = request.form.get('student2_first_name')
        student2_last_name = request.form.get('student2_last_name')
        student2_department = request.form.get('student2_department')
        student2_email = request.form.get('student2_email')
        student2_phone = request.form.get('student2_phone')

        cursor.execute("INSERT INTO student (srn, cgpa, first_name, last_name, department, stud_email, stud_phone) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (student2_srn, student2_cgpa, student2_first_name, student2_last_name, student2_department, student2_email, student2_phone))

        # Insert data for Student 3
        student3_srn = request.form.get('student3_srn')
        student3_cgpa = request.form.get('student3_cgpa')
        student3_first_name = request.form.get('student3_first_name')
        student3_last_name = request.form.get('student3_last_name')
        student3_department = request.form.get('student3_department')
        student3_email = request.form.get('student3_email')
        student3_phone = request.form.get('student3_phone')

        cursor.execute("INSERT INTO student (srn, cgpa, first_name, last_name, department, stud_email, stud_phone) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (student3_srn, student3_cgpa, student3_first_name, student3_last_name, student3_department, student3_email, student3_phone))

        # Insert data for Student 4
        student4_srn = request.form.get('student4_srn')
        student4_cgpa = request.form.get('student4_cgpa')
        student4_first_name = request.form.get('student4_first_name')
        student4_last_name = request.form.get('student4_last_name')
        student4_department = request.form.get('student4_department')
        student4_email = request.form.get('student4_email')
        student4_phone = request.form.get('student4_phone')
        cursor.execute("INSERT INTO student (srn, cgpa, first_name, last_name, department, stud_email, stud_phone) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (student4_srn, student4_cgpa, student4_first_name, student4_last_name, student4_department, student4_email, student4_phone))
        
        team_id = student1_srn + '_' + student2_srn + '_' + student3_srn + '_' + student4_srn
        project_domain = request.form.get('project_domain')
        faculty_srn = request.form.get('faculty_srn')
        problem_statement = request.form.get('problem_statement')
        team_password = request.form.get('team_password')
        cursor.execute("INSERT INTO team (faculty_srn, team_id, project_domain, problem_statement, team_password) VALUES (%s, %s, %s, %s, %s)",
                       (faculty_srn, team_id, project_domain, problem_statement, team_password))

        db.commit()
        cursor.close()
        string_return = "Team successfully signed \n\n Your team ID is :" + team_id
        return string_return
    return render_template('team_signup.html')

# Team Login Page
@app.route('/team_login', methods=['GET', 'POST'])
def team_login():
    if request.method == 'POST':
        team_id = request.form.get('team_id')
        team_password = request.form.get('team_password')

        cursor = db.cursor()
        cursor.execute("SELECT * FROM team WHERE team_id = %s AND team_password = %s", (team_id, team_password))
        team = cursor.fetchone()
        cursor.close()

        if team:
            # Team login successful, you can redirect to a dashboard or perform other actions
            return "Team login successful!"
        else:
            # Team login failed, you can redirect to the login page with an error message
            return "Invalid team ID or password. Please try again."
    return render_template('team_login.html')

# Faculty Signup Page
@app.route('/faculty_signup', methods=['GET', 'POST'])
def faculty_signup():
    if request.method == 'POST':
        faculty_srn = request.form.get('faculty_srn')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        designation = request.form.get('designation')
        faculty_department = request.form.get('faculty_department')
        faculty_domain = request.form.get('faculty_domain')
        faculty_phone_no = request.form.get('faculty_phone_no')
        faculty_email = request.form.get('faculty_email')
        faculty_password = request.form.get('faculty_password')

        cursor = db.cursor()

        # Insert data into the faculty table
        cursor.execute("INSERT INTO faculty (faculty_srn, first_name, last_name, designation, faculty_department, faculty_domain, faculty_phone_no, faculty_email, faculty_password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (faculty_srn, first_name, last_name, designation, faculty_department, faculty_domain, faculty_phone_no, faculty_email, faculty_password))

        db.commit()
        cursor.close()

        return "Faculty signup successful!"
    return render_template('faculty_signup.html')

# Faculty Login Page
@app.route('/faculty_login', methods=['GET', 'POST'])
def faculty_login():
    if request.method == 'POST':
        session['faculty_srn'] = request.form['faculty_srn']
        faculty_srn = request.form.get('faculty_srn')
        faculty_password = request.form.get('faculty_password')

        cursor = db.cursor()
        cursor.execute("SELECT * FROM faculty WHERE faculty_srn = %s AND faculty_password = %s", (faculty_srn, faculty_password))
        faculty = cursor.fetchone()
        cursor.close()

        if faculty:
            # Faculty login successful, you can redirect to a dashboard or perform other actions
            return render_template('faculty_home.html')
        else:
            # Faculty login failed, you can redirect to the login page with an error message
            return "Invalid SRN or password. Please try again."
    return render_template('faculty_login.html')

@app.route('/faculty_home')
def faculty_home():
    return render_template('faculty_home.html')

@app.route('/faculty_results', methods=['GET', 'POST'])
def faculty_results():
    if request.method == 'POST':
        cursor = db.cursor()

        # Retrieve data from the form
        student_srn = request.form.get('student_srn')
        semester = request.form.get('semester')
        isa1_marks = request.form.get('isa1_marks')
        isa2_marks = request.form.get('isa2_marks')
        esa_marks = request.form.get('esa_marks')

        # Insert results into the review table
        insert_query = "INSERT INTO review (student_srn, semester, isa1_marks, isa2_marks, esa_marks) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (student_srn, semester, isa1_marks, isa2_marks, esa_marks))
        db.commit()

        cursor.close()
        return "Results added successfully!"
    return render_template('faculty_results.html')

@app.route("/faculty_delete", methods=["GET", "POST"])
def faculty_delete():
    if request.method == "POST":
        faculty_srn = request.form["faculty_srn"]

        try:
            # Check if faculty member is associated with existing teams
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) FROM team WHERE faculty_srn = %s", (faculty_srn,))
            team_count = cursor.fetchone()[0]
            cursor.close()

            if team_count == 0:
                cursor = db.cursor()
                cursor.execute("DELETE FROM faculty WHERE faculty_srn = %s", (faculty_srn,))
                db.commit()
                cursor.close()

                # Use flash() to store the message
                flash("Faculty member successfully deleted.")
            else:
                flash("Cannot delete faculty member associated with existing teams.")

        except mysql.connector.errors.IntegrityError:
            flash("Faculty member cannot be deleted due to integrity constraints.")

        return redirect("/faculty_delete")

    return render_template("faculty_delete.html")

@app.route('/faculty_view')
def faculty_view():
    # Retrieve 'faculty_srn' from the logged in faculty
    faculty_srn = session['faculty_srn']
    # Fetch teams associated with the faculty from the database
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT team_id, project_domain FROM team WHERE faculty_srn = %s", (faculty_srn,))
    faculty_teams = cursor.fetchall()
    cursor.close()
    return render_template('faculty_view.html', faculty_teams=faculty_teams)

@app.route('/student_score', methods = ['GET', 'POST'])
def student_score():
    if request.method == 'GET':
        cursor = db.cursor()
        student_srn = 'PES1UG21CS123'
        # student_srn = request.form.get('student_srn')
        print(student_srn)
        query = """
        SELECT AVG(review.isa1_marks + review.isa2_marks + review.esa_marks) / 3 AS avg_score
        FROM review
        INNER JOIN student ON student.srn = review.student_srn
        WHERE student.srn = %s
        """
        x = cursor.execute(query, (student_srn,))
        avg_score = cursor.fetchone()[0]
        session['student_srn'] = student_srn
        session['avg_score'] = avg_score
        cursor.close()
        db.close()
        print(student_srn, '.....', x, '/////', avg_score)
    return render_template('student_score.html', student_srn=student_srn, avg_score=avg_score)

@app.route('/student_avg_score', methods=['GET', 'POST'])
def student_avg_score():
    student_srn = session.get('student_srn')
    avg_score = session.get('avg_score')
    return render_template('student_avg_score.html', student_srn=student_srn, avg_score=avg_score)

if __name__ == '__main__':
    app.run(debug=True)






