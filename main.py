from linkedlist import LinkedList as llist

if __name__ == "__main__":
    ll = llist()
    for i in range(1, 6):
        ll.push(i)
    ll.printnodes()
    ll.length()
    # llist.removeFirst()
    ll.pushAfter(3, 3.4)
    ll.printnodes()
    ll.length()

    ll.removeAfter(3)
    ll.printnodes()
    ll.length()
