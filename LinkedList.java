/**
 * Implementation of lists, using doubly linked elements, and dummy nodes.
 * Starter class for "9.10 Laboratory: Lists with Dummy Nodes"
 * Please modify this code by following the directions in  on page 216 of
 * Java Structures sqrt(7) edition by Duane Bailey.
 */

import structure5.*;

import java.net.http.HttpHeaders;
import java.util.Iterator;

public class LinkedList<E> extends DoublyLinkedList<E> {

	// Use these variables inherited from DoublyLinkedList
	// Do not uncomment this!  Just use the variables as if they were uncommented
	/**
	* Number of elements within the list.
	*	protected int count;
	*/

	/**
	* Reference to head of the list.
	*
	protected DoublyLinkedNode<E> head;
	*/

	/**
	* Reference to tail of the list.
	*
	protected DoublyLinkedNode<E> tail;
	*/


	/**
	* Constructs an empty list.
	*
	* @post constructs an empty list
	*
	*/
	public LinkedList() {
		
		head = new DoublyLinkedNode<E>(null);
		tail = new DoublyLinkedNode<E>(null);
		count = 0;
		
		head.setNext(tail);
		tail.setPrevious(head);
	}

	/**
	* Determine the number of elements in the list.
	*
	* @post returns the number of elements in list
	*
	* @return The number of elements found in the list.
	* @big-o O(1) (referances are in constant time)
	*/
	public int size() {
		Assert.pre(count >= 0, "Count was negative.");
		return count;
	}

	/**
	* Determine if the list is empty.
	*
	* @post returns true iff the list has no elements.
	*
	* @return True iff list has no values.
	* @big-o O(1) (referances are in constant time)
	*/
	public boolean isEmpty() {
		return size() == 0;
	}

	/**
	* Remove all values from list.
	*
	* @post removes all the elements from the list
	* @big-o O(1) (creats new empty list and sets referances, all constant time)
	*/
	public void clear() {
		// Makes a new head and tail and points them at each other.
		head = new DoublyLinkedNode<E>(null);
		tail = new DoublyLinkedNode<E>(null);
		count = 0;
		
		head.setNext(tail);
		tail.setPrevious(head);

		Assert.post(isEmpty(), "list was not empty after clear.");
	}

	/**
	* A private routine to add an element after a node.
	* @param value the value to be added
	* @param previous the node the come before the one holding value
	* @post list contains a node following previous that contains value
	* @big-o O(1) (sets referances and adds new node, all constant time operations)
	*/
	protected void insertAfter(E value, DoublyLinkedNode<E> previous) {

		DoublyLinkedNode<E> before = previous;
		DoublyLinkedNode<E> after = previous.next();

		DoublyLinkedNode<E> newNode = new DoublyLinkedNode<E>(value, after, before);

		after.setPrevious(newNode);
		before.setNext(newNode);
		int check = count;
		count++;
		Assert.post(count == check + 1, "Count increased by more than one.");

	}

	/**
	* A private routine to remove a node.
	* @param node the node to be removed
	* @pre node is non null
	* @post node is removed from the list
	* @post returns the value of the node removed
	* @return the value of the node removed
	* @big-o O(1) (removes referances to node and changes referances and returns
	* all constant time operations)
	*/
	protected E remove(DoublyLinkedNode<E> node) {
		
		DoublyLinkedNode<E> before = node.previous();
		DoublyLinkedNode<E> after = node.next();
		
		// points before and after at eachother and points node at nothing.
		before.setNext(after);
		after.setPrevious(before);
		node.setNext(null);
		node.setPrevious(null);

		int check = count;
		count--;
		Assert.post(count == check - 1, "count was decreased by more than one.");

		return node.value();
	}


	/**
	* Add a value to the head of the list.
	*
	* @param value The value to be added.
	* @pre value is not null
	* @post adds element to head of list
	* @big-o O(1) (performs a constant time operation => constant time operation)
	*
	*/
	public void addFirst(E value) {
		// construct a new element, making it the first after the sentenal node.
		Assert.pre(value != null, "value was null.");

		insertAfter(value, head);

		Assert.post(head.next().value() == value, "value was not stored in first.");
	}


