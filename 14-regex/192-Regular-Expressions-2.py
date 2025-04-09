# 192 : Regular Expressions 2
# TODO: more advanced patterns (regular expressions)
# - only numbers    :       \d
# - only letters    :       \w
# - only whitespace :       \s
# - only not numbers:       \D
# - only not letters:       \W
# - only not whitespace:    \S
# - any character   :       .
# TODO: [Regex101] build, test, and debug regex
# - https://regex101.com/

import re

# TODO: simple pattern
text_pattern = re.compile("text")  # specific text
text_pattern.search("text & text")  # <re.Match object; span=(0, 4), match='text'>
text_pattern.findall("text & text")  # ['text', 'text']
text_pattern.fullmatch("text & text")  # None

# TODO: more advanced patterns
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
pattern = r"([a-z]).(is)"  # TODO: r: raw string
test_str = "This is test text in test text"
matches = re.finditer(pattern, test_str, re.MULTILINE)
print(matches)  # TODO: <callable_iterator object at 0x000001E3B6D4F3D0>

for matchNum, match in enumerate(matches, start=1):
    print(
        "Match {matchNum} was found at {start}-{end}: {match}".format(
            matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()
        )
    )

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print(
            "Group {groupNum} found at {start}-{end}: {group}".format(
                groupNum=groupNum,
                start=match.start(groupNum),
                end=match.end(groupNum),
                group=match.group(groupNum),
            )
        )
