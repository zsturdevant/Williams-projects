/* Uses the TwoPlayerGame interface to implement the
 * "Silver Dollar Game".
 */
import java.util.Random;
import java.util.Scanner;
import java.util.Vector;

public class CoinStrip implements TwoPlayerGame {
 
  // initilizes scanner, random, sets the max width of a strip to 25 before adding a new strip
  // initilizes the coin strip as an integer vector, and makes current player and numCoins variables
  public static final int MAX_WIDTH = 25;
  private Random r = new Random();
  private Scanner s = new Scanner(System.in);

  private int currentPlayer;
  private Vector<Integer> strip = new Vector<>(0);
  private int numCoins;
  
  // randomly chooses the number of coins based on user input
  public CoinStrip(int maxCoins) {
    if (maxCoins >= 1000) {
      numCoins = r.nextInt(3, 1000);
    } else {
      numCoins = r.nextInt(3, maxCoins + 1);
    }

    //sets variables to initial values
    currentPlayer = 0;
    int slot = 0;
    int coinNumber = 1;
    
    // randomly adds coins to strip until the number of coins is reached
    while (numCoins >= coinNumber) {
      int addCoin = r.nextInt(0, 2);
      for (int coin = 0; coin < addCoin; coin++) {
        addCoin = r.nextInt(0, 2);
        if (addCoin == 1) {
          strip.add(0);
          strip.add(slot, (coinNumber));
          slot = slot + 1;
          coinNumber = coinNumber + 1;
        } else {
          slot = slot + 1;
          strip.add(0);
        }
      }
    }
     strip.setSize(strip.indexOf(numCoins) + 1);
  }
    /**
   * Returns the current value for a given resource.
   *
   * @param resource Describes the game element.
   * @returns The current value of the resource.
   */
  public int getResource(int resource) {
   return strip.get(resource - 1);
  }
  
  /**
   * Sets the game state. Should not check whether the given
   * parameters are valid. isValidMove should be called before
   * calling this method to ensure that a move is legal.
   *
   * @param resource Which resource to alter (e.g., position, gamepiece, pile of matches, etc.)
   * @param updatedValue The updated value of the resource (e.g., how many matches remain, the updated position of a piece, etc.)
   */
  public void setResource(int resource, int updatedValue) {
    strip.setElementAt(resource, updatedValue);
  }
  
  /**
   * Returns the number representing the current player.
   * @returns The current player.
   */
  public int getPlayer() {
    return currentPlayer + 1;
  }
  
  /**
   * Changes the current player to the next player.
   * @param player A player number.
   */
  public void setPlayer(int player) {
    if (currentPlayer == 0) {
      currentPlayer = 1;
    } else {
      currentPlayer = 0;
    }
  }
  /** shortens length of vector to only show/store the necessary length to keep all coins on
   * the strip.
   */
  public void trimCoinStrip() {
    strip.setSize(strip.indexOf(numCoins) + 1);
  }

  /**
   * Returns true if the specification of a move describes a legal move
   * given all the rules of the game. Note: this does not check whether the
   * move is *good* move, only whether it is legal.
   *
   * @param coin Which resource to alter (e.g., position, gamepiece, pile of matches, etc.)
   * @param spacesToMove provides the number of spaces to check if the move is valid
   * @return True iff the move is valid.
   */
  public boolean isValidMove(int coin, int spacesToMove) {
    if (coin == 1) {
      return strip.indexOf(1) != 0 && spacesToMove >= 1;
    } else {
    return coin > 0 && coin <= numCoins && strip.indexOf(coin - 1)
    < strip.indexOf(coin) - spacesToMove && spacesToMove >= 1;
    }
  }
  
  /**
   * @returns True if the game is over, false otherwise.
   * checks that the numeric value of the last coin is equal to the size of the strip
   * proving that no more moves are possible
   */
  public boolean isGameOver() {
    return strip.lastElement() == strip.size();
  }
  
