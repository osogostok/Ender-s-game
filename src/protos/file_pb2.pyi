from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Coordinates(_message.Message):
    __slots__ = ["pos"]
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, pos: _Optional[_Iterable[float]] = ...) -> None: ...

class Ship(_message.Message):
    __slots__ = ["alignment", "name", "length", "class_ship", "size", "armed", "oficer"]
    class AlignmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        Ally: _ClassVar[Ship.AlignmentType]
        Enemy: _ClassVar[Ship.AlignmentType]
    Ally: Ship.AlignmentType
    Enemy: Ship.AlignmentType
    class ClassShipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        Corvette: _ClassVar[Ship.ClassShipType]
        Frigate: _ClassVar[Ship.ClassShipType]
        Cruiser: _ClassVar[Ship.ClassShipType]
        Destroyer: _ClassVar[Ship.ClassShipType]
        Carrier: _ClassVar[Ship.ClassShipType]
        Dreadnought: _ClassVar[Ship.ClassShipType]
    Corvette: Ship.ClassShipType
    Frigate: Ship.ClassShipType
    Cruiser: Ship.ClassShipType
    Destroyer: Ship.ClassShipType
    Carrier: Ship.ClassShipType
    Dreadnought: Ship.ClassShipType
    class OficerType(_message.Message):
        __slots__ = ["first_name", "second_name", "rank"]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        SECOND_NAME_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        first_name: str
        second_name: str
        rank: str
        def __init__(self, first_name: _Optional[str] = ..., second_name: _Optional[str] = ..., rank: _Optional[str] = ...) -> None: ...
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    CLASS_SHIP_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ARMED_FIELD_NUMBER: _ClassVar[int]
    OFICER_FIELD_NUMBER: _ClassVar[int]
    alignment: Ship.AlignmentType
    name: str
    length: float
    class_ship: Ship.ClassShipType
    size: int
    armed: bool
    oficer: _containers.RepeatedCompositeFieldContainer[Ship.OficerType]
    def __init__(self, alignment: _Optional[_Union[Ship.AlignmentType, str]] = ..., name: _Optional[str] = ..., length: _Optional[float] = ..., class_ship: _Optional[_Union[Ship.ClassShipType, str]] = ..., size: _Optional[int] = ..., armed: bool = ..., oficer: _Optional[_Iterable[_Union[Ship.OficerType, _Mapping]]] = ...) -> None: ...

class Ships(_message.Message):
    __slots__ = ["ship"]
    SHIP_FIELD_NUMBER: _ClassVar[int]
    ship: _containers.RepeatedCompositeFieldContainer[Ship]
    def __init__(self, ship: _Optional[_Iterable[_Union[Ship, _Mapping]]] = ...) -> None: ...
