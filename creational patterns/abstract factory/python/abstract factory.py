class TextView:
    def __init__(self):
        pass


class ImageView:
    def __init__(self):
        pass


class BigTextView(TextView):
    def __init__(self):
        TextView.__init__(self)
        self.width = 50
        self.height = 50


class SmallTextView(TextView):
    def __init__(self):
        TextView.__init__(self)
        self.width = 10
        self.height = 10


class BigImageView(ImageView):
    def __init__(self):
        ImageView.__init__(self)
        self.width = 50
        self.height = 50


class SmallImageView(ImageView):
    def __init__(self):
        ImageView.__init__(self)
        self.width = 10
        self.height = 10


class UIFactory:
    def __init__(self):
        pass

    def getBigView(self): pass

    def getSmallView(self): pass


class ImageViewFactory(UIFactory):
    def __init__(self):
        UIFactory.__init__(self)

    def getBigView(self):
        return BigImageView()

    def getSmallView(self):
        return SmallImageView()


class TextViewFactory(UIFactory):
    def __init__(self):
        UIFactory.__init__(self)

    def getSmallView(self):
        return SmallTextView()

    def getBigView(self):
        return BigTextView()


def main():
    image_factory = ImageViewFactory()
    text_factory = TextViewFactory()

    big_text_view = text_factory.getBigView()
    small_text_View = text_factory.getSmallView()

    big_image_view = image_factory.getBigView()
    small_image_view = image_factory.getSmallView()


if __name__ == '__main__':
    main()
