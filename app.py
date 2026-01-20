from flask import Flask, render_template, send_from_directory, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
from models import db, User, Client, Portfolio
from forms import LoginForm, ClientForm, PortfolioForm

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'working-media-secret-key-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workingmedia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folders exist
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'clients'), exist_ok=True)
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'portfolio'), exist_ok=True)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'
login_manager.login_message = 'Silakan login untuk mengakses halaman admin.'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create tables and default admin user
with app.app_context():
    db.create_all()
    # Create default admin if not exists
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', email='admin@workingmedia.com')
        admin.set_password('admin123')  # Change this password!
        db.session.add(admin)
        db.session.commit()
        print("Default admin created: username='admin', password='admin123'")

# Helper function for file upload
def save_file(file, folder):
    """Save uploaded file and return path"""
    if file:
        filename = secure_filename(file.filename)
        # Add timestamp to filename to avoid conflicts
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{timestamp}{ext}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], folder, filename)
        file.save(filepath)
        return f'/static/uploads/{folder}/{filename}'
    return None

# Public routes
@app.route('/')
def index():
    clients = Client.query.filter_by(is_active=True).order_by(Client.order, Client.created_at).all()
    portfolio_items = Portfolio.query.filter_by(is_active=True).order_by(Portfolio.order, Portfolio.created_at).all()
    return render_template('index.html', clients=clients, portfolio_items=portfolio_items)

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

# Admin Authentication
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login berhasil!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin_dashboard'))
        else:
            flash('Username atau password salah.', 'danger')
    
    return render_template('admin/login.html', form=form)

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    flash('Anda telah logout.', 'info')
    return redirect(url_for('index'))

# Admin Dashboard
@app.route('/admin')
@login_required
def admin_dashboard():
    clients_count = Client.query.count()
    portfolio_count = Portfolio.query.count()
    return render_template('admin/dashboard.html', 
                         clients_count=clients_count,
                         portfolio_count=portfolio_count)

# Client Management
@app.route('/admin/clients')
@login_required
def admin_clients():
    clients = Client.query.order_by(Client.category, Client.order, Client.name).all()
    return render_template('admin/clients.html', clients=clients)

@app.route('/admin/clients/add', methods=['GET', 'POST'])
@login_required
def admin_add_client():
    form = ClientForm()
    if form.validate_on_submit():
        client = Client(
            name=form.name.data,
            category=form.category.data,
            emoji=form.emoji.data or '🏢',
            order=form.order.data,
            is_active=form.is_active.data
        )
        
        # Handle logo upload
        if form.logo.data:
            logo_path = save_file(form.logo.data, 'clients')
            client.logo_path = logo_path
        
        db.session.add(client)
        db.session.commit()
        flash(f'Klien "{client.name}" berhasil ditambahkan!', 'success')
        return redirect(url_for('admin_clients'))
    
    return render_template('admin/client_form.html', form=form, title='Tambah Klien')

@app.route('/admin/clients/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_edit_client(id):
    client = Client.query.get_or_404(id)
    form = ClientForm(obj=client)
    
    if form.validate_on_submit():
        client.name = form.name.data
        client.category = form.category.data
        client.emoji = form.emoji.data or '🏢'
        client.order = form.order.data
        client.is_active = form.is_active.data
        
        # Handle logo upload
        if form.logo.data:
            logo_path = save_file(form.logo.data, 'clients')
            client.logo_path = logo_path
        
        db.session.commit()
        flash(f'Klien "{client.name}" berhasil diupdate!', 'success')
        return redirect(url_for('admin_clients'))
    
    return render_template('admin/client_form.html', form=form, title='Edit Klien', client=client)

@app.route('/admin/clients/delete/<int:id>', methods=['POST'])
@login_required
def admin_delete_client(id):
    client = Client.query.get_or_404(id)
    name = client.name
    db.session.delete(client)
    db.session.commit()
    flash(f'Klien "{name}" berhasil dihapus!', 'success')
    return redirect(url_for('admin_clients'))

# Portfolio Management
@app.route('/admin/portfolio')
@login_required
def admin_portfolio():
    portfolio_items = Portfolio.query.order_by(Portfolio.category, Portfolio.order, Portfolio.created_at.desc()).all()
    return render_template('admin/portfolio.html', portfolio_items=portfolio_items)

@app.route('/admin/portfolio/add', methods=['GET', 'POST'])
@login_required
def admin_add_portfolio():
    form = PortfolioForm()
    if form.validate_on_submit():
        portfolio = Portfolio(
            title=form.title.data,
            description=form.description.data,
            category=form.category.data,
            order=form.order.data,
            is_active=form.is_active.data
        )
        
        # Handle image upload (required for new portfolio)
        if form.image.data:
            image_path = save_file(form.image.data, 'portfolio')
            portfolio.image_path = image_path
        else:
            flash('Gambar portfolio harus diupload!', 'danger')
            return render_template('admin/portfolio_form.html', form=form, title='Tambah Portfolio')
        
        db.session.add(portfolio)
        db.session.commit()
        flash(f'Portfolio "{portfolio.title}" berhasil ditambahkan!', 'success')
        return redirect(url_for('admin_portfolio'))
    
    return render_template('admin/portfolio_form.html', form=form, title='Tambah Portfolio')

@app.route('/admin/portfolio/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_edit_portfolio(id):
    portfolio = Portfolio.query.get_or_404(id)
    form = PortfolioForm(obj=portfolio)
    
    if form.validate_on_submit():
        portfolio.title = form.title.data
        portfolio.description = form.description.data
        portfolio.category = form.category.data
        portfolio.order = form.order.data
        portfolio.is_active = form.is_active.data
        
        # Handle image upload
        if form.image.data:
            image_path = save_file(form.image.data, 'portfolio')
            portfolio.image_path = image_path
        
        db.session.commit()
        flash(f'Portfolio "{portfolio.title}" berhasil diupdate!', 'success')
        return redirect(url_for('admin_portfolio'))
    
    return render_template('admin/portfolio_form.html', form=form, title='Edit Portfolio', portfolio=portfolio)

@app.route('/admin/portfolio/delete/<int:id>', methods=['POST'])
@login_required
def admin_delete_portfolio(id):
    portfolio = Portfolio.query.get_or_404(id)
    title = portfolio.title
    db.session.delete(portfolio)
    db.session.commit()
    flash(f'Portfolio "{title}" berhasil dihapus!', 'success')
    return redirect(url_for('admin_portfolio'))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    if request.path.startswith('/admin'):
        return render_template('admin/404.html'), 404
    return render_template('index.html'), 200

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('index.html'), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
