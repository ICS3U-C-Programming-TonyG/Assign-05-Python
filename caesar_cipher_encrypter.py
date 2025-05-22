def encrypt_text(plaintext, n):
    ans_list = []
    for ch in plaintext:
        # Compound Boolean and nested if
        if (ch.isalpha() and not ch.isdigit()) or ch == " ":
            if ch == " ":
                ans_list.append(" ")
            else:
                if ch.isupper():
                    ans_list.append(chr((ord(ch) + n - 65) % 26 + 65))
                else:
                    ans_list.append(chr((ord(ch) + n - 97) % 26 + 97))
        else:
            ans_list.append(ch)
    # Use a while loop to build the answer string from the list
    ans = ""
    idx = 0
    while idx < len(ans_list):
        ans += ans_list[idx]
        idx += 1
    return ans

# Use the function with user input
plaintext = input("Write your message: ")
n = int(input("What order of magnitude? "))
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext, n))