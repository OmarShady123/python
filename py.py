#     multithreading
import time

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

arr = [2,3,8,9]

t = time.time()

calc_square(arr)
calc_cube(arr)


print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
print("#####################")

import time
import threading

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(0.2) #simulate an I/O-bound task

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
print("#################################")
import concurrent.futures

def worker():
	print("Worker thread running")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker) 
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")
print("#################################")


def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(1)
 

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(1)


arr = [2,3,8]

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(calc_square , arr) 
pool.submit(calc_cube , arr)

pool.shutdown(wait=True)

print("Main thread continuing to run")
print("#################################")



import threading 

# global variable x 
x = 0

def increment(): 
	""" 
	function to increment global variable x 
	"""
	global x 
	x += 1

def thread_task(): 
	""" 
	task for thread 
	calls increment function 1000 times. 
	"""
	for _ in range(100000): 
		increment() 

def main_task(): 
	global x 
	# setting global variable x as 0 
	x = 0

	# creating threads 
	t1 = threading.Thread(target=thread_task) 
	t2 = threading.Thread(target=thread_task) 

	# start threads 
	t1.start() 
	t2.start() 

	# wait until threads finish their job 
	t1.join() 
	t2.join() 

if __name__ == "__main__": 
	for i in range(10): 
		main_task() 
		print("Iteration {0}: x = {1}".format(i,x)) 
print("#################")

import threading 

# global variable x 
x = 0

def increment(): 
	""" 
	function to increment global variable x 
	"""
	global x 
	x += 1

def thread_task(lock): 
	""" 
	task for thread 
	calls increment function 100000 times. 
	"""
	for _ in range(100000): 
		lock.acquire() 
		increment() 
		lock.release() 

def main_task(): 
	global x 
	# setting global variable x as 0 
	x = 0

	# creating a lock 
	lock = threading.Lock() 

	# creating threads 
	t1 = threading.Thread(target=thread_task, args=(lock,)) 
	t2 = threading.Thread(target=thread_task, args=(lock,)) 

	# start threads 
	t1.start() 
	t2.start() 

	# wait until threads finish their job 
	t1.join() 
	t2.join() 

if __name__ == "__main__": 
	for i in range(10): 
		main_task() 
print("###########################")

#          Multiprocessing

import time
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))
        time.sleep(3)

def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*n*n))
        time.sleep(3)


if __name__ == "__main__":
    arr = [2,3,8]
    
    t = time.time()
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
  
     
    print("done in : ",time.time()-t)

    print("The number of CPU currently working in system : ", multiprocessing.cpu_count()) 
print("########################")

def worker1(): 
	# printing process id 
	print("ID of process running worker1: {}".format(os.getpid())) 

def worker2(): 
	# printing process id 
	print("ID of process running worker2: {}".format(os.getpid())) 

if __name__ == "__main__": 
	# printing main program process id 
	print("ID of main process: {}".format(os.getpid())) 

	# creating processes 
	p1 = multiprocessing.Process(target=worker1) 
	p2 = multiprocessing.Process(target=worker2) 

	# starting processes 
	p1.start() 
	p2.start() 

	# process IDs 
	print("ID of process p1: {}".format(p1.pid)) 
	print("ID of process p2: {}".format(p2.pid)) 

	# wait until processes are finished 
	p1.join() 
	p2.join() 

	# both processes finished 
	print("Both processes finished execution!") 

	# check if processes are alive 
	print("Process p1 is alive: {}".format(p1.is_alive())) 
	print("Process p2 is alive: {}".format(p2.is_alive())) 
print("##########################")
result = [] 

def square_list(mylist): 
	""" 
	function to square a given list 
	"""
	global result 
	# append squares of mylist to global list result 
	for num in mylist: 
		result.append(num * num) 
	# print global list result 
	print("Result(in process p1): {}".format(result)) 

if __name__ == "__main__": 
	# input list 
	mylist = [1,2,3,4] 

	# creating new process 
	p1 = multiprocessing.Process(target=square_list, args=(mylist,)) 
	# starting process 
	p1.start() 
	# wait until process is finished 
	p1.join() 

	# print global result list 
	print("Result(in main program): {}".format(result)) 
print("####################")


def square_list(mylist, result, square_sum): 
	""" 
	function to square a given list 
	"""
	# append squares of mylist to result array 
	for idx, num in enumerate(mylist): 
		result[idx] = num * num 

	# square_sum value 
	square_sum.value = sum(result) 

	# print result Array 
	print("Result(in process p1): {}".format(result[:])) 

	# print square_sum Value 
	print("Sum of squares(in process p1): {}".format(square_sum.value)) 

