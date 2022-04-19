import re , shutil ,os
datePattern = re.compile(r"""^(.*?) 
((0|1)?\d)- 
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$ 
w """, re.VERBOSE)