from linked_list import LinkedList

def main():

    list = LinkedList()
    #print list.empty()
    #print list.front()
    #print list.back()
    #print list.size()
    list.push_back(2)
    #list.show()
    list.push_front(5)
    list.push_front(7)
    #list.show()
    list.push_front(10)
    list.push_back(15)
    #list.insert_at(5, 555)
    #print list.pop_front()
    #list.pop_back()
    #print list.front()
    #print list.back()
    list.show()
    #print list.size()
    #print list.value_at(2)
    #list.erase_at()
    #print list.value_from_end(1)
    list.show()

if __name__ == '__main__':
    main()
