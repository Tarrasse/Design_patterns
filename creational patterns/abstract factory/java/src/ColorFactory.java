import color.Color;
import color.Green;
import color.Red;
import shapes.Shape;

/**
 * Created by mahmoud on 5/23/2017.
 */
public class ColorFactory extends AbstractFactory {

    @Override
    public Shape getShape(String shapeType){
        return null;
    }

    @Override
    Color getColor(String color) {

        if(color == null){
            return null;
        }

        if(color.equalsIgnoreCase("RED")){
            return new Red();

        }else if(color.equalsIgnoreCase("GREEN"))
            return new Green();



        return null;
    }
}
