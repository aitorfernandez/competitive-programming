use std::fmt;

const MINUTES_PER_HOUR: i64 = 60;
const MINUTES_PER_DAY: i64 = 24 * MINUTES_PER_HOUR;

#[derive(Debug, PartialEq)]
pub struct Clock(i64);

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "{:02}:{:02}",
            self.0 / MINUTES_PER_HOUR,
            self.0 % MINUTES_PER_HOUR
        )
    }
}

impl Clock {
    pub fn new(hours: i64, minutes: i64) -> Self {
        Self(
            (((hours * MINUTES_PER_HOUR + minutes) % MINUTES_PER_DAY) + MINUTES_PER_DAY)
                % MINUTES_PER_DAY,
        )
    }

    pub fn add_minutes(&self, minutes: i64) -> Self {
        Clock::new(0, self.0 + minutes)
    }
}
