from linkedlist import *

#create Hashing Table
    #1using Direct Access Table
    #2using Array
    #3using LinkedList
    #4using Balance Binary Search Tree

#Avoid Collision
    #1 Chaining
    #2 OpenAddressing
        #2.1 Linear Probing
        #2.2 Quadratic Probing
        #2.3 Double Hashing

class IndexTable():
    def __init__(self, key=None, next=None, link=LinkedList()):
        self.key=key
        self.next=next
        self.link=link

class HashTable():
	def __init__(self):
		self.size=10
		self.indextable=IndexTable()
		self.ptr=IndexTable()

	def hash(self, key):
		hash=key%self.size
		return hash

	def len(self):
		count=0
		self.ptr = self.indextable
		while self.ptr and self.ptr.key!=None:
		    count+=1
		    self.ptr=self.ptr.next
		return count

	def sort(self):
		#insertion sort
		self.ptr = self.indextable
		while self.ptr.next:
		    if self.ptr.key>self.ptr.next.key:
		        self.ptr.key, self.ptr.link, self.ptr.next.key, self.ptr.next.link = self.ptr.next.key, self.ptr.next.link, self.ptr.key, self.ptr.link
		        self.ptr=self.indextable
		    else:
		        self.ptr=self.ptr.next

	def add(self, info, key):
		hash=self.hash(key)
		if self.len()==0:
		    self.indextable=IndexTable(key=hash, link=LinkedList(info=info), next=None)
		elif self.len()>0:
		    count=0
		    self.ptr=self.indextable
		    while self.ptr:
		        if self.ptr.key==hash:
		            break
		        self.ptr=self.ptr.next
		        count+=1
		    if count==self.len():
		        self.ptr=self.indextable
		        while self.ptr.next:
		            self.ptr=self.ptr.next
		        self.ptr.next=IndexTable(key=hash, link=LinkedList(info=info))
		    elif count<self.len():
		        i=0
		        self.ptr=self.indextable
		        while i<count:
		            self.ptr=self.ptr.next
		            i+=1
		        self.ptr.link.append(info=info)
		self.sort()
		self.ptr=self.indextable
		while self.ptr:
		    print("Index:", self.ptr.key, "-->> ", sep=" ", end="", flush=True)
		    self.ptr.link.show()
		    self.ptr=self.ptr.next

	def delete(self, key):
		count=0
		self.ptr=self.indextable
		hash=self.hash(key)
		while self.ptr:
			if self.ptr.key==hash:
				break
			self.ptr=self.ptr.next
			count+=1
		if self.len()==0:
			print('Index is out of bound.')
		else:
			if count==self.len():
				print('Index is out of bound.')
			elif count<self.len():
				if count==0: 
					if self.len()==1:
						self.indextable=IndexTable()
					else:
						self.indextable=self.indextable.next
				elif count>0:
					i=0
					self.ptr=self.indextable
					while i<count-1:
						self.ptr=self.ptr.next
						i+=1
					self.ptr.next=self.ptr.next.next



def main():
    hashtable=HashTable()
    process=True
    while process:
        choice=input('1:Add\n2:Delete\n3:Exit\nChoice: ')
        if choice=='1':
            hashtable.add(input('Value: '), int(input('Index: ')))
        elif choice=='2':
            hashtable.delete(int(input('Index: ')))
        elif choice=='3':
            process=False
        else:
            print('Invalid Input!')

if __name__ == '__main__':
    main()
