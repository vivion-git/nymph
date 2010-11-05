about file method:
f=open("filename","r"),if at the beginning ,you write like above ,then
f.readline() method can read the next line by repeatting the
command"f.readline(),like that:
fe=open("ppr.py","r")
>>> fe.readline()
'import sys,os,pprint\n'
>>> fe.readline()
'visited={}\n'
>>> fe.readline()
'allsizes=[]\n'
but if you don't write this command"e=open("ppr.py","r")"
only write the command "e=open("filename").readline()
then it can run but only can display the first line.
additionally speaking,file.read() is used to read entire file into string,and
the file.readlines() is used to read entire file into line strings list.


