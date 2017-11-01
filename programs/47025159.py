def get_encrypt(original_text,dictionary):
    #4
    match= ""
    for base in original_text:
        match += dictionary[base]
    return match

def rev_look(encrypted_text, dictionary):
    match_key = []        
    for base in encrypted_text:
        for key in dictionary:
            if dictionary[key] == base:
                match_key.append(key)

    return match_key

def main():
    print('* Simple Substitution Cipher Tool *')
    #Define the dictionary
    dictionary_encryption = {' ':' ','a':'p', 'b':'h', 'c':'q', 'd':'g', 'e':'i', 'f':'u', 'g':'m', 'h':'e', 'i':'a', 'j':'y', 'k':'l', 'l':'n','m':'o', 'n':'f', 'o':'d', 'p':'x', 'q':'j', 'r':'k', 's':'r', 't':'c', 'u':'v', 'v':'s', 'w':'t', 'x':'z', 'y':'w', 'z':'b'}
    #2
    original_text =(input('Please enter the original text: '))
    #3
    dictionary_decryption = {y:x for x,y in dictionary_encryption.items()}
    encrypted_text = get_encrypt(original_text,dictionary_encryption)
    print('The encrypted text is: ', encrypted_text)
    print('The decrypted text is: ', rev_look(encrypted_text,dictionary_encryption))

main()
