import re

txt= """ %eu% %estou% %mui%to% %feliz%, %M%aria %Ce%ci%lia %est%%á% %che%ga%ndo%"""
match = re.sub("%", "", txt)
print(match)