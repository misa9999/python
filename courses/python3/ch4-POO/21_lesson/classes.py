"""Description fast and simple.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam feugiat eu 
ipsum et pretium. Aenean ac pulvinar nunc. Nulla ut nisl magna. Etiam placerat
nisi a porttitor consectetur. Nunc vel lorem non quam gravida maximus. 
Vestibulum tellus massa, eleifend quis dui quis, ullamcorper feugiat purus. 
Sed enim diam, iaculis at sem nec, pretium suscipit nisi. Phasellus gravida 
odio quis varius laoreet. Nunc porta facilisis tellus eu malesuada. Etiam et 
porttitor turpis, sed consequat ante. Integer pellentesque lorem non nunc 
fermentum lacinia.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam feugiat eu 
ipsum et pretium. Aenean ac pulvinar nunc. Nulla ut nisl magna. Etiam placerat
nisi a porttitor consectetur. Nunc vel lorem non quam gravida maximus. 
Vestibulum tellus massa, eleifend quis dui quis, ullamcorper feugiat purus. 
Sed enim diam, iaculis at sem nec, pretium suscipit nisi. Phasellus gravida 
odio quis varius laoreet. Nunc porta facilisis tellus eu malesuada. Etiam et 
porttitor turpis, sed consequat ante. Integer pellentesque lorem non nunc 
fermentum lacinia.
"""


class MyClass:
    """Documentation normal

    description....
    """

    attribute1 = 1
    attribute2 = "Value"

    def __init__(self, text):
        """Start data

        :param text: class text
        :type text: str
        """
        self.text = text
        self.show_text(text)

    @staticmethod
    def show_text(text):
        """Method that displays 100-characters text on the screen

        :param text: 100-characters text
        :type text:  str

        :return: 100-characters text
        :rtype: str

        :raises ValueError: If text has more than 100 characters
        :raises TypeError:  If the text isn't a string
        """
        if not instance(text, str):
            raise TypeError("Text must be a string")

        if len(text) > 100:
            raise ValueError("Test must be 100 characters or less")

        return text
