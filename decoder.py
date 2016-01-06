# Secret Decoder

#save a message to a file

#encrypt the message to a separate file

#option to decrypt a file


def main():
	file_name = raw_input("Enter a file name: ")
	old_message = open(file_name)
	print"Your old message said: "
	print old_message.read()
	
	message = raw_input("Enter a message:")
	
	plain_message = open("plain_message.txt", "w")
	plain_message.write(message)
	plain_message.close()
	


main()