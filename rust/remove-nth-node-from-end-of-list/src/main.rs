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

fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
    let mut dummy = Box::new(ListNode {
        next: head.clone(),
        val: 0,
    });
    let (mut l, mut r, mut n) = (dummy.as_mut(), head, n);

    while n > 0 && r.is_some() {
        r = r.unwrap().next;
        n -= 1;
    }

    while let Some(node) = r {
        l = l.next.as_mut().unwrap();
        r = node.next;
    }

    l.next = l.next.take().unwrap().next.take();

    dummy.next
}

fn main() {
    println!("remove-nth-from-end");
}
