from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
import json
import os
from functools import wraps
import jinja2
from datetime import datetime

app = Flask(__name__, static_folder='public', static_url_path='/static')
app.secret_key = 'your-secret-key-here'
app.url_map.strict_slashes = False  # Add this line to handle trailing slashes

JSON_FILE = './database/auth.json'

# INVESTMENT JSON FILES
JSON_FILE = './database/investment.json'

# REY JSON FILES
JSON_FILE = './database/rey.json'
JSON_FILE = './database/reyIncome.json'
JSON_FILE = './database/reyOutcome.json'

# DANIA JSON FILES
JSON_FILE = './database/dania.json'
JSON_FILE = './database/daniaIncome.json'
JSON_FILE = './database/daniaOutcome.json'


# Public funtion
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def load_users():
    with open('./database/auth.json', 'r') as f:
        return json.load(f)['data']
    
def load_investments():
    with open('./database/investment.json', 'r') as f:
        return json.load(f)
    
def load_rey():
    with open('./database/rey.json', 'r') as f:
        return json.load(f)["data"]
    
def load_rey_income():
    with open('./database/reyIncome.json', 'r') as f:
        return json.load(f)["data"]
    
def load_rey_outcome():
    with open('./database/reyOutcome.json', 'r') as f:
        return json.load(f)["data"]
    
def load_dania():
    with open('./database/dania.json', 'r') as f:
        return json.load(f)["data"]
    
def load_dania_income():
    with open('./database/daniaIncome.json', 'r') as f:
        return json.load(f)["data"]
    
def load_dania_outcome():
    with open('./database/daniaOutcome.json', 'r') as f:
        return json.load(f)["data"]

def current_user():
    return {
        'username': session['username'],
    }

# Routes Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = load_users()
        user = next((user for user in users if user['username'] == username and user['password'] == password), None)
        
        if user:
            session['logged_in'] = True
            session['user_id'] = user['id_petugas']
            session['username'] = user['username']
            return redirect(url_for('home'))
        else:
            return render_template('auth/index.html', error='Invalid username or password')
            
    return render_template('auth/index.html')

