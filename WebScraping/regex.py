import re

haystack = 'jkasdhjkasdhkasjdh<script>javascripth\nere</script>alsh\ndklashdaskld'

needle = '<script(.|\n)*</script>'

re_match = re.search(needle, haystack)
matching_text= re_match.group(0)
print(matching_text)
