#$env:FLASK_APP = "api.py"
#flask run -h 192.168.167.1
from flask.json import jsonify
from Source_code.AccessPoint import Execution_Point
from flask import Flask,request,jsonify
import base64
from Source_code import Path_file
app = Flask(__name__)  
app.config['JSONIFY_PRETTYPRINT_REGULAR']=False
@app.route('/Topic',methods = ['GET'])


def gettopic():
    d={}
    topic_name= request.args.get('topic')
    obj=Execution_Point(topic_name)
    obj.Start_Excution()
    d['topic']="Classification Done!"

    return jsonify(d)
    
   
if __name__ == '__main__':  
   app.run(debug = True)  



#

##maxtweet=max(disa,rain,thun,cloudy,fog,snow,clear)
#            'topic': topic_name, 'disa':disa, 'rain':rain,
#            'thun':thun,'cloudy':cloudy,'fog':fog,
#           'snow':snow,'clear':snow,'maxtweet':maxtweet,
#        }
#    return jsonify(content)
   # image = open(file, 'rb')
   # image_read = image.read()
   # image_64_encode = base64.encodebytes(image_read)