  /**
   * Displays the coinStrip on the screen.
   */
  public void displayBoard() {
    int numberOfSpaces = 0;
    int numberOfStrips = strip.size() / MAX_WIDTH;
    int remainder = strip.size() - (numberOfStrips * MAX_WIDTH);

    // print the first numberOfStrips complete strips of width MAX_WIDTH
    // to allow for games with up to 999 coins.

    for (int repeat = 0; repeat < numberOfStrips; repeat++) {

      for (int boardLength = 0; boardLength < MAX_WIDTH; boardLength++) {
        System.out.print("----");
      }

      System.out.println();
      System.out.print("|");

      for (int boardLength = 0; boardLength < MAX_WIDTH; boardLength++) {
        System.out.print("   |");
      }

      System.out.println();
  
      for (int c = 0; c < MAX_WIDTH; c++) {
        if (strip.get(numberOfSpaces) < 99) {
          System.out.print("| ");
        } else {
          System.out.print("|");
        }

        if (strip.get(numberOfSpaces) == 0) {
          System.out.print(" ");
        } else {
          System.out.print(strip.get(numberOfSpaces));
        }

        if (strip.get(numberOfSpaces) < 10) {
          System.out.print(" ");
          numberOfSpaces++;
        } else {
          System.out.print("");
          numberOfSpaces++;
        }
      }

      System.out.print("|");
      System.out.println();
      System.out.print("|");

      for (int boardLength = 0; boardLength < MAX_WIDTH; boardLength++) {
        System.out.print("   |");
      }

      System.out.println();

      for (int boardLength = 0; boardLength < MAX_WIDTH; boardLength++) {
        System.out.print("----");
      }

      System.out.println();
    }
    

    // print the last incomplete strip if it exists.
    if (remainder >= 1) {
    
      for (int boardLength = 0; boardLength < remainder; boardLength++) {
        System.out.print("----");
      }

      System.out.println();
      System.out.print("|");

      for (int boardLength = 0; boardLength < remainder; boardLength++) {
        System.out.print("   |");
      }

      System.out.println();
  
      for (int c = 0; c < remainder; c++) {
        if (strip.get(numberOfSpaces) < 99) {
          System.out.print("| ");
        } else {
          System.out.print("|");
        }

        if (strip.get(numberOfSpaces) == 0) {
          System.out.print(" ");
        } else {
          System.out.print(strip.get(numberOfSpaces));
        }

        if (strip.get(numberOfSpaces) < 10) {
          System.out.print(" ");
          numberOfSpaces++;
        } else {
          System.out.print("");
          numberOfSpaces++;
        }
      }
    
      System.out.print("|");
      System.out.println();
      System.out.print("|");

      for (int boardLength = 0; boardLength < remainder; boardLength++) {
        System.out.print("   |");
      }

      System.out.println();

      for (int boardLength = 0; boardLength < remainder; boardLength++) {
        System.out.print("----");
      }

      System.out.println();
    }
  }

  /** Prompts user to enter a coin and a number of spaces they wish to move the coin
   * to the left then verifies the move is valid, if the move is valid updates the coin
   * strip with the new positions of the coins.
   */
  public void takeATurn() {

    int coin = 0;

    int spaces = 0;

    System.out.print("Enter a coin and a number of spaces to move:");
    // asks user for coin input, if input is not valid prompts user for new input.
    try {
      coin = s.nextInt();
      spaces = s.nextInt();
    } catch (java.util.InputMismatchException e) {
      System.out.println("Please enter a valid coin and a positive integer.");
      s.next();
      takeATurn();
      return;
    }

    // if the move is valid update the coinStrip with position of the moved coin
    // and places 0 in its place.
    if (!isValidMove(coin, spaces)) {
      System.out.println("This is not a valid move.");
      takeATurn();
      return;
    } else {
      int temp = strip.indexOf(coin);
      strip.setElementAt(coin, (strip.indexOf(coin) - spaces));
      strip.setElementAt(0, temp);
    }
  }

  public static void main(String[] args) {
    // initilizes a coinStrip.
    CoinStrip st = new CoinStrip(Integer.parseInt(args[0]));

    // ensures the game has at least one legal move.
    while (st.isGameOver()) {
      st = new CoinStrip(Integer.parseInt(args[0]));
    }

    // display board and take turns until the game is over.
    while (!st.isGameOver()) {
      System.out.println("Player " + st.getPlayer() + ":");
      st.displayBoard();
      st.takeATurn();
      st.setPlayer(st.getPlayer());
      st.trimCoinStrip();
    }

    st.displayBoard();
    st.setPlayer(st.getPlayer());
    System.out.println("Player " + st.getPlayer() + " Wins!");
  }
}
