from app.decorators import role_required

@employers_bp.route('/dashboard')
@login_required
@role_required('employer') # Only users with role='employer' can enter 
def dashboard():
    # ... logic for employer dashboard [cite: 33]
    return render_template('employers/dashboard.html')