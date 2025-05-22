def encrypt_text(plaintext, n):
    ans = ""
    for ch in plaintext:
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        elif ch.islower():
            ans += chr((ord(ch) + n - 97) % 26 + 97)
        else:
            ans += ch  # Leave non-letters unchanged
    return ans

plaintext = input("Write your message: ")
n = int(input("What order of magnitude? "))
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext, n))