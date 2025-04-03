# 042 : Exercise: Password Checker
# - create some sort of input that we're going to ask

username = input("what is your username? ")  # John Doe
password = input("what is your password? ")  # 1234
password_length = len(password)  # 4
hidden_password = "*" * password_length  # ****

print(
    f"Hello {username}, your password {hidden_password} is {password_length} letters long."
)
