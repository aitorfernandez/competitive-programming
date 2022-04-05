pub fn factors(mut n: u64) -> Vec<u64> {
    // let mut c = 2;
    // let mut v = Vec::new();

    // while n != 1 {
    //     if n % c == 0 {
    //         n /= c;
    //         v.push(c);
    //     } else {
    //         c += 1;
    //     }
    // }
    // v

    let mut v = Vec::new();

    while n != 1 {
        let i = (2..n + 1).find(|v| n % v == 0).unwrap();
        v.push(i);
        n /= i;
    }
    v
}
