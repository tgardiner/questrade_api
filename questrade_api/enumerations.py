from enum import Enum


class Currency(Enum):
    USD = 'USD'
    CAD = 'CAD'


class Exchange(Enum):
    TSX = 'TSX'
    TSXV = 'TSXV'
    CNSX = 'CNSX'
    MX = 'MX'
    NASDAQ = 'NASDAQ'
    NYSE = 'NYSE'
    AMEX = 'AMEX'
    ARCA = 'ARCA'
    OPRA = 'OPRA'
    PinkSheets = 'PinkSheets'
    OTCBB = 'OTCBB'


class AccountType(Enum):
    Cash = 'Cash'
    Margin = 'Margin'
    TFSA = 'TFSA'
    RRSP = 'RRSP'
    SRRSP = 'SRRSP'
    LRRSP = 'LRRSP'
    LIRA = 'LIRA'
    LIF = 'LIF'
    RIF = 'RIF'
    SRIF = 'SRIF'
    LRIF = 'LRIF'
    RRIF = 'RRIF'
    PRIF = 'PRIF'
    RESP = 'RESP'
    FRESP = 'FRESP'


class ClientAccountType(Enum):
    Individual = 'Individual'
    Joint = 'Joint'
    InformalTrust = 'InformalTrust'
    Corporation = 'Corporation'
    InvestmentClub = 'InvestmentClub'
    FormalTrust = 'FormalTrust'
    Partnership = 'Partnership'
    SoleProprietorship = 'SoleProprietorship'
    Family = 'Family'
    JointAndInformalTrust = 'JointAndInformalTrust'
    Institution = 'Institution'


class AccountStatus(Enum):
    Active = 'Active'
    SuspendedClosed = 'Suspended(Closed)'
    Suspended = 'Suspended(View Only)'
    LiquidateOnly = 'LiquidateOnly'
    Closed = 'Closed'


class TickType(Enum):
    Up = 'Up'
    Down = 'Down'
    Equal = 'Equal'


class OptionType(Enum):
    Call = 'Call'
    Put = 'Put'


class OptionDurationType(Enum):
    Weekly = 'Weekly'
    Monthly = 'Monthly'
    Quarterly = 'Quarterly'
    LEAP = 'LEAP'


class OptionExerciseType(Enum):
    American = 'American'
    European = 'European'


class SecurityType(Enum):
    Stock = 'Stock'
    Option = 'Option'
    Bond = 'Bond'
    Right = 'Right'
    Gold = 'Gold'
    MutualFund = 'MutualFund'
    Index = 'Index'


class OrderStateFilterType(Enum):
    All = 'All'
    Open = 'Open'
    Closed = 'Closed'


class OrderAction(Enum):
    Buy = 'Buy'
    Sell = 'Sell'


class OrderSide(Enum):
    Buy = 'Buy'
    Sell = 'Sell'
    Short = 'Short'
    Cov = 'Cov'
    BTO = 'BTO'
    STC = 'STC'
    STO = 'STO'
    BTC = 'BTC'


class OrderType(Enum):
    Market = 'Market'
    Limit = 'Limit'
    Stop = 'Stop'
    StopLimit = 'StopLimit'
    TrailStopInPercentage = 'TrailStopInPercentage'
    TrailStopInDollar = 'TrailStopInDollar'
    TrailStopLimitInPercentage = 'TrailStopLimitInPercentage'
    TrailStopLimitInDollar = 'TrailStopLimitInDollar'
    LimitOnOpen = 'LimitOnOpen'
    LimitOnClose = 'LimitOnClose'


class OrderTimeInForce(Enum):
    Day = 'Day'
    GoodTillCanceled = 'GoodTillCanceled'
    GoodTillExtendedDay = 'GoodTillExtendedDay'
    GoodTillDate = 'GoodTillDate'
    ImmediateOrCancel = 'ImmediateOrCancel'
    FillOrKill = 'FillOrKill'


class OrderState(Enum):
    Failed = 'Failed'
    Pending = 'Pending'
    Accepted = 'Accepted'
    Rejected = 'Rejected'
    CancelPending = 'CancelPending'
    Canceled = 'Canceled'
    PartialCanceled = 'PartialCanceled'
    Partial = 'Partial'
    Executed = 'Executed'
    ReplacePending = 'ReplacePending'
    Replaced = 'Replaced'
    Stopped = 'Stopped'
    Suspended = 'Suspended'
    Expired = 'Expired'
    Queued = 'Queued'
    Triggered = 'Triggered'
    Activated = 'Activated'
    PendingRiskReview = 'PendingRiskReview'
    ContingentOrder = 'ContingentOrder'


class HistoricalDataGranularity(Enum):
    OneMinute = 'OneMinute'
    TwoMinutes = 'TwoMinutes'
    ThreeMinutes = 'ThreeMinutes'
    FourMinutes = 'FourMinutes'
    FiveMinutes = 'FiveMinutes'
    TenMinutes = 'TenMinutes'
    FifteenMinutes = 'FifteenMinutes'
    TwentyMinutes = 'TwentyMinutes'
    HalfHour = 'HalfHour'
    OneHour = 'OneHour'
    TwoHours = 'TwoHours'
    FourHours = 'FourHours'
    OneDay = 'OneDay'
    OneWeek = 'OneWeek'
    OneMonth = 'OneMonth'
    OneYear = 'OneYear'


class OrderClass(Enum):
    Primary = 'Primary'
    Limit = 'Limit'
    StopLoss = 'StopLoss'


class StrategyTypes(Enum):
    CoveredCall = 'CoveredCall'
    MarriedPuts = 'MarriedPut'
    VerticalCallSpread = 'VerticalCall'
    VerticalPutSpread = 'VerticalPut'
    CalendarCallSpread = 'CalendarCall'
    CalendarPutSpread = 'CalendarPut'
    DiagonalCallSpread = 'DiagonalCall'
    DiagonalPutSpread = 'DiagonalPut'
    Collar = 'Collar'
    Straddle = 'Straddle'
    Strangle = 'Strangle'
    ButterflyCall = 'ButterflyCall'
    ButterflyPut = 'ButterflyPut'
    IronButterfly = 'IronButterfly'
    CondorCall = 'Condor'
    Custom = 'Custom'
