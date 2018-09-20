#program to extract domain name from a url entered by user;using slicing
#url should be of the form;https://www.abcdef.com
url=input('enter url:')
domainName=url[12:-3]
print(domainName)
