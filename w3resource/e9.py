"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
from datetime import datetime

exam_st_date = (11, 12, 2014)

exam_st_date = datetime.strptime(exam_st_date, '%m-%d-%Y').date()
print(exam_st_date)