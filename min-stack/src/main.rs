struct MinStack {
    values: Vec<i32>,
    min_values: Vec<i32>,
}

impl MinStack {
    fn new() -> Self {
        Self {
            values: vec![],
            min_values: vec![],
        }
    }

    fn push(&mut self, val: i32) {
        self.values.push(val);

        if self.min_values.len() == 0 {
            self.min_values.push(val);
        } else {
            let min = val.min(self.min_values[self.min_values.len() - 1]);
            self.min_values.push(min);
        }
    }

    fn pop(&mut self) {
        self.values.pop();
        self.min_values.pop();
    }

    fn top(&self) -> i32 {
        self.values[self.values.len() - 1]
    }

    fn get_min(&self) -> i32 {
        self.min_values[self.min_values.len() - 1]
    }
}

fn main() {
    println!("Hello, world!");
}
