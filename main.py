from flask import Flask, request
import requests

app1 = Flask(__name__)

@app1.route('/app')
def app1_route():
    name = request.args.get('name')
    org = request.args.get('org')
    
    # Make a GET request to app2 with the name and org values as URL parameters
    response = requests.get('http://127.0.0.1:5001/', params={'name': name, 'org': org})
    
    return response.text

if __name__ == '__main__':
    app1.run(debug=True)
