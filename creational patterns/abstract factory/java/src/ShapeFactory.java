import color.Color;
import shapes.Rectangle;
import shapes.Shape;
import shapes.Square;

/**
 * Created by mahmoud on 5/23/2017.
 */
public class ShapeFactory extends AbstractFactory {
    @Override
    Color getColor(String color) {
        return null;
    }

    @Override
    Shape getShape(String shape) {
        if (shape == null){
            return null;
        }

        if(shape.equalsIgnoreCase("RECTANGLE")){
            return new Rectangle();

        }else if(shape.equalsIgnoreCase("SQUARE")){
            return new Square();
        }

        return null;
    }
}
