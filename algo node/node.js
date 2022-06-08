///class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}


class SLList{
    constructor(){
        this.head = null
    }

    addToFront(value) {
        let newNode = new Node (value)
        if(!this.head){
            this.head = newNode
            this.tail = this.head
        } 
        else {
            this.tail.next = newNode
            this.tail= newNode
        }
        this.length++
        return this
    }

    // given a value, add it to the back of your singly linked list
    // what if the list is empty?

    addToBack(value) {
        let newNode = new SinglyLinkedListNode(data)
    if (!head) {
        head = newNode 
        return head
    }
    let current  = head
    while (current.next) {
        current = current.next
    }
    current.next = newNode
    return head
        
        return this
    }



    printValues() {
        // step #0 [EDGE CASE]) handle a case where there is nothing in the list
        if(this.head == null){
            console.log("There's nothing in the list! Dummy!")
            // return 'this' to end function and allow chaining of methods
            return this
        }
        //step #1) establish a runner to traverse through the list
        var runner = this.head;

        // NOTE: we can move runner all the way into null because our loop will exit as soon as runner hits null, avoiding any errors with printing
        while(runner != null) {
            // step #2) print the values at each iteration before moving the runner!
            console.log(The current value is: ${runner.value})
            runner = runner.next
        }
        console.log("We have hit the end of the list!")
        // return 'this' to end function and allow chaining of methods
        return this
    }
}

const sll = new SLList();
sll.addToFront(-3)
sll.addToFront(-122)
sll.addToFront(41)
sll.addToBack(48)
sll.addToBack(-5)
sll.printValues()///