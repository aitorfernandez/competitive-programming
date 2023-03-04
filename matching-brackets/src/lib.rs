pub fn brackets_are_balanced(string: &str) -> bool {
    let mut stack = Vec::new();

    for c in string.chars() {
        match c {
            '[' | '{' | '(' => stack.push(c),
            ']' | '}' | ')' => {
                if let Some(last) = stack.pop() {
                    if (c == ']' && last != '[')
                        || (c == '}' && last != '{')
                        || (c == ')' && last != '(')
                    {
                        return false;
                    }
                } else {
                    return false;
                }
            }
            _ => continue,
        }
    }

    stack.is_empty()
}
