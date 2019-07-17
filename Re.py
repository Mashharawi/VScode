import re
pattern = '[A-Z0-9]'
test_string = input("Enter Text:     ")
result = re.match(pattern, test_string)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
  # test commit