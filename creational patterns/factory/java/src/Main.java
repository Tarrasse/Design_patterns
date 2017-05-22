import games.MagicMazeGame;
import games.MazeGame;
import games.OrdinaryMazeGame;

/**
 * Created by mahmoud on 5/23/2017.
 */
public class Main {
    public static void main(String[] args) {
        MazeGame ordinaryMazeGame = new OrdinaryMazeGame();
        MazeGame magicMazeGame = new MagicMazeGame();

        System.out.println(ordinaryMazeGame);
        System.out.println(magicMazeGame);
    }
}
