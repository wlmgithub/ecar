
import re

#address = re.compile(r'((?P<name>\w+\s+\w+)\s+)(?=(<.*>)|([^<].*[^>]))<?(<?P<email>[\w.\d+-]+@([\w\d.]+\.)+(com|edu|org))>?')

address = re.compile(
         '''
# A name is made up of letters, and may include "." 
# for title abbreviations and middle initials. 
((?P<name>
  ([\w.,]+\s+)*[\w.,]+
  )
  \s+
) # The name is no longer optional.

# LOOKAHEAD
# Email addresses are wrapped in angle brackets, but only 
# if both are present or neither is.
(?= (<.*>$) | ([^<].*[^>]$) )

<?  
	(?P<email> [\w\d.+-]+ @ ([\w\d.]+\.)+ (com|org|edu) 
	) 
>? 
    ''',
re.VERBOSE)



candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com>',
]

for candidate in candidates:
	print('Candidate: ', candidate)
	match = address.search(candidate)
	if match:
		print("		Match:")
		print("		Name: ",  match.groupdict()['name'])
		print("		Email: ",  match.groupdict()['email'])
	else:
	
		print("		No match")
	