if __name__ == "__main__": 
	# input list 
	mylist = [1,2,3,4] 

	# creating Array of int data type with space for 4 integers 
	result = multiprocessing.Array('i', 4) 

	# creating Value of int data type 
	square_sum = multiprocessing.Value('i') 

	# creating new process 
	p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum)) 

	# starting process 
	p1.start() 

	# wait until the process is finished 
	p1.join() 

	# print result array 
	print("Result(in main program): {}".format(result[:])) 

	# print square_sum Value 
	print("Sum of squares(in main program): {}".format(square_sum.value)) 
import multiprocessing 

def square_list(mylist, q): 
	""" 
	function to square a given list 
	"""
	# append squares of mylist to queue 
	for num in mylist: 
		q.put(num * num) 

def print_queue(q): 
	""" 
	function to print queue elements 
	"""
	print("Queue elements:") 
	while not q.empty(): 
		print(q.get()) 
	print("Queue is now empty!") 

if __name__ == "__main__": 
	# input list 
	mylist = [1,2,3,4] 

	# creating multiprocessing Queue 
	q = multiprocessing.Queue() 

	# creating new processes 
	p1 = multiprocessing.Process(target=square_list, args=(mylist, q)) 
	p2 = multiprocessing.Process(target=print_queue, args=(q,)) 

	# running process p1 to square list 
	p1.start() 
	p1.join() 

	# running process p2 to get queue elements 
	p2.start() 
	p2.join() 
print("###########################")


def sender(conn, msgs): 
	""" 
	function to send messages to other end of pipe 
	"""
	for msg in msgs: 
		conn.send(msg) 
		print("Sent the message: {}".format(msg)) 
	conn.close() 

def receiver(conn): 
	""" 
	function to print the messages received from other 
	end of pipe 
	"""
	while 1: 
		msg = conn.recv() 
		if msg == "END": 
			break
		print("Received the message: {}".format(msg)) 

if __name__ == "__main__": 
	# messages to be sent 
	msgs = ["hello", "hey", "hru?", "END"] 

	# creating a pipe 
	parent_conn, child_conn = multiprocessing.Pipe() 

	# creating new processes 
	p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs)) 
	p2 = multiprocessing.Process(target=receiver, args=(child_conn,)) 

	# running processes 
	p1.start() 
	p2.start() 

	# wait until processes finish 
	p1.join() 
	p2.join() 
print("#######################")


#                      Socket programming

# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b"Hello, world.... sent by client")

#receive data from server and print it
data = s.recv(1024)
print(f"Received {data!r}")
print("######################")

import socket			 

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind((HOST, PORT))
s.listen()

	 
print ("socket binded to %s" %(PORT)) 

print ("socket is listening....")		 

# a forever loop until we interrupt it or 
# an error occurs 
while True: 

    # Establish connection with client. 
    con, addr = s.accept()	 
    print ('Got connection from', addr )

    # send a thank you message to the client. encoding to send byte type. 
    con.send(b"Thank you for connecting...sent by server")

    #receive data from client and print it
    data = con.recv(1024) 
    print(f"Received {data!r}")

    # Close the connection with the client 
    con.close()

    # Breaking once connection closed
    break
print("########################")

import socket # for socket 
import sys 

try: 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	print ("Socket successfully created")
except socket.error as err: 
	print ("socket creation failed with error %s" %(err))

# default port for socket 
port = 80

try: 
	host_ip = socket.gethostbyname('www.google.com') 
except socket.gaierror: 

	# this means could not resolve the host 
	print ("there was an error resolving the host")
	sys.exit() 

# connecting to the server 
s.connect((host_ip, port)) 

print ("the socket has successfully connected to google") 
print (host_ip)

print("#############################")

#                            Design pattern

"""Facade pattern with an example of WashingMachine"""

class Washing: 
	'''Subsystem # 1'''

	def wash(self): 
		print("Washing...") 


class Rinsing: 
	'''Subsystem # 2'''

	def rinse(self): 
		print("Rinsing...") 


class Spinning: 
	'''Subsystem # 3'''

	def spin(self): 
		print("Spinning...") 


class WashingMachine: 
	'''Facade'''

	def __init__(self): 
		self.washing = Washing() 
		self.rinsing = Rinsing() 
		self.spinning = Spinning() 

	def startWashing(self): 
		self.washing.wash() 
		self.rinsing.rinse() 
		self.spinning.spin() 

