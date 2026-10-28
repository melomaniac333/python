from django.shortcuts import render

# Create your views here.

import re
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.utils.html import escape


def login_view(request):
    message = ""
    color = "red"

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        # Regular expression for username
        username_pattern = r"^[A-Za-z0-9]{3,15}$"

        # Regular expression for email
        email_pattern = (
            r"^[A-Za-z0-9._%+-]+@"
            r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        )

        # Regular expression for password
        password_pattern = (
            r"^(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*[0-9])"
            r"(?=.*[@$!%*?&#])"
            r"[A-Za-z0-9@$!%*?&#]{8,}$"
        )

        if not re.fullmatch(username_pattern, username):
            message = (
                "Invalid username! Use 3-15 letters or numbers."
            )

        elif not re.fullmatch(email_pattern, email):
            message = "Invalid email address!"

        elif not re.fullmatch(password_pattern, password):
            message = (
                "Invalid password! Use at least 8 characters, "
                "one uppercase, one lowercase, one number "
                "and one special character."
            )

        else:
            message = "All fields are valid!"
            color = "green"

    token = get_token(request)

    page = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Login</title>
    </head>
    <body>
        <h2>Login Page</h2>

        <form method="POST">
            <input type="hidden" name="csrfmiddlewaretoken"
                   value="{escape(token)}">

            <label>Username:</label>
            <input type="text" name="username" required>
            <br><br>

            <label>Email:</label>
            <input type="text" name="email" required>
            <br><br>

            <label>Password:</label>
            <input type="password" name="password" required>
            <br><br>

            <button type="submit">Login</button>
        </form>

        <p style="color: {color};">{escape(message)}</p>
    </body>
    </html>
    """

    return HttpResponse(page)