	/**
	* Add a value to the tail of the list.
	*
	* @param value The value to be added.
	* @pre value is not null
	* @post adds new value to tail of list
	* @big-o O(1) (performs a constant time operation => constant time operation)
	*/
	public void addLast(E value) {
		// Add a new element before the ending sentenal.
		Assert.pre(value != null, "value was null.");

		insertAfter(value, tail.previous());

		Assert.post(tail.previous().value() == value, "value was not stored in last.");
	}

	/**
	* Remove a value from the head of the list.
	* Value is returned.
	*
	* @pre list is not empty
	* @post removes first value from list
	*
	* @post Returns the value removed from the list.
	* @return The value removed from the list.
	* @big-o O(1) (performs two constant time operation => constant time operation)
	*/
	public E removeFirst() {
		// remove the first node in a list.
		Assert.pre(!isEmpty(), "List is empty.");

		return remove(head.next());
	}

	/**
	* Remove a value from the tail of the list.
	*
	* @pre list is not empty
	* @post removes value from tail of list
	* @post Returns the value removed from the list.
	*
	* @return The value removed from the list.
	* @big-o O(1) (performs two constant time operation => constant time operation)
	*/
	public E removeLast() {
		// removes the last value in the list.
		Assert.pre(!isEmpty(), "List is empty.");

		return remove(tail.previous());
	}

	/**
	* Get a copy of the first value found in the list.
	*
	* @pre list is not empty
	* @post returns first value in list.
	*
	* @return A reference to first value in list.
	* @big-o O(1) (performs two constant time operation => constant time operation)
	*/
	public E getFirst() {
		// returns the first value after the sentenal node.
		Assert.pre(size() > 0, "list is empty");

		return head.next().value();
	}

	/**
	* Get a copy of the last value found in the list.
	*
	* @pre list is not empty
	* @post returns last value in list.
	*
	* @return A reference to the last value in the list.
	* @big-o O(1) (performs two constant time operation => constant time operation)
	*/
	public E getLast() {
		// returns the first value before the ending sentenal node.
		Assert.pre(size() > 0, "list is empty");

		return tail.previous().value();
	}

	/**
	* Insert the value at location.
	*
	* @pre 0 <= i <= size()
	* @post adds the ith entry of the list to value o
	* @param i the index of this new value
	* @param o the the value to be stored
	* @big-o O(n) (loops, worst case inserts at the end of the list => O(n))
	*/
	public void add(int i, E o) {
		// loops until it reaches the node to add after, then adds the node as the next node.
		Assert.pre((0 <= i) && (i <= size()), "Index out of range.");

		DoublyLinkedNode<E> finger = head.next();

		for (int a = 0; a < i; a++) {
			finger = finger.next();
		}

		insertAfter(o, finger);
	}

	/**
	* Remove and return the value at location i.
	*
	* @pre 0 <= i < size()
	* @post removes and returns the object found at that location.
	*
	* @param i the position of the value to be retrieved.
	* @return the value retrieved from location i (returns null if i invalid)
	* @big-o O(n) (loops, worst case removes node the end of the list => O(n))
	*/
	public E remove(int i) {
		// navigates to index i and removes the element at i.
		Assert.pre(0 <= i && (i < size()), "Index out of range.");

		DoublyLinkedNode<E> finger = head.next();

		for (int a = 0; a < i; a++) {
			finger = finger.next();
		}

		Assert.post(finger.value() != null, "value to be removed was null");

		return remove(finger);
	}

	/**
	* Get the value at location i.
	*
	* @pre 0 <= i < size()
	* @post returns the object found at that location.
	*
	* @param i the position of the value to be retrieved.
	* @return the value retrieved from location i (returns null if i invalid)
	* @big-o O(n) (loops, worst case gets node at the end of the list => O(n))
	*/
	public E get(int i) {
		// loops over a list until the value in list element i is found and returns it.
		Assert.pre((0 <= i) && (i < size()), "Index out of range.");

		DoublyLinkedNode<E> finger = head.next();

		for (int a = 0; a < i; a++) {
			finger = finger.next();
		}

		return finger.value();
	}

	/**
	* Set the value stored at location i to object o, returning the old value.
	*
	* @pre 0 <= i < size()
	* @post sets the ith entry of the list to value o, returns the old value.
	* @param i the location of the entry to be changed.
	* @param o the new value
	* @return the former value of the ith entry of the list.
	* @big-o O(n) (loops, worst case sets at the end of the list => O(n))
	*/
	public E set(int i, E o) {
		// moves through the elements of a list and sets the node at index i to a given value.
		Assert.pre((0 <= i) && (i < size()), "Index out of range.");

		DoublyLinkedNode<E> finger = head.next();

		for (int a = 0; a < i; a++) {
			finger = finger.next();
		}

		//saves the old value for later returning
		E result = finger.value();

		//sets node to new value
		finger.setValue(o);

		return result;
	}

