import tkinter

window = tkinter.Tk()
window.title("Calculator")

def close_window(): 
    window.destroy()


def calc(sign):
	if (sign == '+'):
		operator_label.config(text='+')
		val1 = int(entry_A.get())
		val2 = int(entry_B.get())
		res = float(val1+val2)
		result_label.config(text=res)

	elif (sign == '-'):
		operator_label.config(text='-')
		val1 = int(entry_A.get())
		val2 = int(entry_B.get())
		res = float(val1-val2)
		result_label.config(text=res)
	
	elif (sign == '*'):
		operator_label.config(text='*')
		val1 = int(entry_A.get())
		val2 = int(entry_B.get())
		res = float(val1*val2)
		result_label.config(text=res)
	
	elif (sign == '/'):
		operator_label.config(text='/')
		val1 = int(entry_A.get())
		val2 = int(entry_B.get())
		if val2 == 0:
			result_label.config(text="Cannot be divided by 0")
		else:
			res = float(val1/val2)
			result_label.config(text=res)


title_label = tkinter.Label(window, text="A very simple calculator", fg='blue', font='Helvetica 18')
title_label.grid(row=0, column=0, columnspan=2)

entry_A = tkinter.Entry(window)
entry_A.insert('0', '0')
entry_A.grid(row=1, column=0, columnspan=2)

operator_label = tkinter.Label(window, text="+")
operator_label.grid(row=2, column=0, columnspan=2, sticky='W')

entry_B = tkinter.Entry(window)
entry_B.insert('0', '0')
entry_B.grid(row=3, column=0, columnspan=2)

equals_label = tkinter.Label(window, text="=")
equals_label.grid(row=4, column=0, columnspan=2, sticky='W')

result_label = tkinter.Label(window, text="0")
result_label.grid(row=5, column=0, columnspan=2, sticky='W')

plus_btn = tkinter.Button(window, text="+", command=lambda: calc('+'))
plus_btn.grid(row=6, column=0, sticky='nesw')

minus_btn = tkinter.Button(window, text="-", command=lambda: calc('-'))
minus_btn.grid(row=6, column=1, sticky='nesw')

multiply_btn = tkinter.Button(window, text="*", command=lambda: calc('*'))
multiply_btn.grid(row=7, column=0, sticky='nesw')

divide_btn = tkinter.Button(window, text="/", command=lambda: calc('/'))
divide_btn.grid(row=7, column=1, sticky='nesw')


quit_btn = tkinter.Button(window, text="QUIT", command = close_window)
quit_btn.grid(row=8, column=0, columnspan=2)


window.mainloop()
