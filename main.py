# fontforge python script
# http://fontforge.org/python.html
import os
import sys
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

files = os.listdir(name)
for f in files:
  ucp = int(f[:f.index('.')], 0x10)
  uname = f[(f.index('.') + 1):f.rfind('.')]
  g = cbft.createChar(ucp, uname)
  g.importOutlines(name + '/' + f)

cbft.save(name + '.sfd')
cbft.generate(name + '.ttf')
