#PROTOCOLS
 * 0 - Request log-in
 * 1 - Confirm log-in
 * 2 - Error
 * 3 - Send Message
 * 4 - Recieve Message
 * 5 - User has logged in
 * 6 - User has logged out

##[0] Request log-in
<pre>
{
	"protocol": 0,
	"data": {
		"timestamp": "",
		"username": ""
	}
}
</pre>

##[1] Confirm log-in
<pre>
{
	"protocol": 1,
	"data": {
		"welcome_msg": "",
		"userlist": [
			"User_A",
			"User_B",
			"User_C"
		]
	}
}
</pre>

##[2] Error
<pre>
{
	"protocol": 2,
	"data": {
		"timestamp": "",
		"error_msg": ""
	}
}
</pre>

##[3] Send a message
<pre>
{
	"protocol": 3,
	"data": {
		"timestamp": "",
		"message_enc": "",
		"username": ""
	}
}
</pre>

##[4] Send a message
<pre>
{
	"protocol": 4,
	"data": {
		"timestamp": "",
		"message_enc": "",
		"username": ""
	}
}
</pre>

##[5] User log-in
<pre>
{
	"protocol": 5,
	"data": {
		"timestamp": "",
		"username": ""
	}
}
</pre>

##[6] User log-out
<pre>
{
	"protocol": 6,
	"data": {
		"timestamp": "",
		"username": ""
	}
}
</pre>