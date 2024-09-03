fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut numbers = nums.clone();
    numbers.sort_by(|a, b| a.cmp(&b));

    let mut res = vec![];

    for i in 0..numbers.len() {
        if i > 0 && numbers[i] == numbers[i - 1] {
            continue;
        }

        let (mut l, mut r) = (i + 1, numbers.len() - 1);

        while r > l {
            let sum = numbers[i] + numbers[l] + numbers[r];

            if sum == 0 {
                res.push(vec![numbers[i], numbers[l], numbers[r]]);

                l += 1;
                while numbers[l] == numbers[l - 1] && l < r {
                    l += 1;
                }
                r -= 1;
                while numbers[r] == numbers[r + 1] && l < r {
                    r -= 1;
                }
            } else if sum > 0 {
                r -= 1;
            } else {
                l += 1;
            }
        }
    }

    res
}

fn main() {
    assert_eq!(
        three_sum(vec![-1, 0, 1, 2, -1, -4]),
        vec![vec![-1, -1, 2], vec![-1, 0, 1]]
    );

    assert_eq!(three_sum(vec![0, 0, 0]), vec![vec![0, 0, 0]]);
    assert_eq!(three_sum(vec![0, 0, 0, 0]), vec![vec![0, 0, 0]]);
}
