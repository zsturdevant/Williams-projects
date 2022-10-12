/**
 * This file contains starter code for the Nim game.  We copied
 * over method names from the TwoPlayerGame interface and provided
 * just enough implementation so that the compiler can compile them
 * without producing any errors.  These implementations are not
 * correct, so you should replace them with real implementations.
 *
 * We also added an empty constructor, which you should implement.
 * 
 * A good place to start is by writing a main method...
 */
import java.util.Random;
import java.util.Scanner;

public class Nim implements TwoPlayerGame {
    
    //initilize scanner
    Scanner s = new Scanner(System.in);
    //initilize random
    Random r = new Random();

    //initialize a board
    int board[];

    //Initialize the current player
    int currentPlayer;

    /**
     * Initializes a new Nim board game.
     *
     * @param numPiles The number of matchstick piles.
     * @param minMatches The smallest number of matches per pile.
     * @param maxMatches The largest number of matches per pile.
     */
    public Nim(int numPiles, int minMatches, int maxMatches ) {
        // create a new board
        board = new int[numPiles];

        // initilize piles on the board
        for(int i = 0; i < board.length; i++){
            board[i] = r.nextInt(minMatches, maxMatches);
        }
        //sets current player to zero
        currentPlayer = 0;
    }
  
    /**
     * Returns the current value for a given resource.
     *
     * @param resource Describes the game element.
     * @returns The current value of the resource.
     */  
    public int getResource(int resource) {
        // returns the resource from nim 
        return board[resource - 1];
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

        board[resource - 1] = (board[resource -1] - updatedValue);

    }
    
    /**
     * Returns the number representing the current player.
     * 
     * @returns The current player.
     */
    public int getPlayer() {
        // returns the number of the player 
        return currentPlayer;
    }
    
    /**
     * Changes the current player to the given player.
     * 
     * @param player A player number.
     */
    public void setPlayer(int player) {
        // switches players.
        if (player == 0){
            currentPlayer = 1;
        }
        else{
            currentPlayer = 0;
        }


    }
    
    /**
     * Returns true if the specification of a move describes a legal move
     * given all the rules of the game. Note: this does not check whether the
     * move is *good* move, only whether it is legal.
     *
     * @param resource Which resource to alter (e.g., position, gamepiece, pile of matches, etc.)
     * @param matchesToRemove The updated value of the resource (e.g., how many matches remain, the updated position of a piece, etc.)
     * @return True iff the move is valid.
     */
    
    public boolean isValidMove(int resource, int matchesToRemove) {
        // checks to ensure a valid pile and non empty pile is selected,
        // the number of matches to remove is not 0 and that the number is 
        // not greater than the number of matches in the pile.

        return resource > 0 && resource <= board.length && getResource(resource)
             >= matchesToRemove && matchesToRemove > 0;
    }
    
    /**
     * Returns true if the game is over.
     * @returns True if the game is over, false otherwise.
     */
    public boolean isGameOver() {
        // checks each pile, if any pile has matches in it, returns false, else returns true.
        for(int i = 0; i < board.length; i++){
            if(board[i] != 0)
                return false;
        }
        return true;
    }
    
    /**
     * Displays the board on screen.
     */
    public void displayBoard() {
        //prints the number of the pile and a number of matches in that pile for each pile
        
        for(int i=0; i < board.length; i++){
            System.out.print((i+1)+")");

            for(int a = 0; a < board[i]; a++){
                System.out.print( "| ");
            }
            System.out.println();
        }
    }

    /**
     * The entry point to the program.  It currently ignores
     * the contents of the args array.
     * @param args
     */

     public void takeATurn() {
        // prompt player to select a pile
        System.out.print("Choose a pile:");
        int pile = 0;
        int amount = 0;
        // Checks if the input is an integer and ensures selected pile is not empty.
        if(s.hasNextInt()){
            pile = s.nextInt();
            if(!isValidMove(pile, 1)){
                System.out.println("This move is not valid.");
                takeATurn();
                return;
            }   
        }
        // If not an Int loops back to ask again.
        else{
            System.out.println("This was not a integer, please try again.");
            s.next();
            takeATurn();
            return;
        }
        //prompt player to enter a number of matches
        System.out.print("Choose a number of matches to remove [1-"+ board[pile-1] + "]:");
        if(s.hasNextInt()){
            amount = s.nextInt();
        }
        else{
            System.out.println("This was not a integer, please try again.");
            s.next();
            takeATurn();
            return;
        }
        // is move valid? if yes contine, if no print "this move is not valid" takeATurn
        if(!isValidMove(pile, amount)){
            System.out.println("This move is not valid.");
            takeATurn();
            return;
        }
        // If move is valid then update the selected pile with its new value.
        else{
            setResource(pile, amount);
        }
     }


    public static void main(String[] args) {
        
        // create a new Nim board with inputs from user
        Nim n = new Nim(Integer.parseInt(args[0]), Integer.parseInt(args[1]), Integer.parseInt(args[2]));
        
        // take turns until game is over
        
        while(!n.isGameOver()) {
            System.out.println("Player: " + (n.getPlayer() +1));
             n.displayBoard();
             n.takeATurn();
             n.setPlayer(n.getPlayer());

        }
        
        System.out.println("Player " + (n.getPlayer() +1) +" Wins!");
        
    }
  }
  