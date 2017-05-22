package games;

/**
 * Created by mahmoud on 5/23/2017.
 */
public abstract class MazeGame {
    protected String toPrint = "";

    public MazeGame() {

    }

    abstract protected void setToPrint();

    @Override
    public String toString() {
        return toPrint;
    }
}
