import hashlib   # this calls a module called 'hashlib' that isn't automatically fired up when Python starts
import os
import subprocess

def MD5hash(string):
   ''' 
   Returns the MD5 hash of a string.
   
    `hashlib.md5(...)` is telling the computer that it will find the `md5` function in the `hashlib` module
   `"password".encode('utf-8')` is saying how to encode the word "password". There are different ways printable letters can be encoded into bits, and utf-8 is one standard way of doing it. Normally your application, such as a browser or word processor, can just work it out and print the letters as intended. However, hash functions act on a string of bits, so it needs to know how to interpret the characters you've entered.
   A hash function also returns a string of bits, but these are very hard for humans to read. Hexadecimal is a way of encoding this string of bits so it's easier to read. The command `hexdigest()` is saying to return the hash in that format.
   '''
   return hashlib.md5(string.encode('utf-8')).hexdigest()

def MaskAttack(hashstring, mask, customset=None):
    '''
    Performs a hashcat mask attack against the hashstring
    
   `hashcat`: run the hashcat program
   `-a 3`: use attack mode 3, which is the mode for mask attacks
   `-m 0`: the hash is of type 0, which is the code for MD5 hashes
   `hashstring`: is the hash you want to break
   `mask`: is the mask, as explained above
   `--show`: show the recovered password for that hash. Hashcat looks in its broken hash 'potfile' for the hash specified, and prints the password if it's in there. 
    '''
    if customset:
        customcommand='-1'+customset
        subprocess.run(['hashcat', '-a', '3', '-m', '0', hashstring, customcommand, mask])
    else:
        subprocess.run(['hashcat', '-a', '3', '-m', '0', hashstring, mask])
        
    s=subprocess.check_output(['hashcat', '-a', '3', '-m', '0', hashstring, '--show'])
    if len(s)>=32:
        out=s.decode("ascii")[:-1].split(':')
        print('The password for hash ',out[0],' is ',out[1])
    elif not s:
        print('Password not recovered!')
        out=0
    
    return out

def DictAttack(hashstring, dictfile, rules=None):
    
    if rules:
        rulecommand = ['hashcat', '-a', '0', '-m', '0', hashstring]
        for rule in rules:
            rulecommand.append('-r')
            rulecommand.append(rule)
        rulecommand.append(dictfile)
        h=subprocess.run( rulecommand, capture_output=True)
        if str(h.stderr).find('No such file or directory')>0 and str(h.stderr).find('Password_cracking_workshop')>0:
            print("Dictionary file not found")
        if str(h.stderr).find('No such file or directory')>0 and str(h.stderr).find('rule')>0:
            print("Rule file not found")
    else:    
        h=subprocess.run(['hashcat', '-a', '0', '-m', '0', hashstring, dictfile], capture_output=True)
        if str(h.stderr).find('No such file or directory')>0:
            print("Dictionary file not found")
        
    
    s=subprocess.check_output(['hashcat', '-a', '3', '-m', '0', hashstring, '--show'])
    if len(s)>=32:
        out=s.decode("ascii")[:-1].split(':')
        print('The password for hash ',out[0],' is ',out[1])
    elif not s:
        print('Password not recovered!')
        out=0
    
    return out

def PrintSolved():
    potfile_path = os.path.join(os.path.expanduser("~"), ".hashcat/hashcat.potfile")
    with open(potfile_path) as potfile:
        i=1
        for line in potfile.readlines():
            print(str(i)+') '+line)
            i=i+1
            
    return 0

def EmptyPot():
    potfile_path = os.path.join(os.path.expanduser("~"), ".hashcat/hashcat.potfile")
    open(potfile_path,"w").close()
    return 0
