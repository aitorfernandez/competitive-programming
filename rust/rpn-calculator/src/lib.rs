#[derive(Debug)]
pub enum CalculatorInput {
    Add,
    Subtract,
    Multiply,
    Divide,
    Value(i32),
}

pub fn evaluate(inputs: &[CalculatorInput]) -> Option<i32> {
    let mut stack: Vec<i32> = Vec::new();

    for i in inputs {
        use CalculatorInput::*;
        match i {
            Value(n) => stack.push(*n),
            Add => {
                let (b, a) = (stack.pop()?, stack.pop()?);
                stack.push(b + a);
            }
            Subtract => {
                let (b, a) = (stack.pop()?, stack.pop()?);
                stack.push(a - b);
            }
            Multiply => {
                let (b, a) = (stack.pop()?, stack.pop()?);
                stack.push(b * a);
            }
            Divide => {
                let (b, a) = (stack.pop()?, stack.pop()?);
                stack.push(a / b);
            }
        }
    }

    match stack.len() {
        1 => stack.pop(),
        _ => None,
    }
}
