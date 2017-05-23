import color.Color;
import shapes.Shape;

/**
 * Created by mahmoud on 5/23/2017.
 */
public abstract class AbstractFactory {
    abstract Color getColor(String color);
    abstract Shape getShape(String shape) ;
}
