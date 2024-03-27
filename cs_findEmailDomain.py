# An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

# The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

# Given a valid email address, find its domain part.

# Example

# For address = "prettyandsimple@example.com", the output should be
# solution(address) = "example.com";
# For address = "fully-qualified-domain@codesignal.com", the output should be
# solution(address) = "codesignal.com".



def solution(address):
    target_index= []
    for s in range(len(address)):
        if address[s]=="@":
            target_index.append(s)
    if len(target_index)==1:
        return address[target_index[0]+1:]
    else:
        return address[target_index[-1]+1:]
    




def solution(address):
    a = address.split('@')
    return a[-1] 