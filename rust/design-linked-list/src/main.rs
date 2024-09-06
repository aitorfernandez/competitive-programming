struct Node {
    val: i32,
    next: Link,
}

type Link = Option<Box<Node>>;

struct MyLinkedList {
    head: Link,
    len: i32,
}

impl MyLinkedList {
    fn new() -> Self {
        Self { head: None, len: 0 }
    }

    fn get(&mut self, index: i32) -> i32 {
        if index >= self.len || index < 0 {
            return -1;
        }

        let mut cur = self.head.as_mut().unwrap();
        for _ in 0..index {
            cur = cur.next.as_mut().unwrap();
        }
        cur.val
    }

    fn add_at_head(&mut self, val: i32) {
        let new_node = Box::new(Node {
            val,
            next: self.head.take(),
        });

        self.head = Some(new_node);
        self.len += 1;
    }

    fn add_at_tail(&mut self, val: i32) {
        let new_tail = Box::new(Node { val, next: None });

        if self.head.is_none() {
            self.head = Some(new_tail);
        } else {
            let mut cur = self.head.as_mut().unwrap();
            while cur.next.is_some() {
                cur = cur.next.as_mut().unwrap();
            }

            cur.next = Some(new_tail);
        }

        self.len += 1;
    }

    fn add_at_index(&mut self, index: i32, val: i32) {
        if index > self.len || index < 0 {
            return;
        }

        match index {
            0 => self.add_at_head(val),
            index if index == self.len => self.add_at_tail(val),
            _ => {
                let mut cur = self.head.as_mut().unwrap();
                for _ in 0..(index - 1) {
                    cur = cur.next.as_mut().unwrap();
                }
                let next = cur.next.take();
                let new_node = Box::new(Node { val, next });
                cur.next = Some(new_node);

                self.len += 1;
            }
        }
    }

    fn delete_at_index(&mut self, index: i32) {
        if index >= self.len || index < 0 {
            return;
        }

        match index {
            0 => self.head = self.head.as_mut().unwrap().next.take(),
            _ => {
                let mut cur = self.head.as_mut().unwrap();
                for _ in 0..(index - 1) {
                    cur = cur.next.as_mut().unwrap();
                }

                let delete_node = cur.next.as_mut().unwrap();
                cur.next = delete_node.next.take();
            }
        }
        self.len -= 1;
    }

    fn display(&self) {
        let mut cur = &self.head;
        let mut i = 0;
        while let Some(node) = cur {
            println!("i: {} n: {}", i, node.val);
            cur = &node.next;
            i += 1;
        }
    }
}

fn main() {
    let mut l = MyLinkedList::new();

    l.add_at_head(1);
    l.delete_at_index(0);

    l.add_at_head(2);
    l.delete_at_index(1);

    l.add_at_head(3);
    l.add_at_head(4);
    l.add_at_head(5);

    l.add_at_index(4, 1);
    l.add_at_tail(0);

    let _ = l.get(2);

    l.delete_at_index(6);
    l.delete_at_index(4);

    l.display();
}
