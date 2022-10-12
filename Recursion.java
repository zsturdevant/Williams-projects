/*
 * Recursion.java
 *
 * Starter code for the recursion lab.
 *
 */
import structure5.*;
import java.util.Arrays;


public class Recursion {

  // Note: Warmup questions are not graded, but you may wish to
  // complete & test them since later, graded questions build
  // on them.

  /***** Warmup 0.1 ********************************************/

  /**
   * Takes a non-negative integer and returns the sum of its digits.
   * @param n a non-negative integer.
   * @return the sum of n's digits
   * @pre n greater than or equal to zero
   * @post n was shorter than all of its digits
   */


  public static int digitSum(int n) {
    Assert.pre(n >= 0, "n was less than 0.");
    //uses integer division to determine when the last digit is reached and returns it.
    if (n / 10 == 0) {
      return n;
    } else {
      int divided = n / 10;
      Assert.post(n > divided, "n was shorter than the sum of its digits");
      //uses modular division to return the remainder if divided by ten added to the rest of the digits.
      return n % 10 + digitSum(n / 10);
    }
    
  }

  /***** Warmup 0.2 ********************************************/

  /** Takes an int array and adds the numbers to find the sum.
   *
   * @param int []
   * @return the sum of the integers in the array
   */

  public static int sumArray(int[]numList) {
    int sum = 0;

    //adds each position in the array to the other positions. returns the sum.
    for (int position = 0; position < numList.length; position++) {
      sum = sum + numList[position];
    }
    return sum;
  }

 /** Adds a new element to and array, adds one new slot to the end and puts the new item in the slot.
   *
   * @param int [] the origional array of numbers
   * @param int the new number to add to the array
   * @return returns the new array for use in the future.
   * @pre new number < max int
   * @post new list is not longer than the old list.
   */
  public static int[] addToSoFar(int[] numList, int newNum) {
    Assert.pre(newNum < Integer.MAX_VALUE, "New num was > max value of an int.");
    // makes a new int array one longer than the previous
    int[] newList = new int[(numList.length + 1)];

    // fills the new array with the existing arrays information.
    for (int i = 0; i < numList.length; i++) {
      newList[i] = numList[i];
    }

    // adds the new element to the new array in the last space, then returns the new array.
    newList[numList.length] = newNum;
    Assert.post(newList.length > numList.length, "Failed to add new number to soFar.");
    return newList;
  }

  /** helper method to determine what subsequeces of an interger array add up to
   * returns true if a sum can be made with the integers.
   *
   * @param numbers and array oof integers
   * @param targetSum the integer target to try and sum to
   * @param soFar an array of the ints in each subset of the calls of sumHelper so far
   * @return true if the sum can be made by any subset.
   *
   * @pre ensures we are not removing too many positions
   * @post ensures the array is getting shorter with each run.
   */
  public static boolean sumHelper(int[] numbers, int targetSum, int[] soFar) {
    
    int last = numbers.length - 1;
    //when all numbers have been looked at, determines what subsets add up to target sum
    if (numbers.length == 0) {
      return sumArray(soFar) == targetSum;
      }

    Assert.pre(last > -1, "Last position was negative.");
    // takes the old array and removes the last element
    int[] newNumbers = Arrays.copyOf(numbers, last);

    Assert.post(newNumbers.length < numbers.length, "Array was not getting shorter.");

    // makes all possible subsets from an array of numbers
    boolean answer = sumHelper(newNumbers, targetSum, addToSoFar(soFar, numbers[last]));
    boolean answerTwo = sumHelper(newNumbers, targetSum, soFar);
    
    //returns true if any subsets add up to the target.
    return answer || answerTwo;
    
  }

  /**
   * Given a set of integers and a target number, determines
   * whethere there is a subset of those numbers that sum to the
   * target number.
   *
   * @param setOfNums a set of numbers that may appear in the subset
   * @param targetSum the target value for the subset
   * @return true if some subset of numbers in setOfNums sums to targetSum
   * @pre in the helper method
   * @post in the helper method
   */
  
