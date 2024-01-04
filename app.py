from flask import Flask, render_template, request, redirect,session, url_for
from flask_mysqldb import MySQL
import yaml
from yaml import FullLoader

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'),Loader=FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)
app.secret_key = 'your_secret_key_here'

name=""
@app.route('/homepage')
def home():
    return render_template('Package.html')

@app.route('/flights')
def flights():
    return render_template('Flight.html')

@app.route('/hotels')
def hotels():
    return render_template('Hotel.html')

@app.route('/holiday')
def holiday():
    return render_template('HolidayPackage.html')

@app.route('/trains')
def trains():
    return render_template('Train.html')

@app.route('/activity')
def activity():
    return render_template('Activities.html')

@app.route('/chennai_flights')
def chennai_flights():
    return render_template('chennai_flights.html')

@app.route('/goa_flights')
def goa_flights():
    return render_template('goa_flights.html')

@app.route('/hydrebad_flights')
def hydrebad_flights():
    return render_template('hydrebad_flights.html')

@app.route('/delhi_flights')
def delhi_flights():
    return render_template('delhi_flights.html')

@app.route('/pune_flights')
def pune_flights():
    return render_template('pune_flights.html')

@app.route('/kolkata_flights')
def kolkata_flights():
    return render_template('kolkata_flights.html')

@app.route('/bangalore_flights')
def bangalore_flights():
    return render_template('bangalore_flights.html')

@app.route('/jaipur_flights')
def jaipur_flights():
    return render_template('jaipur_flights.html')

@app.route('/mumbai_flights')
def mumbai_flights():
    return render_template('mumbai_flights.html')

@app.route('/goa_hotels')
def goa_hotels():
    return render_template('goa_hotels.html')

@app.route('/delhi_hotels')
def delhi_hotels():
    return render_template('delhi_hotels.html')

@app.route('/bangalore_hotels')
def bangalore_hotels():
    return render_template('bangalore_hotels.html')

@app.route('/ooty_hotels')
def ooty_hotels():
    return render_template('ooty_hotels.html')

@app.route('/mumbai_hotels')
def mumbai_hotels():
    return render_template('mumbai_hotels.html')

@app.route('/shimla_hotels')
def shimla_hotels():
    return render_template('shimla_hotels.html')

@app.route('/jaipur_hotels')
def jaipur_hotels():
    return render_template('jaipur_hotels.html')

@app.route('/manali_hotels')
def manali_hotels():
    return render_template('manali_hotels.html')

@app.route('/chennai_hotels')
def chennai_hotels():
    return render_template('chennai_hotels.html')

@app.route('/bangalore_trains')
def bangalore_trains():
    return render_template('bangalore_trains.html')

@app.route('/goa_trains')
def goa_trains():
    return render_template('goa_trains.html')

@app.route('/hydrebad_trains')
def hydrebad_trains():
    return render_template('hydrebad_trains.html')

@app.route('/kolkata_trains')
def kolkata_trains():
    return render_template('kolkata_trains.html')

@app.route('/delhi_trains')
def delhi_trains():
    return render_template('delhi_trains.html')

@app.route('/pune_trains')
def pune_trains():
    return render_template('pune_trains.html')

@app.route('/mumbai_trains')
def mumbai_trains():
    return render_template('mumbai_trains.html')

@app.route('/chennai_trains')
def chennai_trains():
    return render_template('chennai_trains.html')

@app.route('/jaipur_trains')
def jaipur_trains():
    return render_template('jaipur_trains.html')


@app.route('/adventure_activity')
def adventure_activity():
    return render_template('adventure_activity.html')

@app.route('/monument_activity')
def monument_activity():
    return render_template('monument_activity.html')

@app.route('/cruise_activity')
def cruise_activity():
    return render_template('cruise_activity.html')

@app.route('/water_activity')
def water_activity():
    return render_template('water_activity.html')

@app.route('/shopping_activity')
def shopping_activity():
    return render_template('shopping_activity.html')

@app.route('/concert_activity')
def concert_activity():
    return render_template('concert_activity.html')

@app.route('/park_activity')
def park_activity():
    return render_template('park_activity.html')

@app.route('/air_activity')
def air_activity():
    return render_template('air_activity.html')

@app.route('/flight_booking')
def flight_booking():
    return render_template('flightbooking.html')


