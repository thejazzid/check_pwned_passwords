import requests
import hashlib

def chek_pass(hash_5):
    URL = "https://api.pwnedpasswords.com/range/{}"
    r = requests.get(URL.format(hash_5))
    return r.text

def find_count(full_hash):
    count = 0
    hash_prefix = full_hash[0:5]
    getlistofpass = chek_pass(hash_prefix).split("\n")
    if getlistofpass == None: return 0
    for i in getlistofpass:
        hash_pass = i[0:i.find(":")]
        if (hash_prefix.upper() + hash_pass) == full_hash.upper():
            count = int(i[i.find(":")+1:-1])
    return count

def main():
    password = input("Enter your password and hit Enter: ")
    h = hashlib.sha1()
    h.update(password.encode())
    full_hash = h.hexdigest()
    pass_count = find_count(full_hash)
    if pass_count!=0:
        print("Your password has benn pwned {} times!".format(pass_count))
    else:
        print("It seems your passord is not pwned, yet.")

if __name__ == "__main__":
    main()
