#![allow(unused)]

/// various log levels
#[derive(Clone, PartialEq, Debug)]
pub enum LogLevel {
    Info,
    Warning,
    Error,
    Debug,
}
/// primary function for emitting logs
pub fn log(level: LogLevel, message: &str) -> String {
    let level = format!("{:?}", level);
    format!("[{}]: {}", level.to_uppercase(), message)

    // match level {
    //     LogLevel::Info => info(message),
    //     LogLevel::Warning => warn(message),
    //     LogLevel::Error => error(message),
    //     LogLevel::Debug => debug(message),
    // }
}
pub fn info(message: &str) -> String {
    // format!("[INFO]: {}", message)
    log(LogLevel::Info, message)
}

pub fn warn(message: &str) -> String {
    // format!("[WARNING]: {}", message)
    log(LogLevel::Warning, message)
}

pub fn error(message: &str) -> String {
    // format!("[ERROR]: {}", message)
    log(LogLevel::Error, message)
}

pub fn debug(message: &str) -> String {
    // format!("[DEBUG]: {}", message)
    log(LogLevel::Debug, message)
}
