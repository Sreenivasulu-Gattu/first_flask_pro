from flask import Flask
FAI = Flask(__name__)
@FAI.route('/strresponse')
def strresponse():
    return '<center><marquee><h1 style="color: brown;">Hi hello </h1></marquee></center>'

if __name__ == '__main__':
    FAI.run(debug=True)