// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let (mut prev, mut cur) = (None, head);

    while let Some(mut node) = cur {
        cur = node.next;
        node.next = prev;
        prev = Some(node);
    }

    prev
}

fn main() {
    println!("reverse-linked-list");
}