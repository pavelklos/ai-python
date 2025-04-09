# 194 : Regular Expressions 3

# TODO: [Email Regex] ----------------------------------------------------------
# - https://emailregex.com/index.html
# Python: r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
# TODO: explanation
#   ()                        capture group
#   ^                         beginning of input
#   [a-zA-Z0-9_.+-]+          one or more characters in the list
#   @                         at sign
#   [a-zA-Z0-9-]+             one or more characters in the list
#   \.                        dot
#   [a-zA-Z0-9-.]+            one or more characters in the list
#   $                         end of input

# TODO: Check email address by regular expression ------------------------------
# - Import the re module.
# - Define a regular expression pattern for validating email addresses.
# - Create a function to check if a given string matches the email pattern.
# - Test the function with various email addresses.

import re

# Define a regular expression pattern for validating email addresses
email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def is_valid_email(email):
    return bool(email_pattern.match(email))


# Test the function with various email addresses
test_emails = [
    "test@example.com",
    "invalid-email",
    "another.test@domain.co.uk",
    "wrong@domain,com",
    "right.email@sub.domain.com",
]

for email in test_emails:
    print(f"{email}: {is_valid_email(email)}")

print()  # empty line

# TODO: [Regex101] build, test, and debug regex --------------------------------
# - https://regex101.com/
# TODO: Code Generator for Python

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
test_str = "test@example.com\n"
matches = re.search(regex, test_str)

if matches:
    print(
        "Match was found at {start}-{end}: {match}".format(
            start=matches.start(), end=matches.end(), match=matches.group()
        )
    )

    for groupNum in range(0, len(matches.groups())):
        groupNum = groupNum + 1

        print(
            "Group {groupNum} found at {start}-{end}: {group}".format(
                groupNum=groupNum,
                start=matches.start(groupNum),
                end=matches.end(groupNum),
                group=matches.group(groupNum),
            )
        )
