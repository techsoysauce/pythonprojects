#list used for shifting characters by caesarcypher function
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#definition that will encrypt and decrypt text entered by user
def ceasarcypher(direction, word, shift):
  new_word = ""
  index_of_char = 0

  if direction == 'encode':
    for char in word:
      index_of_char = alphabet.index(char)
      new_word += alphabet[index_of_char+shift]
    print(f"New word is: {new_word}")

  elif direction == 'decode':
    for char in word:
      index_of_char = alphabet.index(char)
      new_word += alphabet[index_of_char-shift]
    print(f"New word is: {new_word}")

  else:
     print("Improper choice, choose again")



#Greeting and prompt user to enter ceasar cypher values
print ("Hi, welcome to the ceasar cipher. \nUse encode to encrypt a new word and decode to make it plain text readable.")

user_direction = input("Enter 'encode' to encrypt or 'decode' to decrypt: \n")
text = input("Enter your text to encrypt/decrypt: \n")
shift_num = int(input ("Enter your desired shift # : \n"))

#Call ceasarcypher function with values entered by user
ceasarcypher(direction=user_direction, word=text, shift=shift_num)