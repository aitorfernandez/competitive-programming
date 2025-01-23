use std::vec;

struct MinStack {
    stack: Vec<i32>,
    min_stack: Vec<i32>,
}

#[allow(dead_code)]
impl MinStack {
    fn new() -> Self {
        Self {
            stack: vec![],
            min_stack: vec![],
        }
    }

    fn push(&mut self, val: i32) {
        self.stack.push(val);

        if self.min_stack.is_empty() {
            self.min_stack.push(val);
        } else {
            let val = self.min_stack[self.min_stack.len() - 1].min(val);
            self.min_stack.push(val);
        }
    }

    fn pop(&mut self) {
        self.stack.pop();
        self.min_stack.pop();
    }

    fn top(&self) -> i32 {
        self.stack.last().cloned().unwrap_or(-1)

        // if self.stack.len() > 1 {
        //     self.stack[self.stack.len() - 1]
        // } else {
        //     -1
        // }
    }

    fn get_min(&self) -> i32 {
        self.min_stack.last().cloned().unwrap_or(-1)
    }
}

fn main() {}
