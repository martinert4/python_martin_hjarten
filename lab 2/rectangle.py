# klass Rektangel 
class Rectangle:
   
    def __init__(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0 ) -> None:
        """Initierar rektanglens centrum samt bredd och höjd. Ger TypeError vid fel typ.
           Ger ValueError om bredd eller höjd är negativt """

        # Rektanglens x-koordinat och y-koordinat (centrum) 
        if not isinstance(x, (int, float)):
            raise TypeError('x must be a number')
        self.x = x
        
        if not isinstance(y, (int, float)):
            raise TypeError('y must be a number')
        self.y = y

        # Rektanglens bredd
        if not isinstance(width, (int, float)):
            raise TypeError('Width must be a number')
        if width < 0:
            raise ValueError('Wrong value - width cant have a negative value')
        self.w = width

        # Rektanglens höjd
        if not isinstance(height, (int, float)):
            raise TypeError('Height must be a number')
        if height < 0:
            raise ValueError('Wrong value - height cant have a negative value')
        self.h = height



    # Metoder för utskrift  
    def __str__(self) -> str:
        """Dunder string (str) används för utskrift för användaren tex print(r1) """
        return f'Rectangle with center at ({self.x}, {self.y}) with width {self.w} and height {self.h}'

    def __repr__(self) -> str:
        """ Dunder repper (repr) används för  utskrift för utvecklaren. Nu går det printa genom bara skriva tex r1 i notebookcell"""
        return f'Rectangle(x={self.x}, y={self.y}, width= {self.w}, height= {self.h})'        


    
    # Metoder för beräkna area och omkrets
    @property 
    def area(self) -> float:
        """ Beräknar area"""
        return self.w * self.h

    @property
    def perimeter(self) -> float:
        """ Beräknar omkrets"""
        return 2 * (self.w + self.h)
        # @property låter oss läsa c1.area utan parenteser. 
        # Utan setter är egenskapen skrivskyddad. 

    # Metod för att kontrollera om det är en kvadrat
    def square(self) -> bool:
        """ Kontroll: är det en kvadrat """
        if self.w == self.h:
            return True
        else:
            return False


    # Metod för att flytta rektangelns centrum
    def translate(self, horisontal: float = 0, vertical: float =0 ) -> None:
        # Type hints: här visas att startvärdet 0 och parametrarna förväntas vara tal och metoden returnerar inget värde.
        """Flyttar centrum med angivna avstånd i x- och y-led.
        Ger TypeError om något av avstånden inte är ett tal.
        """
        
        if not isinstance(horisontal, (int, float)):
            raise TypeError('dx must be a number')

        if not isinstance(vertical, (int, float)):
            raise TypeError('dy must be a number')

        self.x = self.x + horisontal
        self.y = self.y + vertical


    # Metod för att kontroller om två rektanglar har samma bredd och höjd
    def __eq__(self, other) -> bool:
        """ Kontroll 1: Är "other" en rektangel. Kontroll 2: Har rektanglar samma bredd och höjd """
        if isinstance(other, Rectangle) and self.w == other.w and self.h == other.h:
            return True
        else:
            return False


    # Metoder för att jämföra arean mellan två rektanglar    
    def __lt__(self, other) -> bool:
        """ Jämför om rektangeln har mindre area än den andra"""
        if isinstance(other, Rectangle) and self.area < other.area:
            return True
        else:
            return False

    def __le__(self, other) -> bool:
        """ Jämför om rektangelns area är mindre eller lika med arean av den andra rektangeln """
        if isinstance(other, Rectangle) and self.area <= other.area:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        """ Jämför om rektangelns area är större än arean av den andra rektangeln"""
        if isinstance(other, Rectangle) and self.area > other.area:
            return True
        else:
            return False

    def __ge__(self, other) -> bool:
        """ Jämför om rektangelns area är större eller lika med arean av den andra rektangeln  """
        if isinstance(other, Rectangle) and self.area >= other.area:
            return True
        else:
            return False