""" main method """
if __name__ == "__main__": 

	washingMachine = WashingMachine() 
	washingMachine.startWashing() 
print("#########################")

# flyweight
class ComplexCars(object):
    
	"""Separate class for Complex Cars"""

	def __init__(self):

		pass

	def cars(self, car_name):

		return "ComplexPattern[% s]" % (car_name)


class CarFamilies(object):

	"""dictionary to store ids of the car"""

	car_family = {}

	def __new__(cls, name, car_family_id):
 
		try:
			obj = cls.car_family[car_family_id]
            
		except KeyError:
			obj = object.__new__(cls)
			cls.car_family[car_family_id] = obj
		return obj

	def set_car_info(self, car_info):

		"""set the car information"""

		cg = ComplexCars()
		self.car_info = cg.cars(car_info)

	def get_car_info(self):

		"""return the car information"""

		return (self.car_info)



if __name__ == '__main__':
	car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferrari'), ('b', 1, 'Audia'))
	car_family_objects = []
	for i in car_data:
		obj = CarFamilies(i[0], i[1])
		obj.set_car_info(i[2])
		car_family_objects.append(obj)


	"""similar id's says that they are same objects """

	for i in car_family_objects:
		print("id = " + str(id(i)))
		print(i.get_car_info())
print("#############################")
class ConcreteProductA():
    "A Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductA"



class ConcreteProductB():
    "A Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductB"



class ConcreteProductC():
    "A Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductC"



class Creator:
    "The Factory Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None

# The Client
PRODUCT = Creator.create_object('b')
print(PRODUCT.name)
print("#########################")


from abc import ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):
    "The Builder Interface"

    @staticmethod
    @abstractmethod
    def build_part_a():
        "Build part a"

    @staticmethod
    @abstractmethod
    def build_part_b():
        "Build part b"

    @staticmethod
    @abstractmethod
    def build_part_c():
        "Build part c"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"

class Builder(IBuilder):
    "The Concrete Builder."

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('a')
        return self

    def build_part_b(self):
        self.product.parts.append('b')
        return self

    def build_part_c(self):
        self.product.parts.append('c')
        return self

    def get_result(self):
        return self.product

class Product():
    "The Product"

    def __init__(self):
        self.parts = []

class Director:
    "The Director, building a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return Builder()\
            .build_part_a()\
            .build_part_b()\
            .build_part_c()\
            .get_result()

# The Client
PRODUCT = Director.construct()
print(PRODUCT.parts)
print("#########################")



import copy

class Singleton():
    "The Singleton Class"
    value = []

    def __new__(cls):
        return cls #override the classes __new__ method to return a reference to itself
        #return object.__new__(cls) #what would be the out? and why?

    # def __init__(self):
    #     print("in init")

    @staticmethod
    def static_method():
        "Use @staticmethod if no inner variables required"

    @classmethod
    def class_method(cls):
        "Use @classmethod to access class level variables"
        print(cls.value)

# The Client
# All uses of singleton point to the same memory address (id)
print(f"id(Singleton)\t= {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT3)\t= {id(OBJECT3)}")
print("###################")

class Memento:
    
	"""Constructor function"""
	def __init__(self, file, content):

		"""put all your file content here"""
		
		self.file = file     
		self.content = content
        
  
        

"""It's a File Writing Utility"""

class X:

	"""Constructor Function"""

	def __init__(self, file_path):

		"""store the input file data"""
		self.file = file_path
		self.content = ""

	"""Append the data into content attr"""

	def write(self, string):
		self.content += string

	"""save the data into the Memento"""

	def save(self):
		return Memento(self.file, self.content)

	"""UNDO feature provided"""

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class Y:

	"""saves the data"""

	def save(self, x):
		self.mem = x.save()

	"""undo the content"""

	def undo(self, x):
		x.undo(self.mem)


if __name__ == '__main__':

	"""create the caretaker object"""
	y = Y()

	"""create the writer object"""
	x = X("GFG.txt")   #file = object , content = ""

	"""write data into file using writer object"""
	x.write("First vision of Data\n")   #file = object , content = "First vision of Data \n"
	print(x.content + "\n\n")


	"""save the file"""
	y.save(x) # Memento file = object , content = "First vision of Data \n"

	"""again write using the writer """
	x.write("Second vision of Data\n")  #file = object , content = "First vision of Data \n Second vision of Data"

	print(x.content + "\n\n")

	"""undo the file"""
	y.undo(x)

	print(x.content + "\n\n")  #file = object , content = "First vision of Data "
	