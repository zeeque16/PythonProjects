# Complete code
import sys
import datetime

# List out options in the ToDo list
def help():
	sa = """Usage :-
$ ./todo add "todo item" # Add a new todo
$ ./todo ls			 # Show remaining todos
$ ./todo del NUMBER	 # Delete a todo
$ ./todo done NUMBER	 # Complete a todo
$ ./todo help			 # Show usage"""
	sys.stdout.buffer.write(sa.encode('utf8'))

# Add new items to list
def add(s):
	f = open('todo.txt', 'a')		# Opens files
	f.write(s)						# Writes it to the file
	f.write("\n")					# Adds a line break
	f.close()						# Closes the file
	s = '"'+s+'"'
	print(f"Added todo: {s}")

# List out all the items in the Todo List
def ls():
	try:

		nec()
		l = len(d)
		k = l

		for i in d:										# Prints out all the items in the list from the nec() function
			sys.stdout.buffer.write(f"[{l}] {d[l]}".encode('utf8'))
			sys.stdout.buffer.write("\n".encode('utf8'))
			l = l-1

	except Exception as e:
		raise e

# Delete item from todo list
def deL(no):
	try:
		no = int(no)									# Totals number of items in the list
		nec()
		with open("todo.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)
			for i in lines:
				if (i.strip('\n') != d[no]):
					f.write(i)
			f.truncate()
		print(f"Deleted todo #{no}")

	except Exception as e:
		print(f"Error: todo #{no} does not exist. Nothing deleted.")

# check off items from the todo list
def done(no):
	try:

		nec()
		no = int(no)
		f = open('done.txt', 'a')
		st = 'x '+str(datetime.datetime.today()).split()[0]+' '+d[no]
		f.write(st)
		f.write("\n")
		f.close()
		print(f"Marked todo #{no} as done.")
		
		with open("todo.txt", "r+") as f:				# Checks and writes back the items into the file
			lines = f.readlines()
			f.seek(0)
			for i in lines:
				if (i.strip('\n') != d[no]):
					f.write(i)
			f.truncate()
	except:
		print(f"Error: todo #{no} does not exist.")

# A function used to add the lists in the text file
def nec():
	try:
		f = open('todo.txt', 'r')
		c = 1
		for line in f:
			line = line.strip('\n')
			d.update({c: line})
			c = c+1
	except:
		sys.stdout.buffer.write("There are no pending todos!".encode('utf8'))


if __name__ == '__main__':
	try:
		d = {}
		don = {}
		args = sys.argv
		if(args[1] == 'del'):
			args[1] = 'deL'
		if(args[1] == 'add' and len(args[2:]) == 0):
			sys.stdout.buffer.write(
				"Error: Missing todo string. Nothing added!".encode('utf8'))

		elif(args[1] == 'done' and len(args[2:]) == 0):
			sys.stdout.buffer.write(
				"Error: Missing NUMBER for marking todo as done.".encode('utf8'))

		elif(args[1] == 'deL' and len(args[2:]) == 0):
			sys.stdout.buffer.write(
				"Error: Missing NUMBER for deleting todo.".encode('utf8'))
		else:
			globals()[args[1]](*args[2:])

	except Exception as e:

		s = """Usage :-
$ ./todo add "todo item" # Add a new todo
$ ./todo ls			 # Show remaining todos
$ ./todo del NUMBER	 # Delete a todo
$ ./todo done NUMBER	 # Complete a todo
$ ./todo help			 # Show usage"""
		sys.stdout.buffer.write(s.encode('utf8'))
