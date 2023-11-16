def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


@app.route("/todo", methods=["POST", "GET"])
@login_required
def todo():
    if request.method == "POST":
        return redirect("/todo")
    return render_template("todo.html")
    