@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name1']
        email = userDetails['email1']
        password = userDetails['password1']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login(name, email, password) VALUES(%s, %s, %s)",(name, email, password))
        mysql.connection.commit()
        cur.close()
        # return redirect('lo')
    return render_template('loginpage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': #and 'email' in request.form and 'password' in request.form:
        # Fetch form data
        userDetails = request.form
        email = userDetails['email1']
        password = userDetails['password1']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM login WHERE email = %s AND password = %s", (email, password))
        if result > 0:
            user = cur.fetchone()
            session['loggedin'] = True
            session['id'] = user[0]
            session['name'] = user[1]
            session['email'] = user[2]
            global name 
            name = cur.execute("SELECT name FROM login WHERE email = %s AND password = %s",(email,password))
            name = cur.fetchone()
            return redirect('/homepage')
        else:
            return render_template('loginpage.html')
        
        mysql.connection.commit()
        cur.close()

    return render_template('loginpage.html')

@app.route('/book/<f>/<t>/<p>/<h>/<a>', methods=['GET', 'POST'])
def book(f,t,p,h,a):
    return render_template('flightbooking.html',f=f,t=t,p=p,h=h,a=a)

@app.route('/tbook/<f>/<t>/<p>/<h>', methods=['GET', 'POST'])
def tbook(f,t,p,h):
    return render_template('trainbooking.html',f=f,t=t,p=p,h=h)

@app.route('/hbook/<pl>/<p>', methods=['GET', 'POST'])
def hbook(pl,p):
    return render_template('hotelbooking.html',pl=pl,p=p)

@app.route('/abook/<a>/<h>/<p>', methods=['GET', 'POST'])
def abook(a,h,p):
    return render_template('activitybooking.html',a=a,h=h,p=p)

@app.route('/hpbook/<hp>/<pl>/<nd>/<p>', methods=['GET', 'POST'])
def hpbook(hp,pl,nd,p):
    return render_template('holidaypackagebooking.html',hp=hp,pl=pl,nd=nd,p=p)

@app.route('/payment/<a>/<f>/<t>/<nop>/<cls>/<dat>/<tot>', methods=['GET','POST'])
def payment(a,f,t,nop,cls,dat,tot):
    global name
    naam = name[0]
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO flight(Name,Flight,Departure,Destination,Number,Class,Date,Amount) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(naam, a, f, t, nop, cls, dat, tot))
        mysql.connection.commit()
        cur.close()
        return redirect('/thankyou')
    
    return render_template('confirmbooking.html',a=a,f=f,t=t,nop=nop,cls=cls,dat=dat,tot=tot)

@app.route('/tpayment/<f>/<t>/<nop>/<cls>/<dat>/<tot>', methods=['GET','POST'])
def tpayment(f,t,nop,cls,dat,tot):
    global name
    naam = name[0]
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO train(Name,Departure,Destination,Number,Class,Date,Amount) VALUES(%s, %s, %s, %s, %s, %s, %s)",(naam, f, t, nop, cls, dat, tot))
        mysql.connection.commit()
        cur.close()
        return redirect('/thankyou')
    
    return render_template('confirmbooking.html',f=f,t=t,nop=nop,cls=cls,dat=dat,tot=tot)

@app.route('/hpayment/<pl>/<p>/<nop>/<cls>/<dat>/<tot>', methods=['GET','POST'])
def hpayment(pl,p,nop,cls,dat,tot):
    global name
    naam = name[0]
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO hotel(Name,Hotel,Nights,Room,Date,Amount) VALUES(%s, %s, %s, %s, %s, %s)",(naam, pl, nop, cls, dat, tot))
        mysql.connection.commit()
        cur.close()
        return redirect('/thankyou')
    
    return render_template('confirmbooking.html',pl=pl,p=p,nop=nop,cls=cls,dat=dat,tot=tot)

@app.route('/apayment/<a>/<h>/<nop>/<cls>/<dat>/<tot>', methods=['GET', 'POST'])
def apayment(a, h, nop, cls, dat, tot):
    global name
    naam = name[0]
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO activity(Name, Activity, Hours, Person, Time, Date, Amount) VALUES(%s, %s, %s, %s, %s, %s, %s)", (naam, a, h, nop, cls, dat, tot))
        mysql.connection.commit()
        cur.close()
        return redirect('/thankyou')
    
    return render_template('confirmbooking.html', a=a, h=h, nop=nop, cls=cls, dat=dat, tot=tot)

@app.route('/hppayment/<hp>/<pl>/<nd>/<nop>/<cls>/<dat>/<tot>', methods=['GET', 'POST'])
def hppayment(hp, pl, nd, nop, cls, dat, tot):
    global name
    naam = name[0]
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO holidaypackage(Name, Package, Place, Days, Person, Cuisine, Date, Amount) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (naam, hp, pl, nd, nop, cls, dat, tot))
        mysql.connection.commit()
        cur.close()
        return redirect('/thankyou')
    
    return render_template('confirmbooking.html', hp=hp, pl=pl, nd=nd, nop=nop, cls=cls, dat=dat, tot=tot)

@app.route('/thankyou')
def thankyou():
    return render_template('thank_you.html',name=name)

# @app.route('/users')
# def users():
#     cur = mysql.connection.cursor()
#     resultValue = cur.execute("SELECT * FROM login")
#     if resultValue > 0:
#         userDetails = cur.fetchall()
#         return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)