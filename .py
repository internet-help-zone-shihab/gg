CorrectUsername = "rana"
CorrectPassword = "rana"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;97mUSER ID \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;97mPASWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.Youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.Youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 50*"\033[1;96m▪"