  public static boolean canMakeSum(int[] setOfNums, int targetSum) {

    int[] newList = new int[0];
    return sumHelper(setOfNums, targetSum, newList);
  }


  /*****  1  ***************************************************/

  /**
   * Return number of cannoballs in pyramid with the given `height`.
   *
   * @param height the height of the cannonball tower
   * @return the number of cannonballs in the entire tower
   * @pre Height must be a positive number
   * @post ensures height is going down and is not negative.
   */
  public static int countCannonballs(int height) {
    Assert.pre(height > 0, "Height was a negative number");

    if (height == 1) {
      return 1;
    } else {

      Assert.post(height > height - 1, "Height was increasing");
      Assert.post(height > 0, "Height less than 1");

      return height + countCannonballs(height - 1);
    }
  }


  /*****  2  ***************************************************/

 /**
   * A method that determines if a string reads the same forwards
   * and backwards.
   *
   * @param str the string to check
   * @return true if `str` is a palindrome.
   * @pre the String does not have negative length.
   * @post ensures the length of the string is getting shorter each time
   */
  public static boolean isPalindrome(String str) {
    
    //if the length of a string is 0 or 1 then it was a palendrome
    Assert.pre(str.length() > -1, "String had negative length.");
    if (str.length() <= 1) {
      return true;
    }
    //checks to see if the first and last character of a string are the same, then if they are
    //removes them and sends the new string to be checked. If not returns false.
    if (str.charAt(0) == str.charAt(str.length() - 1)) {
      String newString = str.substring(1, str.length() - 1);

      Assert.post(newString.length() < str.length(), "Did not reduce length of string.");
      return isPalindrome(newString);

    } else {
      return false;
    }
  }

  /*****  3  ***************************************************/
  
  /** A helper method for finding the next closing paren, bracket,
   * or brace in a sequence.
   * @param str
   * @return an int that is the location of the character.
   * @pre ensure the string has at least one bracket paren or brace in it
   * @post prevents a negative number from being returned
   */
  protected static int findCloseing(String str) {
    Assert.pre(str.contains("(") || str.contains(")") || str.contains("[") || str.contains("]")
      || str.contains("{") || str.contains("}"), "String does not contain any parens, brackets or braces.");
    Character d = '}';
    Character e = ')';
    Character f = ']';
    int n = str.length();
    // checks each character in a string to find the first character in d, e, or f and returns that
    // position.
    for (int i = 0; i < str.length(); i++) {
      if (str.charAt(i) == d && n > i) {
        n = i;
      }
      if (str.charAt(i) == e && n > i) {
        n = i;
      }
      if (str.charAt(i) == f && n > i) {
        n = i;
      }
      Assert.post(n >= 0, "Position cannot be negative");
    }
    return n;
  }

  /** Helper method used to check if Checks whether the bracket before a closing
   * paren, bracket, or brace is of the same type.
   *
   * @param second the closing paren, bracket, or brace.
   * @param first the character before second.
   * @return true if the character second character matches with the first, else false.
   */

  protected static boolean checkMatch(Character second, Character first) {
    Character a = '{';
    Character b = '(';
    Character c = '[';
    Character d = '}';
    Character e = ')';
    Character f = ']';
    if (second == d && first == a) {
      return true;
    }
    if (second == e && first == b) {
      return true;
    } else {
      return second == f && first == c;
    }
  }

