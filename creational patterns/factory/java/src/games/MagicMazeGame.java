package games;

/**
 * Created by mahmoud on 5/23/2017.
 */
public class MagicMazeGame extends MazeGame {

    public MagicMazeGame() {
        setToPrint();
    }

    @Override
    protected void setToPrint() {
        toPrint = "this is a magic Maze Game";
    }
}
