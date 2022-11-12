from LinkedList import LinkedList
# from LinkedList import Deque

# Create new thing for testing
list = LinkedList()
# queue = Deque()
# tempQueue = Deque()

# Add things to the list
# list.append("String 1")
# list.append("String 2")
# list.append("String 3")
# list.append("String 4")
# list.append("String 5")
# queue.enqueue("String 1")
# queue.enqueue("String 2")
# queue.enqueue("String 3")
# queue.enqueue("String 4")
# queue.enqueue("String 5")



# ====ITERATE BEFORE TESTING THE FUNCTIONS====

for i in list.iter():
    print(i)

# print('Size: ', queue.size)
# curr = queue.first
# while (curr is not None):
#     print(curr.data)
#     curr = curr.prev

# ------------------------------------------------

print('==============')

# ====REMOVELAST & REMOVEFIRST TESTS====
# print('removeLast: ', queue.removeLast())
# print('removeFirst: ', queue.removeFirst())

# ------------------------------------------------

# ====ADDFIRST & ADDLAST TESTS====
# queue.addFirst('New String')
# queue.addLast('New String')

# ------------------------------------------------

# ====CHARCOUNT TESTS====
# print("Run charCount Aggregated: ", list.charCount(aggregated=True))
# print("Run charCount Disaggregated: ", list.charCount())

# ------------------------------------------------

# ====REVERSED TESTS====
# oop_reversed_list = list.reverse()
list.reverse(in_place=True)

# ------------------------------------------------

print('==============')

# ====ITERATE AFTER RUNNING FUNCTIONS====
for i in list.iter():
    print(i)

# print('Size: ', queue.size)
# curr = queue.first
# while (curr is not None):
#     print(curr.data)
#     curr = curr.prev

# ====SPECIAL ITERATE FOR OUT OF PLACE REVERSED====
# for i in oop_reversed_list.iter():
#     print(i)
