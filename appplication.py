from flask import Flask, request
from db import get_details

app2 = Flask(__name__)

@app2.route('/')
def app2_route():
    name = request.args.get('name')
    org = request.args.get('org')
    
    if name and org:
        message = {'name':name,'oraganisation':org}
    else:
        name, org = get_details()
        message = {'name':name,'oraganisation':org}
    
    return message


if __name__ == '__main__':
    app2.run(port=5001, debug=True)
