import subprocess
from flask import Flask, redirect, url_for
from flask import jsonify
from flask import render_template
import piplates.RELAYplate as RELAY

app = Flask(__name__)

@app.route("/")
def index():
    data = getBoardData()
    app.logger.error("Index Page")
    return render_template('board.html', FWrev=data['FWrev'], HWrev=data['HWrev'], PMrev=data['PMrev'], STATE=data['STATE'] )

@app.route("/hello")
def hello():
    app.logger.error("Hello Page")
    return "Hello World!"

@app.route("/board")
def getBoard():
    data = getBoardData()
    return jsonify( data )

@app.route("/update")
def updateCode():
    app.logger.error("Update code from github")
    subprocess.call(['/home/pi/src/eagleweb/updateEagleCode.sh'])
    return redirect( url_for('index') )

def getBoardData():
    brd = 0
    bites = bite_to_boolArray( int_to_bin( RELAY.relaySTATE( brd ) ) )
    data = { "id": RELAY.getID( brd ), "FWrev": RELAY.getFWrev( brd ), "HWrev": RELAY.getHWrev( brd ), "PMrev": RELAY.getPMrev( ), "STATE": bites }
    app.logger.error( data )
    return data
# End def

def int_to_bin(x):
  return bin(x)[2:].zfill(7)
# End def

def bite_to_boolArray(x):
   switches=[]
   for bite in list(x):
      if bite == "1":
         switches.append( "On" )
      elif bite == "0":
         switches.append( "Off" )
      else:
         print "error"
      # End if
   # End for
   return switches
# End def
