fn max_area(height: Vec<i32>) -> i32 {
    let (mut max_area, mut l, mut r) = (0, 0, height.len() - 1);

    while r > l {
        let area = (r - l) as i32 * height[l].min(height[r]);
        max_area = max_area.max(area);

        if height[l] < height[r] {
            l += 1;
        } else {
            r -= 1;
        }
    }

    max_area
}

fn main() {
    assert_eq!(max_area(vec![1, 8, 6, 2, 5, 4, 8, 3, 7]), 49);
    assert_eq!(max_area(vec![1, 1]), 1);
}
