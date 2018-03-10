'''short code to extract US numbers from text'''
import re
numbers = ' 123.456.7889 (123)-456-7888 (425) 465-7523 456 123-7891 111 111.1111 (222)333-4444 666 777 8888 987-654-4321'
res = re.findall(r'\d{3}\)*?\-*?\s*?\.*?\d{3}\-*?\s*?\.*?\d{3}', numbers)
