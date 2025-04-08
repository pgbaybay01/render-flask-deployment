from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

messages = []


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Store the message
        messages.append({
            'name': name,
            'email': email,
            'message': message
        })

        flash('Thank you for your message! We will get back to you soon.')
        return redirect(url_for('messages_page'))

    return render_template('contact.html')


@app.route('/messages')
def messages_page():
    return render_template('messages.html', messages=messages)


if __name__ == '__main__':
    app.run(debug=True)