  /**
   * Takes a string and removes two elements at index skipFirst and skipSecond from the string, returns the new string.
   *
   * @param str initial string containing two elements to remove
   * @param int the start of the new string (if you want to start at the 3rd letter put 2)
   * @param int the first element to remove
   * @param int the second element to remove
   * @return a string removing the undesired elements from the old string
   *
   * @pre makes sure the starting point is valid
   * @post makes sure the new string is shorter than the old string
   */
  protected static String makeString(String str, int start, int skipFirst, int skipSecond) {
    Assert.pre(start <= str.length(), "Starting point must be in string.");
    String newStr = "";

    // loops over characters in a string, skipping two that are desired to be skipped.
    for (int i = start; i < str.length(); i++) {
      if (i != skipFirst && i != skipSecond) {
        newStr = newStr + str.charAt(i);
      }
    }
    Assert.post(str.length() > newStr.length(), "New string was longer than old string.");
    return newStr;
  }


  /**
   * Checks whether `str` is a string of properly nested and matched
   * parens, brackets, and braces.
   *
   * @param str a string of parens, brackets, and braces.
   * @return true if str is properly nested and matched.
   * @pre ensures the length is valid
   * @post the length of the new string is shorter than the length of the origional string.
   */

  public static boolean isBalanced(String str) {
  
    Character first = str.charAt(0);
    Character second = str.charAt(1);
    int len = str.length();
    String newStr = "";
    Assert.pre(len >= 0, "Length is invalid.");
    
    // checks to ensure the string is not an odd number of digits
    if (len % 2 == 1) {
      return false;
    }
    // if the length of the string is zero or the final two characters in the string are a match
    // returns true
    if ((len == 0) || (len == 2 && checkMatch(second, first))) {
      return true;
    }

    int nextClose = findCloseing(str);
    int beforeClose = nextClose - 1;
    Character nextClosingCharacter = str.charAt(nextClose);
    Character oneBeforeClose = str.charAt(nextClose - 1);

    // Checks to ensure there is a match then removes the matching characters and sends a new
    // string to be checked.
    if (checkMatch(nextClosingCharacter, oneBeforeClose)) {
      newStr = makeString(str, 0, nextClose, beforeClose);
      Assert.post(str.length() > newStr.length(), "New string was longer than origional string.");
    } else {
      return false;
    }

    return isBalanced(newStr);
  }

  /*****  4  ***************************************************/

  /**
   * A method to print all subsequences of str (order does not matter).
   *
   * @param str string to print all subsequences of
   * @pre in helper
   * @post in helper
   */
  
  public static void subsequences(String str) {
    subsequenceHelper(str, ", ");
  }

  /**
   * Helper method for subsequences method
   * `soFar` keeps track of the characters currently in the substring
   *   being built
   * @param str hold the parts of the string that still need to be subsequenced.
   * @param soFar holds all the subsequences that have been completed.
   * @pre ensures the string is getting shorter with each pass
   * @post make sure soFar is working.
   */
  protected static void subsequenceHelper(String str, String soFar) {

    //when all sets have been made, prints out all subsets.
    if (str == "") {
      System.out.print(soFar);

    } else {
      String newString = str.substring(1);
      Assert.pre(newString.length() < str.length(), "Strings were not getting shorter with each pass.");

      // makes all possible subsets from a string
      subsequenceHelper(newString, soFar + str.charAt(0));
      subsequenceHelper(newString, soFar);
      Assert.post(soFar.length() >= 0, "So far was negative long?");
    }

  }

  /*****  5  ***************************************************/

  /**
   * A method to print the binary digits of a number.
   *
   * @param number the number to print in binary
   * @pre ensures input is positive
   * @post makes sure the binary representation of the number is longer than the number.
   */
  public static void printInBinary(int number) {
    Assert.pre(number >= 0, "input was negative");

    String binary = binaryConversion(number);

    Assert.post(binary.length() >= String.valueOf(number).length(), "Binary representation was shorter than numeric representation of number.");
    
    System.out.print(binary);
  }

  /** A helper method that converts an integer number into its binary form and returns it as a string.
   * @param number
   * @return a string that represents the number in binary.
   * @pre ensures the input is positive.
   * @post makes sure the binary representation of the number is longer than the number.
   */
  protected static String binaryConversion(int number) {
    Assert.pre(number >= 0, "Number given was negative.");

    //returns zero or one as needed.
    if (number == 0) {
      return "0";
    }
    if (number == 1) {
      return "1";
    } else {

      //determines the binary representation of the number and returns it as a string.
      String binary = binaryConversion(number / 2) + binaryConversion(number % 2);
      Assert.post(binary.length() >= String.valueOf(number).length(), "Binary representation was shorter than numeric representation of number.");
      return binary;
    }
  }


