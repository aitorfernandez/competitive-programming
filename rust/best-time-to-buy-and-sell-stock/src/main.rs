fn max_profit(prices: Vec<i32>) -> i32 {
    let (mut profit, mut l) = (0, 0);

    for r in 1..prices.len() {
        if prices[l] < prices[r] {
            profit = profit.max(prices[r] - prices[l]);
        } else {
            l = r;
        }
    }

    profit
}

fn main() {
    assert_eq!(max_profit(vec![7, 1, 5, 3, 6, 4]), 5);
    assert_eq!(max_profit(vec![7, 6, 4, 3, 1]), 0);
}
