use time::{Duration, PrimitiveDateTime as DateTime};

pub fn after(start: DateTime) -> DateTime {
    let x: i64 = 10;
    start + (Duration::seconds(x.pow(9)))
}