  /*****  6a  ***************************************************/

  /** helper method to determine what subsequeces of an interger array add up to a given sum
   * returns true if a sum can be made with the integers and prints all subsets that can be used
   * to make that sum.
   * @param numbers an array of integers
   * @param targetSum the integer target to try and sum to
   * @param soFar an array that contains all the integers in each group for later summing
   * @return true if the sum can be made by any subset.
   * @pre ensures last is never negative
   * @post ensures the new string is shorter than the old string
   */
  public static boolean sumHelperPrinter(int[] numbers, int targetSum, int[] soFar) {
    int last = numbers.length - 1;

    // when all numbers have been looked at, determines what subsets add up to target sum
    // and prints them out.
    if (numbers.length == 0) {
      if (sumArray(soFar) == targetSum) {
        System.out.println(Arrays.toString(soFar));
        return true;
        } else {
        return false;
        }
    }
    Assert.pre(last > -1, "Last position was negative.");

    // takes the old array and removes the last element
    int[] newNumbers = Arrays.copyOf(numbers, last);
    Assert.post(newNumbers.length < numbers.length, "Array was not getting shorter.");

    // makes all possible subsets from an array of numbers
    boolean answer = sumHelperPrinter(newNumbers, targetSum, addToSoFar(soFar, numbers[last]));
    boolean answerTwo = sumHelperPrinter(newNumbers, targetSum, soFar);
    
    // returns true if any subsets add up to the target.
    return answer || answerTwo;
    
  }

  /**
   * Return whether a subset of the numbers in nums add up to sum,
   * and print them out.
   *
   * @param nums [fill this in]
   * @param targetSum [fill this in]
   * @return [fill this in]
   * @pre in helper
   * @post inhelper
   */
  public static boolean printSubsetSum(int[] nums, int targetSum) {
    int[] newList = new int[0];
    return sumHelperPrinter(nums, targetSum, newList);
  }

  /*****  6b  ***************************************************/
  /**
   * the number of solutions tracked for the helper counter.
   */
  protected static int numberOfSolutions;

  /** helper method to determine what subsequeces of an interger array add up to a given sum
   * returns true if a sum can be made with the integers and prints all subsets that can be used
   * to make that sum.
   * @param numbers an array of integers
   * @param targetSum the integer target to try and sum to
   * @param soFar an array that contains all the integers in each group for later summing
   * @pre ensures last position is not negative
   * @post ensures the arrays are getting shorter
   */
  public static void sumHelperCounter(int[] numbers, int targetSum, int[] soFar) {
    int last = numbers.length - 1;

    // when all numbers have been looked at, determines what subsets add up
    // to target sum and for each one increases count by one
    if (numbers.length == 0 && (sumArray(soFar) == targetSum)) {
        numberOfSolutions = numberOfSolutions + 1;
    }
   
    // takes the old array and removes the last element if it has length > 0
    if (numbers.length > 0) {
      Assert.pre(last > -1, "Last position was negative.");
      int[] newNumbers = Arrays.copyOf(numbers, last);
      Assert.post(newNumbers.length < numbers.length, "Array was not getting shorter.");

      // makes all possible subsets from an array of numbers
      sumHelperCounter(newNumbers, targetSum, addToSoFar(soFar, numbers[last]));
      sumHelperCounter(newNumbers, targetSum, soFar);
     }
  }