	/**
	* Determine the first location of a value in the list.
	*
	* @pre value is not null
	* @post returns the (0-origin) index of the value,
	*   or -1 if the value is not found
	*
	* @param value The value sought.
	* @return the index (0 is the first element) of the value, or -1
	* @big-o O(n) (loops, worst case value not in list => goes the end of the list => O(n))
	*/
	public int indexOf(E value) {
		// loops over the nodes of a list until finding the first node that matches value, then returns
		// an integer that corresponds to its location or -1 if not found.

		int i = 0;
		DoublyLinkedNode<E> finger = head.next();

		// search for value or end of list, counting along the way
		while (!(finger == tail) && !finger.value().equals(value)) {
			finger = finger.next();
			i++;
		}
		// Now finger points to value, i is index

		if (finger == tail) {
			// value not found, return indicator
			return -1;
		} else {
			// value found, return index
			Assert.post(i <= size(), "returned an index out of range.");
			return i;
		}
	}

	/**
	* Determine the last location of a value in the list.
	*
	* @pre value is not null
	* @post returns the (0-origin) index of the value,
	*   or -1 if the value is not found
	*
	* @param value the value sought.
	* @return the index (0 is the first element) of the value, or -1
	* @big-o O(n) (loops, worst case value not in list => goes to the begining of the list => O(n))
	*/
	public int lastIndexOf(E value) {
		// Starting at the end of the list moves through the nodes until it finds the last occurance
		// of a value, returns an int that corresponds to the index of that node.
		int i = size() - 1;

		DoublyLinkedNode<E> finger = tail.previous();

		// search for the last matching value, result is desired index
		while (!finger.value().equals(value) && (finger != head)) {
			finger = finger.previous();
			i--;
		}

		if (finger == head) {
			// value not found, return indicator
			return -1;
		} else {
			// value found, return index
			Assert.post(i <= size() - 1, "returned index larger than list.");
			return i;
		}
	}

	/**
	* Check to see if a value is within the list.
	*
	* @pre value not null
	* @post returns true iff value is in the list
	*
	* @param value A value to be found in the list.
	* @return True if value is in list.
	* @big-o O(n) (calls O(n) function => O(n))
	*/
	public boolean contains(E value) {
		// moves through each node in a list until it reaches a node containing the value, if no
		// such node exists it it returns false.

		int contains = indexOf(value);
		return contains != -1;
	}

	/**
	* Remove a value from the list.  At most one value is removed.
	* Any duplicates remain.  Because comparison is done with "equals,"
	* the actual value removed is returned for inspection.
	*
	* @pre value is not null.  List can be empty.
	* @post first element matching value is removed from list
	*
	* @param value The value to be removed.
	* @return The value actually removed.
	* @big-o O(n) (loops, worst case value at end of list => goes the end of the list => O(n))
	*/
	public E remove(E value) {
		// removes the first occurance of a value in the list.

		return remove(indexOf(value));
	}

	/**
	* Construct an iterator to traverse the list.
	*
	* @post returns iterator that allows the traversal of list.
	*
	* @return An iterator that traverses the list from head to tail.
	* @big-o O(1) (just a pointer so constant time)
	*/
	public Iterator<E> iterator() {
		/**
		 * into your list implementation, please toggle the
		 * comments below. To understand why the lines below
		 * must be swapped, please consult the structure5
		 * source code for DoublyLinkedListIterator class.
		 */

		return new DoublyLinkedListIterator<E>(head, tail);
	}

	/**
	* Construct a string representation of the list.
	*
	* @post returns a string representing list
	*
	* @return A string representing the elements of the list.
	* @big-o O(n) (loops, looking at each value in list not matter what => goess the end of the list
	* => O(n))
	*/
	public String toString() {
		StringBuffer s = new StringBuffer();
		s.append("<LinkedList (" + count + "):");

		Iterator<E> li = iterator();
		while (li.hasNext()) {
			E value = li.next();
			 if (value != null) {
				s.append(" " + value);
			 }
		}
		s.append(">");

		return s.toString();
	}
}
