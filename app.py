from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Database simulation (in-memory)
db = {
    'users': [],
    'accounts': [],
    'journal_entries': [],
    'customers': [],
    'suppliers': [],
    'products': [],
    'inventory': [],
    'sales': [],
    'purchases': [],
}

@app.route('/')
def index():
    """الصفحة الرئيسية - لوحة التحكم"""
    return render_template('index.html')

@app.route('/journal')
def journal():
    """دفتر اليومية"""
    return render_template('journal.html')

@app.route('/ledger')
def ledger():
    """دفتر الأستاذ"""
    return render_template('ledger.html')

@app.route('/inventory')
def inventory():
    """المخزون"""
    return render_template('inventory.html')

@app.route('/purchases')
def purchases():
    """المشتريات"""
    return render_template('purchases.html')

@app.route('/sales')
def sales():
    """المبيعات"""
    return render_template('sales.html')

@app.route('/cash')
def cash():
    """الخزينة"""
    return render_template('cash.html')

@app.route('/customers')
def customers():
    """العملاء"""
    return render_template('customers.html')

@app.route('/suppliers')
def suppliers():
    """الموردين"""
    return render_template('suppliers.html')

@app.route('/adjustments')
def adjustments():
    """قيود التسوية"""
    return render_template('adjustments.html')

@app.route('/accounts')
def accounts():
    """دليل الحسابات"""
    return render_template('accounts.html')

@app.route('/assets')
def assets():
    """الأصول الثابتة"""
    return render_template('assets.html')

@app.route('/financials')
def financials():
    """القوائم المالية"""
    return render_template('financials.html')

@app.route('/analytics')
def analytics():
    """التحليلات"""
    return render_template('analytics.html')

@app.route('/reports')
def reports():
    """التقارير"""
    return render_template('reports.html')

# API Endpoints
@app.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    """الحصول على بيانات لوحة التحكم"""
    return jsonify({
        'total_accounts': len(db['accounts']),
        'total_customers': len(db['customers']),
        'total_suppliers': len(db['suppliers']),
        'total_products': len(db['products']),
        'journal_entries': len(db['journal_entries']),
        'sales_count': len(db['sales']),
        'purchases_count': len(db['purchases']),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/journal', methods=['GET', 'POST'])
def manage_journal():
    """إدارة قيود اليومية"""
    if request.method == 'POST':
        entry = request.json
        entry['id'] = len(db['journal_entries']) + 1
        entry['date'] = datetime.now().isoformat()
        db['journal_entries'].append(entry)
        return jsonify(entry), 201
    return jsonify(db['journal_entries'])

@app.route('/api/customers', methods=['GET', 'POST'])
def manage_customers():
    """إدارة العملاء"""
    if request.method == 'POST':
        customer = request.json
        customer['id'] = len(db['customers']) + 1
        db['customers'].append(customer)
        return jsonify(customer), 201
    return jsonify(db['customers'])

@app.route('/api/suppliers', methods=['GET', 'POST'])
def manage_suppliers():
    """إدارة الموردين"""
    if request.method == 'POST':
        supplier = request.json
        supplier['id'] = len(db['suppliers']) + 1
        db['suppliers'].append(supplier)
        return jsonify(supplier), 201
    return jsonify(db['suppliers'])

@app.route('/api/products', methods=['GET', 'POST'])
def manage_products():
    """إدارة الأصناف"""
    if request.method == 'POST':
        product = request.json
        product['id'] = len(db['products']) + 1
        db['products'].append(product)
        return jsonify(product), 201
    return jsonify(db['products'])

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
