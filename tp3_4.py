from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

key = b'abcdefghijklmnopqrstuvwxyz123456'
iv = b'00000000000000000000000000000000'
def File_Encrypt(fs):
    cipher = AES.new(key, AES.MODE_EAX, iv)
    ciphertext = cipher.encrypt(fs.encode('utf-8'))
    return b2a_hex(ciphertext)

def File_Decrypt(fs):
    cipher = AES.new(key, AES.MODE_EAX, iv)
    plaintext = cipher.decrypt(a2b_hex(fs))
    return plaintext

if __name__=='__main__':
    filename = input("Choisir un nom de fichier: ")

    try:
        fic = open(filename)
    except:
        print("Le fichier n'existe pas!")
    finally:
        fic.close

    fic = open(filename,'r')
    outputfilename = 'output_' + filename
    fs = fic.read()
    fic_encrypt = open(outputfilename,'wb')
    fs_encrypt = File_Encrypt(fs)
    fic_encrypt.write(fs_encrypt)
    fic.close
    fic_encrypt.close

    fic_encrypt = open(outputfilename,'rb')
    fs_encrypt = fic_encrypt.read()
    print(File_Decrypt(fs_encrypt))
