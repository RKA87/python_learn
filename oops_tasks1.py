class Stack:
    
    def __init__(self,items):
        self.items=items

    def inserting_elements(self,item):
        return self.items.append(item)
    
    def pop_element(self):
        if self.items:
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        return self.items

items=['1','2','3', 'rk','4']

stack = Stack(items)
x=stack.display()
print(x)

insert_elemnt=5
stack.inserting_elements(insert_elemnt)


class Queue:

    def __init__(self):
        self.items=[]

    def enqueuing(self,item):
        self.items.append(item)

    def dequeuing(self):
        return self.items.pop(1)

items=['1','2','3','4','5']
q=Queue()
for item in items:
    q.enqueuing(item)

z=q.dequeuing()

print("enqueued:",q.items)

print("dequeued:",z)

class Str:

    def __init__(self):
        self.item=""
    
    def adding_string(self,word):
        self.item += word
    
    def is_al_num(self):
        return self.item.isalnum()

word="rakesh7891"
obj=Str()
obj.adding_string(word)
print(obj.item)

result=obj.is_al_num()
print(f"Is Given String is Alpha Numeric:{result}")
