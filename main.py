# fontforge python script
# http://fontforge.org/python.html
import sys
import xml
import fontforge

ffname = 'chocobar'
if len(sys.argv) != 2:
  print "Usage: main.py <name>"
else:
  name = sys.argv[1];

cbft = fontforge.open('base.sfd')

# process here
cbft.fontname = name.capitalize()
cbft.familyname = ffname.capitalize()
cbft.fullname = (' ').join([ffname.capitalize(), name.capitalize()])

cbft.save(name + '.sfd')
