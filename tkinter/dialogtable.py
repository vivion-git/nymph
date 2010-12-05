from tkFileDialog import askdirectory
from tkMessageBox import askquestion ,showerror
from tkColorChooser import askcolor
from tkSimpleDialog import askfloat
demos={'Open':askdirectory,
'Color':askcolor,
'Query':lambda:askquestion('Warning','You typed "rm*"\nConfirm?'),
'Error':lambda:showerror('Error!',"He's dead,Jim"),
'Input':lambda:askfloat('Entry','Enter credit card number')}


