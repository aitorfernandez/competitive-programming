// use std::cmp::min;

fn max_area(height: Vec<i32>) -> i32 {
    let mut l = 0;
    let mut r = height.len() - 1;
    let mut area = 0;

    while r > l {
        // let total = (r - l) * min(height[l], height[r]) as usize;
        let total = (r - l) * height[l].min(height[r]) as usize;
        area = area.max(total);

        if height[l] < height[r] {
            l += 1;
        } else {
            r -= 1
        }
    }

    area as i32
}

fn main() {
    assert_eq!(max_area(vec![1, 8, 6, 2, 5, 4, 8, 3, 7]), 49);
}
