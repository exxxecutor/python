

def nick(email_list):
	output = []
	for email in email_list:
		part = email.split('@')
		nick = email.split('@')[0]
		domen = part[1].split('.')[0]
		end = part[1].split('.')[1]

		output.append((nick, domen, end))
	return output

print(nick(['zuck26@facebook.com', 'page33@google.com', 'jeff42@amazon.com']))
