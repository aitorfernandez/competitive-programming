#![allow(unused)]

pub fn divmod(dividend: i16, divisor: i16) -> (i16, i16) {
    let quotient = dividend / divisor;
    let remainder = dividend % divisor;
    (quotient, remainder)
}

pub fn evens<T>(iter: impl Iterator<Item = T>) -> impl Iterator<Item = T> {
    // iter.step_by(2)
    // or
    iter.enumerate().filter(|(i, _)| i % 2 == 0).map(|(_, v)| v)

    // unimplemented!("implement `fn evens`");
    // it's only necessary to allow this function to compile
    // before implement.
    // std::iter::empty()
}

pub struct Position(pub i16, pub i16);
impl Position {
    pub fn manhattan(&self) -> i16 {
        self.0.abs() + self.1.abs()
    }
}
