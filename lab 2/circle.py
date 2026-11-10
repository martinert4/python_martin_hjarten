# Bibliotek 
import math


# klass cirkel 
class Circle:
    def __init__(self, x: float = 0, y: float = 0, radius: float =0 ) -> None:
        """Initierar cirkelns centrum och radie. Ger TypeError vid fel typ.
                Ger ValueError om radien är negativt """
        if not isinstance(x, (int, float)):
            raise TypeError('x must be a number')
        self.x = x

        if not isinstance(y, (int, float)):
            raise TypeError('y must be a number')
        self.y = y
        
        if not isinstance(radius, (int, float)):
            raise TypeError('Radius must be a number')
        
        if radius < 0:
            raise ValueError('Wrong value - radius cant have a negative value')
        self.r = radius
        

    
    # Metoder för utskrift  
    def __str__(self) -> str:
        """Dunder string (str) används för utskrift för användaren tex print(c1) """
        return f'Circle with center ({self.x}, {self.y}) and radius {self.r}'
        
    def __repr__(self) -> str:
        """ Dunder repper (repr) används för  utskrift för utvecklaren. Nu går det printa genom bara skriva tex c1 i notebookcell"""
        return f'Circle(x={self.x}, y={self.y}, radius= {self.r})'    


    
    # Metoder för beräkna area och omkrets
    @property 
    def area(self) -> float:
        """ Beräknar area"""
        return self.r**2 * math.pi

    @property
    def perimeter(self) -> float:
        """ Beräknar omkrets"""
        return self.r * 2 * math.pi
        # @property låter oss läsa c1.area utan parenteser. 
        # Utan setter är egenskapen skrivskyddad. 

    
    
    # Metod för att flytta cirklens centrum
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



    # Metod för att kontrollera om det är en enhetscirkel
    def unit_circle(self) -> bool:
        """ Kontroll: är det en enhetscirkel? (radie=1 och centrum i origo) """
        if self.r == 1 and self.x == 0 and self.y == 0:
            return True
        else:
            return False



    # Metod för att kontroller om två cirklar har samma radie
    def __eq__(self, other) -> bool:
        """ Kontroll 1: Är "other" en cirkel. Kontroll 2: Har cirklarna samma radie.  """
        if isinstance(other, Circle) and self.r == other.r:
            return True
        else:
            return False



    # Metoder för att jämföra arean mellan två cirklar    
    def __lt__(self, other) -> bool:
        """ Kontroll 1: Är "other" en cirkel. Kontroll 2: är cirkel_1 < cirkel_2 """
        if isinstance(other, Circle) and self.area < other.area:
            return True
        else:
            return False

    def __le__(self, other) -> bool:
        """ Kontroll 1: Är "other" en cirkel. Kontroll 2: är cirkel_1 <= cirkel_2 """
        if isinstance(other, Circle) and self.area <= other.area:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        """ Kontroll 1: Är "other" en cirkel. Kontroll 2: är cirkel_1 > cirkel_2 """
        if isinstance(other, Circle) and self.area > other.area:
            return True
        else:
            return False
    
    def __ge__(self, other) -> bool:
        """ Kontroll 1: Är "other" en cirkel. Kontroll 2: är cirkel_1 >= cirkel_2 """
        if isinstance(other, Circle) and self.area >= other.area:
            return True
        else:
            return False