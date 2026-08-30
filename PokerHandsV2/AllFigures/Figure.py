from PokerHandsV2.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHandsV2.AllFigures.FullFigure import FullFigure
from PokerHandsV2.AllFigures.HighCardFigure import HighCardFigure
from PokerHandsV2.AllFigures.PairFigure import PairFigure
from PokerHandsV2.AllFigures.StraitFigure import StraitFigure
from PokerHandsV2.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHandsV2.AllFigures.TwoPairFigure import TwoPairFigure

Figure = HighCardFigure | PairFigure | TwoPairFigure | ThreeOfKindFigure | StraitFigure | FullFigure | FourOfKindFigure    