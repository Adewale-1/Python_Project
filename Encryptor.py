
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 
             'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alteration= True

while alteration:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))%26
	
	
	def encrypt(text, shift):
		shifted=""
		for letter in text:
			if letter in alphabet:
				position= alphabet.index(letter)
				new= position+ shift
				new_letter= alphabet[new]
				shifted+=new_letter
			else:
				shifted+=letter
		print(f"The encoded text is {shifted}")
	
	def decrypt(plain, amount):
		newly_shifted=""
		for alpha in text:
			if alpha in alphabet:
				new_position= alphabet.index(alpha)
				new2= new_position-shift
				new_letter2= alphabet[new2]
				newly_shifted +=new_letter2
			else:
				newly_shifted+=alpha
		print(f"The decrypted text is {newly_shifted}")
		
	
	if direction=="encode":
		encrypt(text, shift)
	elif direction=="decode":
		decrypt(plain=text, amount=shift)
	
	
	
	restart=input( "Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
	if restart=="no":
		alteration= False
		print("Goodbye")
