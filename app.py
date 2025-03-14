from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title': 'Software Engineer',
    'company': 'Google',
    'location': 'Bangalore, India',
    'salary': 'RS. 1000000',
    'description': 'Google is hiring a software engineer'
}, 
    {
    'id': 2,
    'title': 'Data Analyst',
    'company': 'Razorpay',
    'location': 'Delhi, India',
    'salary': 'RS. 1500000',
    'description': 'Razorpay is hiring a software engineer'
}, 
    {
    'id': 3,
    'title': 'Data Scientist',
    'company': 'Amazon',
    'location': 'pune, India',
    'salary': 'RS. 1700000',
    'description': 'Amazon is hiring a software engineer'
}, 
    {
    'id': 4,
    'title': 'Backend Engineer',
    'company': 'flipkart',
    'location': 'chennai, India',
    'salary': 'RS. 900000',
    'description': 'flipkart is hiring a software engineer'
}
]


@app.route('/')
def index():
    return render_template('home.html', jobs=JOBS, company_name='Indian')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
