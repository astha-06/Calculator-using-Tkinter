from tkinter import*
root= Tk()  #root is a widget

e=Entry(root,width=30,borderwidth=5)   # for creating a space to get I/P and displaying O/P
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_add():
	first_number=e.get()
	global fnum,math
	fnum=int(first_number)
	math="add"
	e.delete(0,END)

def button_sub():
	first_number=e.get()
	global fnum,math
	fnum=int(first_number)
	math="sub"
	e.delete(0,END)

def button_mul():
	first_number=e.get()
	global fnum,math
	fnum=int(first_number)
	math="mul"
	e.delete(0,END)

def button_div():
	first_number=e.get()
	global fnum,math
	fnum=int(first_number)
	math="div"
	e.delete(0,END)

def button_equal():
	second_num=e.get()
	e.delete(0,END)
	if math=="add":
		e.insert(0,fnum+int(second_num))
	elif math=="sub":
		e.insert(0,fnum-int(second_num))
	elif math=="mul":
		e.insert(0,fnum*int(second_num))
	elif math=="div":
		e.insert(0,fnum/int(second_num))
	
	

def button_clr():
	e.delete(0,END)

def button_click(number):
	
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))
	

b0=Button(text="0",padx=40,pady=20,command=lambda:button_click(0))
b1=Button(text="1",padx=40,pady=20,command=lambda:button_click(1))	
b2=Button(text="2",padx=40,pady=20,command=lambda:button_click(2))	
b3=Button(text="3",padx=40,pady=20,command=lambda:button_click(3))	
b4=Button(text="4",padx=40,pady=20,command=lambda:button_click(4))	
b5=Button(text="5",padx=40,pady=20,command=lambda:button_click(5))	
b6=Button(text="6",padx=40,pady=20,command=lambda:button_click(6))	
b7=Button(text="7",padx=40,pady=20,command=lambda:button_click(7))	
b8=Button(text="8",padx=40,pady=20,command=lambda:button_click(8))	
b9=Button(text="9",padx=40,pady=20,command=lambda:button_click(9))
b_equal=Button(text="=",padx=87,pady=20,command=button_equal)
b_clear=Button(text="ClR",padx=80,pady=20,command=button_clr)	
b_add=Button(text="+",padx=40,pady=20,command=button_add)	
b_sub=Button(text="-",padx=40,pady=20,command=button_sub)	
b_mul=Button(text="*",padx=40,pady=20,command=button_mul)	
b_div=Button(text="/",padx=40,pady=20,command=button_div)
#put the buttons on screen
b1.grid(row=3,column=0,)
b2.grid(row=3,column=1,)
b3.grid(row=3,column=2,)

b4.grid(row=2,column=0,)
b5.grid(row=2,column=1,)
b6.grid(row=2,column=2,)

b7.grid(row=1,column=0,)
b8.grid(row=1,column=1,)
b9.grid(row=1,column=2,)

b0.grid(row=4,column=0,)
b_equal.grid(row=4,column=1,columnspan=2)

b_add.grid(row=5,column=0)
b_sub.grid(row=5,column=1)
b_mul.grid(row=5,column=2)
b_div.grid(row=6,column=0)

b_clear.grid(row=6,column=1,columnspan=3)

root.mainloop()