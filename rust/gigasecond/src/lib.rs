// use std::time::Duration;
// use time::PrimitiveDateTime as DateTime;
use time::{Duration, PrimitiveDateTime as DateTime};

// Returns a DateTime one billion seconds after start.
pub fn after(start: DateTime) -> DateTime {
    // start + Duration::from_secs(1_000_000_000)

    // let s: u64 = 10;
    // start + Duration::from_secs(s.pow(9))

    let s: i64 = 10;
    start + Duration::seconds(s.pow(9))
}