# Routes Home
@app.route('/home')
@login_required
def home():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    investment = load_investments()
    
    # Get the highest investment amount for January
    max_january_investment = max(investment['Januari'], key=lambda x: x['jumlah_investasi'])
    max_january_return = max(investment['Januari'], key=lambda x: x['return'])
    january_investment_result = {
        'amount': float(max_january_investment['jumlah_investasi']),
        'return': float(max_january_return['return']),
        'total': float(max_january_investment['jumlah_investasi']) + float(max_january_return['return'])
    }
    
    max_february_investment = max(investment['Febuari'], key=lambda x: x['jumlah_investasi'])
    max_february_return = max(investment['Febuari'], key=lambda x: x['return'])
    february_investment_result = {
        'amount': float(max_february_investment['jumlah_investasi']),
        'return': float(max_february_return['return']),
        'total': float(max_february_investment['jumlah_investasi']) + float(max_february_return['return'])
    }

    # March
    max_march_investment = max(investment['Maret'], key=lambda x: x['jumlah_investasi'])
    max_march_return = max(investment['Maret'], key=lambda x: x['return'])
    march_investment_result = {
        'amount': float(max_march_investment['jumlah_investasi']),
        'return': float(max_march_return['return']),
        'total': float(max_march_investment['jumlah_investasi']) + float(max_march_return['return'])
    }

    # April through December follow same pattern
    max_april_investment = max(investment['April'], key=lambda x: x['jumlah_investasi'])
    max_april_return = max(investment['April'], key=lambda x: x['return'])
    april_investment_result = {
        'amount': float(max_april_investment['jumlah_investasi']),
        'return': float(max_april_return['return']),
        'total': float(max_april_investment['jumlah_investasi']) + float(max_april_return['return'])
    }

    max_may_investment = max(investment['Mei'], key=lambda x: x['jumlah_investasi'])
    max_may_return = max(investment['Mei'], key=lambda x: x['return'])
    may_investment_result = {
        'amount': float(max_may_investment['jumlah_investasi']),
        'return': float(max_may_return['return']),
        'total': float(max_may_investment['jumlah_investasi']) + float(max_may_return['return'])
    }

    max_june_investment = max(investment['Juni'], key=lambda x: x['jumlah_investasi'])
    max_june_return = max(investment['Juni'], key=lambda x: x['return'])
    june_investment_result = {
        'amount': float(max_june_investment['jumlah_investasi']),
        'return': float(max_june_return['return']),
        'total': float(max_june_investment['jumlah_investasi']) + float(max_june_return['return'])
    }

    max_july_investment = max(investment['Juli'], key=lambda x: x['jumlah_investasi'])
    max_july_return = max(investment['Juli'], key=lambda x: x['return'])
    july_investment_result = {
        'amount': float(max_july_investment['jumlah_investasi']),
        'return': float(max_july_return['return']),
        'total': float(max_july_investment['jumlah_investasi']) + float(max_july_return['return'])
    }

    max_august_investment = max(investment['Agustus'], key=lambda x: x['jumlah_investasi'])
    max_august_return = max(investment['Agustus'], key=lambda x: x['return'])
    august_investment_result = {
        'amount': float(max_august_investment['jumlah_investasi']),
        'return': float(max_august_return['return']),
        'total': float(max_august_investment['jumlah_investasi']) + float(max_august_return['return'])
    }

    max_september_investment = max(investment['September'], key=lambda x: x['jumlah_investasi'])
    max_september_return = max(investment['September'], key=lambda x: x['return'])
    september_investment_result = {
        'amount': float(max_september_investment['jumlah_investasi']),
        'return': float(max_september_return['return']),
        'total': float(max_september_investment['jumlah_investasi']) + float(max_september_return['return'])
    }

    max_october_investment = max(investment['Oktober'], key=lambda x: x['jumlah_investasi'])
    max_october_return = max(investment['Oktober'], key=lambda x: x['return'])
    october_investment_result = {
        'amount': float(max_october_investment['jumlah_investasi']),
        'return': float(max_october_return['return']),
        'total': float(max_october_investment['jumlah_investasi']) + float(max_october_return['return'])
    }

    max_november_investment = max(investment['November'], key=lambda x: x['jumlah_investasi'])
    max_november_return = max(investment['November'], key=lambda x: x['return'])
    november_investment_result = {
        'amount': float(max_november_investment['jumlah_investasi']),
        'return': float(max_november_return['return']),
        'total': float(max_november_investment['jumlah_investasi']) + float(max_november_return['return'])
    }

    max_december_investment = max(investment['Desember'], key=lambda x: x['jumlah_investasi'])
    max_december_return = max(investment['Desember'], key=lambda x: x['return'])
    december_investment_result = {
        'amount': float(max_december_investment['jumlah_investasi']),
        'return': float(max_december_return['return']),
        'total': float(max_december_investment['jumlah_investasi']) + float(max_december_return['return'])
    }
    
    rey = load_rey()
    rey_income = load_rey_income()
    rey_outcome = load_rey_outcome()
    
    dania = load_dania()
    dania_income = load_dania_income()
    dania_outcome = load_dania_outcome()
    
    dania_expense_food = max((item for item in dania_outcome if item['jenis_pengeluaran'] == 'FOOD'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    rey_expense_food = max((item for item in rey_outcome if item['jenis_pengeluaran'] == 'FOOD'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    total_expense_food = dania_expense_food + rey_expense_food
    
    dania_expense_transport = max((item for item in dania_outcome if item['jenis_pengeluaran'] == 'TRANSPORTATION'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    rey_expense_transport = max((item for item in rey_outcome if item['jenis_pengeluaran'] == 'TRANSPORTATION'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    total_expense_transport = dania_expense_transport + rey_expense_transport
    
    dania_expense_entertainment = max((item for item in dania_outcome if item['jenis_pengeluaran'] == 'ENTERTAINMENT'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    rey_expense_entertainment = max((item for item in rey_outcome if item['jenis_pengeluaran'] == 'ENTERTAINMENT'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    total_expense_entertainment = dania_expense_entertainment + rey_expense_entertainment
    
    dania_expense_shopping = max((item for item in dania_outcome if item['jenis_pengeluaran'] == 'SHOPPING'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    rey_expense_shopping = max((item for item in rey_outcome if item['jenis_pengeluaran'] == 'SHOPPING'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    total_expense_shopping = dania_expense_shopping + rey_expense_shopping
    
    dania_expense_grocery = max((item for item in dania_outcome if item['jenis_pengeluaran'] == 'GROCERY'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    rey_expense_grocery = max((item for item in rey_outcome if item['jenis_pengeluaran'] == 'GROCERY'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    total_expense_grocery = dania_expense_grocery + rey_expense_grocery
    
    dania_expense_investment = max((item for item in dania_outcome if item['jenis_pengeluaran'] == 'INVESTMENT'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    rey_expense_investment = max((item for item in rey_outcome if item['jenis_pengeluaran'] == 'INVESTMENT'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    total_expense_investment = dania_expense_investment + rey_expense_investment
    
    dania_expense_parking = max((item for item in dania_outcome if item['jenis_pengeluaran'] == 'PARKING'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    rey_expense_parking = max((item for item in rey_outcome if item['jenis_pengeluaran'] == 'PARKING'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    total_expense_parking = dania_expense_parking + rey_expense_parking
    
    dania_expense_other = max((item for item in dania_outcome if item['jenis_pengeluaran'] == 'OTHER'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    rey_expense_other = max((item for item in rey_outcome if item['jenis_pengeluaran'] == 'OTHER'), key=lambda x: x['id_pengeluaran'])['jumlah_pengeluaran']
    total_expense_other = dania_expense_other + rey_expense_other
    
    return render_template('home/index.html', 
        user=current_user(), 
        investment=investment, 
        january_investment_result=january_investment_result, 
        february_investment_result=february_investment_result, 
        march_investment_result=march_investment_result, 
        april_investment_result=april_investment_result,
        may_investment_result=may_investment_result, 
        june_investment_result=june_investment_result,
        july_investment_result=july_investment_result,
        august_investment_result=august_investment_result,
        september_investment_result=september_investment_result,
        october_investment_result=october_investment_result,
        november_investment_result=november_investment_result,
        december_investment_result=december_investment_result,
        rey=rey,
        dania=dania,
        totalExpenseFood =total_expense_food,
        totalExpenseTransport = total_expense_transport,
        totalExpenseEntertainment = total_expense_entertainment,
        totalExpenseShopping = total_expense_shopping,
        totalExpenseGrocery = total_expense_grocery,
        totalExpenseInvestment = total_expense_investment,
        totalExpenseParking = total_expense_parking,
        totalExpenseOther = total_expense_other,)

@app.route('/rey', methods=['GET', 'POST'])
@login_required
def rey():
    if request.method == 'POST':
        data = request.form['data']
        # Process the data as needed
        return redirect(url_for('home'))
    
    return render_template('rey/index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


