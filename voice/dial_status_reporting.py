from flask import Flask, request, Response
import plivoxml

app=Flask(__name__)

@app.route('/dial/', methods=['GET','POST'])
def dial_xml():

    # Generate Dial XML

    response = plivoxml.Response()
    params = {
        'action' : "https://morning-ocean-4669.herokuapp.com/dial_status/",
        'method' : 'GET'
    }
    response.addSpeak("Connecting your call..")
    d = response.addDial(**params)
    d.addNumber("1111111111")
    print response.to_xml()
    return Response(str(response), mimetype='text/xml')

# Sample Dial XML
# <Response>
#	<Speak>Connecting your call..</Speak>
#	<Dial action="https://morning-ocean-4669.herokuapp.com/dial_status/" method="GET">
#		<Number>1111111111</Number>
#	</Dial>
# </Response>

@app.route('/dial_status/', methods=['GET','POST'])
def dial_status():

	# After completion of the call, Plivo will report back the status to the action URL in the Dial XML.

    status = request.args.get('DialStatus')
    aleg = request.args.get('DialALegUUID')
    bleg = request.args.get('DialBLegUUID')
    print "Status : %s, ALeg Uuid : %s, BLeg Uuid : %s" % (status,aleg,bleg)
    return "Dial status reported"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# Sample successful output
# Status : completed, ALeg Uuid : 52bb0058-902d-11e4-9681-2d7d49a323a0, BLeg Uuid : 54f84290-902d-11e4-96df-2d7d49a323a0