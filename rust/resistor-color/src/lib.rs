use enum_iterator::IntoEnumIterator;
use int_enum::IntEnum;

#[repr(usize)]
#[derive(Clone, Copy, Debug, Eq, PartialEq, IntEnum, IntoEnumIterator)]
pub enum ResistorColor {
    Black = 0,
    Brown = 1,
    Red = 2,
    Orange = 3,
    Yellow = 4,
    Green = 5,
    Blue = 6,
    Violet = 7,
    Grey = 8,
    White = 9,
}

pub fn color_to_value(color: ResistorColor) -> usize {
    color.int_value()
}

pub fn value_to_color_string(value: usize) -> String {
    // Option
    // let resistor = ResistorColor::into_enum_iter().find(|r| color_to_value(r.clone()) == value);
    // match resistor {
    //     Some(r) => format!("{:?}", r),
    //     None => format!("value out of range"),
    // }

    // Result
    match ResistorColor::from_int(value) {
        Ok(r) => format!("{:?}", r),
        Err(_) => format!("value out of range"),
    }
}

pub fn colors() -> Vec<ResistorColor> {
    ResistorColor::into_enum_iter().collect::<Vec<_>>()
}
