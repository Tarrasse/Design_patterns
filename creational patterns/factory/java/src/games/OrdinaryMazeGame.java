package games;

/**
 * Created by mahmoud on 5/23/2017.
 */
public class OrdinaryMazeGame extends MazeGame {

    public OrdinaryMazeGame() {
        setToPrint();
    }

    @Override
    protected void setToPrint() {
        toPrint = "this is a Ordinary Maze Game";
    }
}