  /**
   * Return the number of different ways elements in nums can be
   * added together to equal sum (you do not need to print them all).
   *
   * @param nums an array of integers to check and see what combinations can sum to a target
   * @param targetSum the number you wish to add all numbers to
   * @return how many different solutions exist.
   * @pre in helper
   * @post ensures the number of solutions is positive
   */
  public static int countSubsetSumSolutions(int[] nums, int targetSum) {
    int[] newList = new int[0];
    numberOfSolutions = 0;
    sumHelperCounter(nums, targetSum, newList);
    Assert.post(numberOfSolutions >= 0, "number of solutions cannot be negative.");
    return numberOfSolutions;

  }


  /***********************************************************/

  /**
   * Add testing code to main to demonstrate that each of your
   * recursive methods works properly.
   *
   * Think about the so-called corner cases!
   *
   * Remember the informal contract we are making: as long as all
   * predconditions are met, a method should return with all
   * postconditions met.
   */

  protected static void testCannonballs() {
    System.out.println("Testing cannonballs: ....");
    System.out.println(countCannonballs(3));
    System.out.println(countCannonballs(10));
  }

  protected static void testPalindrome() {
    System.out.println("Testing isPalindrome: ....");
    System.out.println(isPalindrome("mom"));
    System.out.println(isPalindrome("deeded"));
    System.out.println(isPalindrome("ablewasIereIsawelba"));
  }

  protected static void testBalanced() {
    System.out.println("Testing isBalanced: ....");
    System.out.println(isBalanced("[{[()()]}]"));
    System.out.println(isBalanced("[{[()()]}][{[()()]}]"));
    System.out.println(isBalanced("[{[()()]}{]{[()()]}]"));
  }

  protected static void testSubsequence() {
    System.out.println("Testing subsequences: ....");
    subsequences("abc");
    System.out.println();
    subsequences("CSCI136");
    System.out.println();
    subsequences("a");
    System.out.println();
    subsequences("");
    System.out.println();
  }

  protected static void testBinary() {
    System.out.println("Testing printInBinary: ....");
    printInBinary(0);
    System.out.println();
    printInBinary(30);
    System.out.println();
    printInBinary(1);
    System.out.println();
    printInBinary(110);
    System.out.println();
    printInBinary(2048);
    System.out.println();
    printInBinary(43);
    System.out.println();
      }

  protected static void testCanMakeSum() {
    System.out.println("Testing canMakeSum: ....");
    int[] numSet = {2, 5, 7, 12, 16, 21, 30};
    System.out.println(canMakeSum(numSet, 21));
    System.out.println(canMakeSum(numSet, 22));
    System.out.println(canMakeSum(numSet, 3));
    System.out.println(canMakeSum(numSet, 30));
  }

  protected static void testPrintSubsetSum() {
    System.out.println("Testing printSubsetSum: ....");
    int[] numSet = {2, 5, 7, 12, 16, 21, 30};
    System.out.println(printSubsetSum(numSet, 21));
    System.out.println(printSubsetSum(numSet, 22));
    System.out.println(printSubsetSum(numSet, 3));
    System.out.println(printSubsetSum(numSet, 30));
  }

  protected static void testCountSubsetSum() {
    System.out.println("Testing countSubsetSumSolutions: ....");
    int[] numSet = {2, 5, 7, 12, 16, 21, 30};
    System.out.println(countSubsetSumSolutions(numSet, 21));
    System.out.println(countSubsetSumSolutions(numSet, 22));
    System.out.println(countSubsetSumSolutions(numSet, 3));
    System.out.println(countSubsetSumSolutions(numSet, 30));
  }

  /**
   * Main method that calls testing methods to verify
   * the functionality of each lab exercise.
   *
   * Please supplement the testing code with additional
   * correctness tests as needed.
   */
  public static void main(String[] args) {

    System.out.println(digitSum(123458));
    System.out.println(digitSum(1234580));
    System.out.println(digitSum(10230458));
    testCannonballs();
    testPalindrome();
    testBalanced();
    testSubsequence();
    testBinary();
    testCanMakeSum();
    testPrintSubsetSum();
    testCountSubsetSum();

  }
}
